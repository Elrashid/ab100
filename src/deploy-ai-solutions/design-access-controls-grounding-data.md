<div style="page-break-before: always;"></div>

# 3.4.7 Design Access Controls on Grounding Data

## Overview

Access controls for grounding data ensure that AI systems only access and retrieve information that users are authorized to see, maintaining data security and privacy.

## Access Control Principles

### Least Privilege

```
Principle: Grant minimum necessary access

Implementation:
- User-specific permissions
- Role-based access (RBAC)
- Time-bound access
- Just-in-time access

Example:
- Sales rep: Only their accounts
- Manager: Team accounts
- Admin: All accounts
```

### Need-to-Know

```
Principle: Access only required information

Application:
- Filter grounding data by user
- Restrict sensitive content
- Context-aware filtering
- Dynamic permissions
```

## Access Control Models

### Role-Based Access Control (RBAC)

```
Structure:
Roles → Permissions → Resources

Example:
Role: Sales Manager
Permissions:
  - Read: Own team data
  - Write: Own opportunities
  - View: Company reports

Implementation in Dataverse:
- Security roles
- Business units
- Teams
- Field-level security
```

### Attribute-Based Access Control (ABAC)

```
Structure:
User Attributes + Resource Attributes + Context → Access Decision

Example:
IF user.department = "Sales"
AND resource.region = user.region
AND time.hour >= 8 AND time.hour <= 18
THEN grant access

Use Cases:
- Multi-tenant scenarios
- Complex hierarchies
- Dynamic permissions
```

### Row-Level Security

```
Purpose: Filter data at row level

Implementations:

1. SharePoint:
   - Item permissions
   - Audience targeting
   - Security groups

2. Dataverse:
   - Business unit hierarchy
   - Owner-based security
   - Position hierarchy

3. SQL/Fabric:
   - Security predicates
   - Inline table-valued functions
   
Example (SQL):
CREATE FUNCTION Security.fn_securitypredicate
(@UserID int)
RETURNS TABLE
WITH SCHEMABINDING
AS
RETURN SELECT 1 AS fn_securitypredicate_result
WHERE @UserID = USER_ID() OR IS_MEMBER('Manager') = 1;
```

### Column-Level Security

```
Purpose: Restrict sensitive fields

Examples:
- SSN fields
- Salary information
- Personal health data
- Financial details

Implementation:
- Field-level security (Dataverse)
- Column permissions (SQL)
- Attribute restrictions
```

## Microsoft Platform Implementations

### SharePoint/OneDrive

```
Access Controls:
- Site permissions
- Document library permissions
- Item-level permissions
- Folder permissions
- Sharing links (Anyone, Specific people, Organization)

AI Integration:
- Graph API respects permissions
- Search results filtered by access
- Copilot sees only accessible content

Configuration:
{
  "permissions": {
    "siteAccess": "members",
    "documentLibrary": "contribute",
    "sensitiveFolder": "owners",
    "itemLevel": true
  }
}
```

### Dataverse

```
Security Layers:
1. Environment security
2. Business unit security
3. Security roles
4. Record-level security
5. Field-level security
6. Column security profiles

AI Considerations:
- Agents honor all security
- Grounding respects permissions
- Filtered responses

Example:
Security Role: Sales Representative
Privileges:
- Account: Read (User)
- Contact: Read (Business Unit)
- Opportunity: Read/Write (User)
- Quote: No Access
```

### Azure AI Search

```
Security Features:
- Index-level permissions
- Document-level security trimming
- Field-level security

Implementation:
1. Security filters in queries
2. User context in search
3. Dynamic filtering

Example:
{
  "search": "AI solutions",
  "filter": "security_groups/any(g: g eq 'Sales')"
}
```

### Microsoft Fabric

```
Access Controls:
- Workspace roles
- Item permissions
- Row-level security
- Object-level security

OneLake Security:
- Folder permissions
- File permissions
- Shortcut permissions
```

## Implementation Patterns

### Pattern 1: User Context Propagation

```
Flow:
User → Agent → Grounding Data
       ↓
   User Identity Passed
       ↓
   Filtered Results

Implementation:
- Pass user token to search
- Apply security context
- Filter based on permissions
- Return authorized data only

Code Example:
async function getGroundingData(userToken, query) {
  const userContext = await validateToken(userToken);
  const searchClient = createSearchClient(userContext);
  const results = await searchClient.search(query, {
    filter: buildSecurityFilter(userContext.permissions)
  });
  return results;
}
```

### Pattern 2: Pre-Filtered Indices

```
Approach:
- Create user/role-specific indices
- Pre-filter during indexing
- Route to appropriate index

Use Cases:
- Multi-tenant scenarios
- Clear role boundaries
- Performance optimization
```

### Pattern 3: Dynamic Filtering

```
Approach:
- Single index with security metadata
- Filter at query time
- Based on user context

Example:
Document Metadata:
{
  "content": "...",
  "security_groups": ["Sales", "Management"],
  "region": "West",
  "classification": "Internal"
}

Query Filter:
filter: security_groups/any(g: g in ('Sales')) 
  and region eq 'West'
```

## Agent Integration

### Copilot Studio

```
Security Integration:
- Uses authenticated user context
- Respects data source permissions
- Variables for user identity

Implementation:
1. Enable authentication
2. Pass user token to connectors
3. Filter knowledge sources
4. Apply data source security

Configuration:
Authentication: Azure AD
Scope: User.Read, Sites.Read.All
Pass token: Yes
Filter by user: Yes
```

### Custom Agents (Azure OpenAI)

```
Implementation:
1. Authenticate user
2. Retrieve user permissions
3. Filter grounding data
4. Generate response
5. Apply output filtering

Code:
# Retrieve context with security
def get_user_context(user_id):
    permissions = get_user_permissions(user_id)
    return build_search_filter(permissions)

# Search with security
def search_with_security(query, user_id):
    filter = get_user_context(user_id)
    results = search_service.search(
        query, 
        filter=filter,
        select=["content", "metadata"]
    )
    return [r for r in results if user_can_access(r, user_id)]
```

## Testing Access Controls

```
Test Scenarios:
1. User without access attempts query
   Expected: No restricted data in response

2. User with partial access queries
   Expected: Only authorized data returned

3. User attempts to elevate privileges
   Expected: Access denied

4. Cross-tenant data access attempt
   Expected: Blocked

Test Approach:
- Create test users with different roles
- Query same content
- Verify filtered results
- Check audit logs
```

## Monitoring and Auditing

```
Log:
- Access attempts
- Granted permissions
- Denied access
- Permission changes
- Unusual patterns

Alerts:
- Repeated access denials
- Privilege escalation attempts
- Unusual data access patterns
- Bulk data retrieval

Tools:
- Azure Monitor
- Microsoft Purview
- Audit logs
- Security Center
```

## Best Practices

1. **Default Deny**: Explicit grants only
2. **User Context**: Always propagate identity
3. **Layered Security**: Multiple control levels
4. **Regular Reviews**: Audit permissions
5. **Least Privilege**: Minimum necessary access
6. **Separation of Duties**: Role segregation
7. **Testing**: Validate controls work
8. **Monitoring**: Track access patterns
9. **Documentation**: Maintain access matrix
10. **Compliance**: Meet regulatory requirements

## Common Pitfalls

```
Avoid:
❌ Over-permissive defaults
❌ Shared accounts
❌ Stale permissions
❌ Bypassing security in code
❌ Not propagating user context
❌ Insufficient testing

Do:
✓ Principle of least privilege
✓ Individual user accounts
✓ Regular access reviews
✓ Respect platform security
✓ Pass user identity
✓ Comprehensive testing
```

## Related Resources

- [Dataverse Security](https://learn.microsoft.com/en-us/power-platform/admin/security-concepts)
- [SharePoint Permissions](https://learn.microsoft.com/en-us/sharepoint/modern-experience-sharing-permissions)
- [Azure AI Search Security](https://learn.microsoft.com/en-us/azure/search/search-security-trimming-for-azure-search)
- [Row-Level Security](https://learn.microsoft.com/en-us/fabric/security/service-admin-row-level-security)
