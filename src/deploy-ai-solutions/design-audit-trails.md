<div style="page-break-before: always;"></div>

# 3.4.8 Design Audit Trails for Changes

## Overview

Audit trails provide comprehensive logging of AI system activities for compliance, security, troubleshooting, and accountability.

## Audit Trail Components

### What to Log

```
Essential Events:
1. User Activities
   - Authentication/authorization
   - Queries submitted
   - Actions taken
   - Access attempts

2. System Activities
   - Model predictions
   - Confidence scores
   - Data accessed
   - Errors/exceptions

3. Administrative Activities
   - Configuration changes
   - Model deployments
   - Permission changes
   - Policy updates

4. Data Activities
   - Data access
   - Data modifications
   - Data exports
   - Data deletions
```

### Audit Log Structure

```
Standard Fields:
- Timestamp (ISO 8601, UTC)
- Event ID (unique identifier)
- Event type/category
- User ID
- User IP address
- Resource accessed
- Action performed
- Result (success/failure)
- Request details
- Response summary
- Session ID
- Correlation ID

Example:
{
  "timestamp": "2025-11-11T14:30:00Z",
  "eventId": "evt-12345",
  "eventType": "agent.query",
  "userId": "user@contoso.com",
  "userIp": "203.0.113.42",
  "resource": "sales-copilot",
  "action": "query",
  "query": "Show top opportunities",
  "result": "success",
  "confidence": 0.95,
  "dataSourcesAccessed": ["Dataverse", "SharePoint"],
  "recordsReturned": 10,
  "sessionId": "sess-789",
  "correlationId": "corr-456"
}
```

## Platform-Specific Auditing

### Azure AI Services

```
Audit Sources:
- Azure Monitor
- Diagnostic logs
- Application Insights
- Azure Activity logs

Configuration:
resource diagnosticSettings 'Microsoft.Insights/diagnosticSettings@2021-05-01' = {
  name: 'ai-audit-logs'
  scope: cognitiveService
  properties: {
    logs: [
      {
        category: 'Audit'
        enabled: true
        retentionPolicy: {
          enabled: true
          days: 365
        }
      }
      {
        category: 'RequestResponse'
        enabled: true
      }
    ]
    metrics: [
      {
        category: 'AllMetrics'
        enabled: true
      }
    ]
    workspaceId: logAnalyticsWorkspace.id
  }
}
```

### Copilot Studio

```
Audit Features:
- Conversation transcripts
- User actions
- Topic triggers
- Flow executions
- Connector calls

Access Logs:
- Power Platform admin center
- Dataverse audit logs
- Analytics dashboard

Key Events:
- Agent created/modified
- Topic added/changed
- Agent published
- Conversations
- Errors
```

### Microsoft 365 Copilot

```
Audit Logs:
- Microsoft Purview
- Unified audit log
- Compliance center

Events:
- Copilot interactions
- Data accessed
- Permissions used
- Plugins invoked

Search:
Search-UnifiedAuditLog -Operations "CopilotInteraction" `
  -StartDate (Get-Date).AddDays(-30) `
  -EndDate (Get-Date)
```

### Dataverse

```
Auditing Levels:
1. Organization level
2. Entity level
3. Attribute level

Configuration:
- Enable in settings
- Select entities
- Choose attributes
- Set retention

Access:
- Audit Summary View
- Audit History
- Power Automate
- Reports

Example Query:
// Retrieve audit records
var query = new QueryExpression("audit")
{
    ColumnSet = new ColumnSet(
        "createdon", 
        "userid", 
        "operation", 
        "objectid"
    ),
    Criteria = {
        Conditions = {
            new ConditionExpression(
                "createdon", 
                ConditionOperator.GreaterThan, 
                DateTime.UtcNow.AddDays(-7)
            )
        }
    }
};
```

## Compliance Requirements

### GDPR

```
Requirements:
- Log data access
- Track consent
- Record deletions
- Audit data transfers
- Retention policies

Retention:
- 3-6 years typical
- Varies by jurisdiction
- Secure storage
- Tamper-proof
```

### HIPAA

```
Requirements:
- Access logs (who, what, when, where)
- Modification logs
- Security incident logs
- Minimum 6 years retention

Implementation:
- Comprehensive logging
- Protected audit logs
- Regular reviews
- Audit reports
```

### SOX

```
Requirements:
- Financial data access
- System changes
- Model decisions
- 7 years retention

Controls:
- Segregation of duties
- Change management logs
- Approval trails
- Exception tracking
```

## Audit Storage

### Azure Solutions

```
1. Log Analytics Workspace
   - Centralized logging
   - Query with KQL
   - Alerting
   - Long-term retention

2. Storage Accounts
   - Archive logs
   - Cost-effective
   - Immutable storage
   - Compliance retention

3. Event Hub
   - Stream to SIEM
   - Real-time processing
   - Integration hub

4. Application Insights
   - Application-level logs
   - Performance data
   - Custom events
   - Dashboards
```

### Retention Strategy

```
Tier 1: Hot (0-90 days)
- Log Analytics
- Quick access
- Real-time queries

Tier 2: Cool (90 days - 1 year)
- Storage Account
- Occasional access
- Lower cost

Tier 3: Archive (1+ years)
- Archive storage
- Compliance retention
- Lowest cost
- Rare retrieval

Configuration:
{
  "retentionPolicy": {
    "hot": 90,
    "cool": 365,
    "archive": 2555
  }
}
```

## Audit Analysis

### KQL Queries

```
// Failed authentication attempts
AuditLogs
| where TimeGenerated > ago(24h)
| where ActivityDisplayName == "Failed sign-in"
| summarize FailedAttempts = count() by UserPrincipalName
| where FailedAttempts > 5
| order by FailedAttempts desc

// AI agent queries
AppInsights
| where TimeGenerated > ago(7d)
| where Type == "AgentQuery"
| summarize QueryCount = count() by UserId, bin(TimeGenerated, 1h)
| render timechart

// Data access patterns
DataverseAudit
| where Operation in ("Read", "ReadMultiple")
| summarize AccessCount = count() by UserId, EntityName
| where AccessCount > 100
| order by AccessCount desc
```

### Anomaly Detection

```
Detect:
- Unusual access patterns
- After-hours activity
- Bulk data access
- Failed authorization spikes
- Geographic anomalies

Techniques:
- Statistical analysis
- Machine learning
- Rule-based detection
- Behavioral baselines

Alerts:
- Real-time notifications
- Email/Teams alerts
- SIEM integration
- Incident creation
```

## Security and Compliance

### Audit Log Protection

```
Controls:
- Immutable logs
- Encrypted storage
- Access restricted
- Tamper detection
- Backup/replication

Azure Implementation:
- WORM (Write Once Read Many)
- Legal hold
- Time-based retention
- Access policies
- Audit log auditing (meta-audit)
```

### Audit Reviews

```
Regular Reviews:
- Daily: Security incidents
- Weekly: Access patterns
- Monthly: Compliance check
- Quarterly: Comprehensive review
- Annual: Audit assessment

Reviewers:
- Security team
- Compliance officers
- IT audit
- Business owners
- External auditors
```

## Monitoring and Alerting

### Alert Rules

```
Critical Alerts:
- Multiple failed logins
- Unauthorized access attempts
- Privilege escalation
- Data exfiltration patterns
- System configuration changes
- Model tampering

Example Alert:
{
  "alert": "Suspicious AI Agent Access",
  "condition": "FailedQueries > 10 in 5 minutes",
  "action": [
    "Email security team",
    "Create incident",
    "Block user (optional)"
  ]
}
```

### Dashboards

```
Key Metrics:
- Total queries
- Success/failure rate
- Active users
- Response times
- Data sources accessed
- Error trends
- Compliance status

Tools:
- Power BI
- Azure Dashboard
- Log Analytics workbooks
- Custom dashboards
```

## Best Practices

1. **Comprehensive Logging**: Log all relevant events
2. **Secure Storage**: Protect audit logs
3. **Retention Policies**: Meet compliance requirements
4. **Regular Reviews**: Scheduled audit reviews
5. **Automation**: Automated analysis and alerting
6. **Correlation**: Link related events
7. **Immutability**: Tamper-proof logs
8. **Performance**: Efficient logging without impact
9. **Privacy**: Mask sensitive data in logs
10. **Documentation**: Maintain audit procedures

## Audit Trail Checklist

```
Implementation:
☐ Audit logging enabled
☐ All required events captured
☐ Secure log storage configured
☐ Retention policies set
☐ Access controls on logs
☐ Monitoring and alerting active
☐ Review procedures documented
☐ Compliance validated

Maintenance:
☐ Regular log reviews scheduled
☐ Storage capacity monitored
☐ Archive process working
☐ Alert rules current
☐ Documentation updated
```

## Reporting

```
Report Types:
1. Compliance Reports
   - Regulatory requirements
   - Audit findings
   - Remediation status

2. Security Reports
   - Incidents
   - Vulnerabilities
   - Access violations

3. Operational Reports
   - System usage
   - Performance metrics
   - Error analysis

4. Executive Reports
   - High-level summary
   - Key metrics
   - Risk status
```

## Related Resources

- [Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/)
- [Microsoft Purview Audit](https://learn.microsoft.com/en-us/purview/audit-solutions-overview)
- [Dataverse Auditing](https://learn.microsoft.com/en-us/power-platform/admin/manage-dataverse-auditing)
- [Log Analytics](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-overview)
