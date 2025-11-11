<div style="page-break-before: always;"></div>

# 2.3.6 Design Interoperability of Finance and Operations Agent Chats

## Overview

Finance and Operations (F&O) agent chats can be enhanced by integrating additional knowledge sources beyond standard F&O data, providing richer, more contextual assistance.

## Knowledge Source Types

### Internal Sources
- **Dataverse**: Business data across Dynamics 365
- **SharePoint**: Documents, policies, procedures
- **OneDrive**: User and team files
- **Teams**: Conversations and shared knowledge
- **OneNote**: Notes and documentation

### External Sources
- **Public Websites**: Industry information
- **Partner Systems**: Supplier/customer portals
- **Regulatory Databases**: Compliance information
- **Market Data**: Financial, commodity data

## Integration Architecture

```
F&O Agent Chat
    ↓
Knowledge Integration Layer
    ├→ F&O Data (native)
    ├→ Dataverse (connected)
    ├→ SharePoint (Graph API)
    ├→ External APIs (custom connectors)
    └→ Azure AI Search (unified index)
```

## Implementation Approaches

### Approach 1: Direct Integration
```
Agent Query
    ↓
Multi-Source Search:
- Search F&O data
- Query Dataverse
- Search SharePoint
- Call external APIs
    ↓
Aggregate Results
    ↓
Ranked Response
```

### Approach 2: Unified Search Index
```
Preparation:
- Index F&O data in Azure AI Search
- Index SharePoint docs
- Index Dataverse
- Index external content

Runtime:
Agent Query → Azure AI Search → Ranked Results
```

### Approach 3: Agent Orchestration
```
Master Agent determines:
- Query type
- Required sources

Delegates to specialized agents:
- F&O Data Agent
- Policy Agent (SharePoint)
- Compliance Agent (external)

Synthesizes responses
```

## Configuration Steps

**1. Enable Multi-Source Knowledge**
```
F&O Settings:
- Enable Copilot features
- Configure data connectors
- Set permissions
- Add knowledge sources
```

**2. Configure SharePoint Integration**
```
Steps:
- Identify relevant SharePoint sites
- Set up indexing
- Configure permissions
- Test retrieval
```

**3. Add External Sources**
```
Custom Connectors:
- Define API endpoints
- Configure authentication
- Map data fields
- Test integration
```

**4. Optimize Retrieval**
```
Tuning:
- Relevance scoring
- Source prioritization
- Result ranking
- Response formatting
```

## Use Cases

### Use Case 1: Policy Guidance
```
Scenario: User asks about expense policy

Knowledge Sources:
- F&O: Expense limits, approval rules
- SharePoint: Detailed policy documents
- Dataverse: Department-specific rules

Response:
"Based on your department and role:
- Standard limit: $X [from F&O]
- Per-diem rates: [from SharePoint policy]
- Approval required: [from Dataverse rules]
See full policy: [SharePoint link]"
```

### Use Case 2: Regulatory Compliance
```
Scenario: User asks about compliance requirement

Knowledge Sources:
- F&O: Current compliance status
- External API: Latest regulatory updates
- SharePoint: Internal compliance procedures

Response:
"Current status: Compliant [F&O]
Recent update: [External API]
Required action: [SharePoint procedures]"
```

## Best Practices

1. **Relevance**: Only add sources that enhance answers
2. **Performance**: Index for fast retrieval
3. **Security**: Respect permissions across sources
4. **Attribution**: Cite sources in responses
5. **Freshness**: Keep knowledge sources updated
6. **Monitoring**: Track source usage and relevance

## Security and Compliance

**Access Control**:
```
User permissions flow through:
- F&O role-based security
- SharePoint permissions
- Dataverse security roles
- External system auth

Agent respects all permission boundaries
```

**Audit Trail**:
```
Log:
- Which sources accessed
- What data retrieved
- User who queried
- Timestamp
- Results provided
```

## Related Resources

- [F&O Copilot](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/)
- [SharePoint integration](https://learn.microsoft.com/en-us/sharepoint/dev/)
- [Azure AI Search](https://learn.microsoft.com/en-us/azure/search/)
