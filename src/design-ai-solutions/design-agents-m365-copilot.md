<div style="page-break-before: always;"></div>

# 2.2.2 Design Agents in Microsoft 365 Copilot

## Overview

Microsoft 365 Copilot agents extend Copilot's capabilities by integrating custom skills, connecting to external data sources, and automating workflows across the Microsoft 365 ecosystem.

## Types of M365 Copilot Agents

### 1. Declarative Agents
**Characteristics**:
- Configuration-based (no code required)
- Extend Copilot with specific instructions
- Connect to data sources
- Define custom knowledge and behavior

**Use Cases**:
- Department-specific assistants (HR, Finance, Sales)
- Role-based helpers (Manager, Executive)
- Project-specific agents

### 2. Conversational Plugins
**Characteristics**:
- API-based extensions
- Respond to natural language commands
- Execute actions across systems
- Return structured data

**Use Cases**:
- CRM integration (create leads, update opportunities)
- Project management (create tasks, update status)
- Custom business logic

### 3. Message Extensions
**Characteristics**:
- Enhance messaging in Teams
- Search and insert content
- Create rich cards
- Action-based interactions

**Use Cases**:
- Search company knowledge
- Insert templates
- Quick actions from messages

## Declarative Agent Design

### Agent Manifest Structure

**Basic Manifest**:
```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/copilot/declarative-agent/v1.0/schema.json",
  "version": "1.0",
  "name": "Sales Assistant",
  "description": "Helps sales team with CRM data and insights",
  "instructions": "You are a sales assistant. Help users with customer information, deal status, and sales insights. Always maintain confidentiality and follow company sales policies.",
  "conversation_starters": [
    {"title": "Show my pipeline", "text": "What deals are in my pipeline?"},
    {"title": "Top opportunities", "text": "Show me my top opportunities"},
    {"title": "Customer insights", "text": "Tell me about Contoso Ltd"}
  ],
  "capabilities": [
    {"name": "WebSearch"},
    {"name": "GraphConnectors"}
  ],
  "actions": [
    {
      "id": "updateDeal",
      "file": "updateDeal.json"
    }
  ]
}
```

### Key Components

**Instructions**:
```
Purpose: Define agent personality and behavior

Best Practices:
- Clear role definition
- Specific domain focus
- Behavioral guidelines
- Constraints and limitations
- Tone and style guidance

Example:
"You are a customer service expert for Contoso Electronics.
You help customers with product information, troubleshooting, and returns.
Always be friendly, professional, and solution-oriented.
If you don't know an answer, admit it and offer to connect with a specialist.
Never make promises about refunds or replacements without checking policy."
```

**Conversation Starters**:
```json
[
  {
    "title": "Check order status",
    "text": "Where is my order #12345?"
  },
  {
    "title": "Return product",
    "text": "I want to return an item"
  },
  {
    "title": "Product comparison",
    "text": "Compare Product A and Product B"
  }
]
```

**Capabilities**:
- `WebSearch`: Enable web search
- `GraphConnectors`: Access Microsoft Graph connectors
- `OneDriveAndSharePoint`: Access files
- `Plugins`: Use specific plugins

### Knowledge Sources

**Microsoft Graph Connectors**:
```
Connect to:
- SharePoint sites
- OneDrive folders
- Microsoft Teams
- Third-party systems (via Graph connectors)

Configuration:
{
  "capabilities": [
    {
      "name": "GraphConnectors",
      "connections": [
        {
          "connection_id": "salesforce_connector"
        }
      ]
    }
  ]
}
```

**SharePoint Integration**:
```
Specify:
- Site URLs
- Document libraries
- Specific folders
- Content types

Security:
- Respects user permissions
- Row-level security enforced
- Audit logging maintained
```

## Plugin Development

### API Plugin Structure

**Plugin Manifest**:
```json
{
  "schema_version": "v2",
  "name_for_human": "CRM Helper",
  "name_for_model": "crm_helper",
  "description_for_human": "Access and manage CRM data",
  "description_for_model": "Helps users access customer information, update deals, and view sales metrics from the CRM system",
  "api": {
    "type": "openapi",
    "url": "https://api.contoso.com/crm/openapi.yaml"
  },
  "auth": {
    "type": "oauth",
    "authorization_url": "https://auth.contoso.com/oauth/authorize",
    "client_url": "https://api.contoso.com/oauth/client"
  },
  "logo_url": "https://contoso.com/logo.png",
  "contact_email": "support@contoso.com",
  "legal_info_url": "https://contoso.com/legal"
}
```

### OpenAPI Specification

**Example Operation**:
```yaml
openapi: 3.0.0
info:
  title: CRM API
  version: 1.0.0
paths:
  /deals/{dealId}:
    get:
      summary: Get deal information
      operationId: getDeal
      description: Retrieve details about a specific deal by ID
      parameters:
        - name: dealId
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Deal'
```

### Authentication Methods

**OAuth 2.0** (Recommended):
```json
{
  "auth": {
    "type": "oauth",
    "authorization_url": "https://auth.example.com/oauth/authorize",
    "client_url": "https://api.example.com/oauth/client",
    "scope": "read:deals write:deals",
    "authorization_content_type": "application/x-www-form-urlencoded"
  }
}
```

**API Key**:
```json
{
  "auth": {
    "type": "service_http",
    "authorization_type": "bearer",
    "verification_tokens": {
      "openai": "abc123def456"
    }
  }
}
```

## Design Patterns

### Pattern 1: Data Retrieval Agent

**Purpose**: Fetch and display information from systems

**Example - HR Assistant**:
```
Agent: HR Policies & Benefits

Instructions:
"You are an HR assistant that helps employees understand policies,
benefits, and procedures. Retrieve information from the HR knowledge base
and company policies. For personal HR matters, direct to HR portal."

Knowledge Sources:
- SharePoint: HR Policies site
- Graph Connector: Benefits system
- OneDrive: Employee handbook

Conversation Starters:
- "What's the PTO policy?"
- "Explain health insurance options"
- "How do I submit expenses?"
```

### Pattern 2: Action-Oriented Agent

**Purpose**: Perform tasks and update systems

**Example - IT Helpdesk Agent**:
```
Plugin Actions:
1. Reset Password
   POST /api/users/{userId}/resetPassword

2. Create Ticket
   POST /api/tickets

3. Check Service Status
   GET /api/services/status

User Flow:
User: "Reset my password"
→ Agent identifies action needed
→ Confirms user identity
→ Calls resetPassword API
→ Confirms completion
```

### Pattern 3: Analytics Agent

**Purpose**: Provide insights and analysis

**Example - Sales Analytics**:
```
Agent: Sales Insights

Capabilities:
- Query Dataverse for sales data
- Calculate metrics (pipeline value, win rate)
- Generate visualizations
- Provide recommendations

Integration:
- Power BI datasets
- Dynamics 365 Sales
- Custom analytics API

Sample Queries:
- "Show me Q4 sales performance"
- "What's my team's win rate?"
- "Forecast revenue for next month"
```

## User Experience Design

### Conversation Design
```
Good Example:
User: "Update the Contoso deal"
Agent: "I can help with that. What would you like to update on the Contoso deal?
- Amount
- Close date
- Stage
- Notes"

Poor Example:
User: "Update the Contoso deal"
Agent: "Provide: deal_id, field, new_value"
[Too technical, not conversational]
```

### Error Handling
```
Graceful Errors:
- "I'm having trouble connecting to the CRM system right now. Please try again in a few minutes."
- "I couldn't find a deal with that name. Could you provide the deal ID?"
- "I don't have permission to update that field. Please contact your admin."

Avoid:
- "Error 500: Internal Server Error"
- "Null reference exception"
- Generic "Something went wrong"
```

### Rich Responses
```
Use Adaptive Cards:
- Display structured data beautifully
- Include action buttons
- Show images and media
- Support interactive elements

Example:
Deal Card:
┌─────────────────────────┐
│ Contoso Ltd Deal       │
├─────────────────────────┤
│ Amount: $50,000        │
│ Stage: Negotiation     │
│ Close Date: 2024-03-15 │
│ Owner: Jane Smith      │
├─────────────────────────┤
│ [Update] [View Details]│
└─────────────────────────┘
```

## Deployment and Distribution

### Packaging
```
Package Contents:
- Agent manifest (JSON)
- App manifest
- Icons (color and outline)
- Localization files (optional)

Deployment Methods:
- Upload to Teams app catalog
- Microsoft AppSource
- Direct deployment (side-loading)
```

### Governance
```
Admin Controls:
- Allow/block specific agents
- Assign to users/groups
- Usage monitoring
- Compliance policies
- Data governance
```

## Best Practices

1. **Clear Instructions**: Define role and boundaries explicitly
2. **Relevant Knowledge**: Connect only necessary data sources
3. **Security First**: Minimal permissions, audit logging
4. **User-Centric**: Design for end-user experience
5. **Test Thoroughly**: Diverse scenarios and edge cases
6. **Monitor Usage**: Track adoption and performance
7. **Iterate**: Improve based on feedback
8. **Documentation**: Clear user and admin guides

## Common Pitfalls

- **Too Broad Scope**: Agent tries to do too much
- **Unclear Instructions**: Vague or contradictory guidance
- **Poor Error Handling**: Technical errors exposed to users
- **Slow Responses**: API calls not optimized
- **Security Issues**: Over-permissioned access
- **No Fallback**: No human escalation path

## Related Resources

- [Microsoft 365 Copilot extensibility](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/)
- [Declarative agents](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/declarative-copilots)
- [Plugins for Copilot](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/build-plugins)
- [Microsoft Graph connectors](https://learn.microsoft.com/en-us/microsoftsearch/connectors-overview)
