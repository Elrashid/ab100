<div style="page-break-before: always;"></div>

# 3.4.6 Validate Data Residency and Movement Compliance

## Overview

Data residency and compliance validation ensures AI systems meet regulatory requirements for data location, protection, and handling across jurisdictions.

## Data Residency Requirements

### Regional Requirements

```
Considerations:
- GDPR (EU): Data must stay in EU
- China: Data localization laws
- Russia: Data localization required
- India: Payment data localization
- Australia: Privacy Act requirements

Implementation:
- Azure regions selection
- Data sovereignty policies
- Cross-border restrictions
- Local data processing
```

### Azure Geography Selection

```
Strategy:
- Deploy in required regions
- Use regional pairs for DR
- Restrict data movement
- Configure geo-fencing

Example Regions:
- EU: West Europe, North Europe
- US: East US, West US
- Asia: Southeast Asia, East Asia
- Australia: Australia East, Australia Southeast
```

## Compliance Frameworks

### GDPR (General Data Protection Regulation)

```
Requirements:
- Lawful basis for processing
- Data minimization
- Purpose limitation
- Storage limitation
- Right to erasure
- Data portability
- Privacy by design

AI-Specific:
- Automated decision-making disclosure
- Right to explanation
- Profiling transparency
- Consent for AI processing

Implementation:
- Data classification
- Consent management
- Retention policies
- Deletion workflows
- Audit trails
```

### CCPA/CPRA (California Privacy)

```
Requirements:
- Right to know
- Right to delete
- Right to opt-out
- Non-discrimination

Implementation:
- Privacy notices
- Opt-out mechanisms
- Data inventory
- Vendor management
```

### HIPAA (Healthcare)

```
Requirements:
- Protected Health Information (PHI)
- Business Associate Agreements
- Encryption requirements
- Access controls
- Audit logs

AI Considerations:
- De-identification before training
- Secure AI processing
- PHI in prompts/responses
- Minimum necessary principle
```

### SOX (Financial)

```
Requirements:
- Financial data controls
- Audit trails
- Change management
- Access controls
- Documentation

AI Impact:
- Model governance
- Decision documentation
- Change tracking
- Validation processes
```

## Validation Process

### 1. Requirements Identification

```
Steps:
1. Identify applicable regulations
2. Map data flows
3. Determine storage locations
4. Document requirements
5. Create compliance matrix

Regulations Matrix:
| Data Type | Regulation | Requirement | Status |
|-----------|-----------|-------------|--------|
| PII | GDPR | EU storage | ✓ |
| PHI | HIPAA | Encryption | ✓ |
| Financial | SOX | Audit trail | ✓ |
```

### 2. Technical Implementation

```
Azure Configuration:
- Select compliant regions
- Enable encryption
- Configure access controls
- Set up audit logging
- Implement DLP policies

Validation:
resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: 'compliantstorage'
  location: 'westeurope'  // GDPR compliant
  properties: {
    minimumTlsVersion: 'TLS1_2'
    encryption: {
      requireInfrastructureEncryption: true
    }
    networkAcls: {
      bypass: 'None'
      defaultAction: 'Deny'
    }
  }
}
```

### 3. Compliance Validation

```
Validate:
☐ Data stored in required regions
☐ Encryption enabled
☐ Access controls configured
☐ Audit logging active
☐ DLP policies applied
☐ Retention policies set
☐ Deletion processes work
☐ Documentation complete
```

## Data Classification

```
Categories:
1. Public: No restrictions
2. Internal: Employee only
3. Confidential: Restricted access
4. Restricted: Highly sensitive

AI Implications:
- Public: Can use for training
- Internal: Restricted training use
- Confidential: No training use
- Restricted: Strict controls

Labels:
- Microsoft Information Protection
- Azure Purview
- Sensitivity labels
```

## Cross-Border Data Transfer

### Transfer Mechanisms

```
GDPR Compliant:
- Standard Contractual Clauses (SCCs)
- Binding Corporate Rules (BCRs)
- Adequacy decisions
- Explicit consent

Implementation:
- Document transfer basis
- Assess third countries
- Implement safeguards
- Regular reviews
```

### Microsoft Compliance

```
Certifications:
- ISO 27001, 27018, 27701
- SOC 1, 2, 3
- GDPR, HIPAA, SOX compliant
- Regional certifications

Data Protection Terms:
- EU Model Clauses
- Data Processing Agreement
- Data Protection Addendum
```

## Monitoring and Auditing

### Compliance Monitoring

```
Monitor:
- Data location
- Access patterns
- Data movements
- Policy violations
- Compliance status

Tools:
- Microsoft Purview
- Azure Policy
- Compliance Manager
- Security Center
```

### Audit Requirements

```
Maintain:
- Access logs
- Data processing records
- Consent records
- Impact assessments
- Vendor agreements
- Training records

Retention:
- GDPR: 3+ years
- HIPAA: 6 years
- SOX: 7 years
- Varies by regulation
```

## Azure Compliance Tools

### Microsoft Purview

```
Capabilities:
- Data discovery
- Data classification
- Data lineage
- Compliance reporting
- Policy enforcement

Usage:
- Scan data estates
- Apply labels
- Track data flow
- Generate reports
```

### Azure Policy

```
Purpose: Enforce compliance rules

Examples:
- Allowed locations policy
- Require encryption
- Require tags
- Audit non-compliance

Implementation:
{
  "policyRule": {
    "if": {
      "field": "location",
      "notIn": ["westeurope", "northeurope"]
    },
    "then": {
      "effect": "deny"
    }
  }
}
```

### Compliance Manager

```
Features:
- Compliance score
- Improvement actions
- Assessment templates
- Documentation hub

Use for:
- Track compliance
- Identify gaps
- Prioritize actions
- Generate reports
```

## Best Practices

1. **Know Your Data**: Classify and inventory
2. **Region Selection**: Deploy in compliant regions
3. **Encryption Always**: At rest and in transit
4. **Access Controls**: Principle of least privilege
5. **Audit Everything**: Comprehensive logging
6. **Regular Reviews**: Ongoing validation
7. **Documentation**: Maintain compliance records
8. **Training**: Educate team on requirements
9. **Vendor Due Diligence**: Verify compliance
10. **Incident Response**: Ready for breaches

## Compliance Checklist

```
Pre-Deployment:
☐ Regulations identified
☐ Data classified
☐ Regions selected
☐ Encryption configured
☐ Access controls set
☐ DLP policies applied
☐ Documentation prepared

Post-Deployment:
☐ Monitoring enabled
☐ Audits scheduled
☐ Compliance validated
☐ Reports generated
☐ Training completed
```

## Related Resources

- [Azure Compliance](https://learn.microsoft.com/en-us/azure/compliance/)
- [Microsoft Trust Center](https://www.microsoft.com/en-us/trust-center)
- [GDPR Compliance](https://learn.microsoft.com/en-us/compliance/regulatory/gdpr)
- [Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/)
