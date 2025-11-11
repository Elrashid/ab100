<div style="page-break-before: always;"></div>

# 2.3.5 Propose Microsoft Power Platform AI Features

## Overview

Microsoft Power Platform offers comprehensive AI capabilities through AI Builder, Copilot features, and the AI Hub, enabling citizen developers to build intelligent applications.

## Power Platform AI Features

### AI Builder
**Capabilities**:
- Prebuilt models (forms, receipts, business cards, IDs)
- Custom models (object detection, text classification, prediction)
- Document processing
- Sentiment analysis
- Text generation

**When to Propose**:
✅ Need document/image processing
✅ Low-code AI development
✅ Power Apps/Power Automate integration
✅ Rapid prototyping

### Copilot in Power Apps
**Features**:
- App building assistance
- Formula generation
- Data insights
- Natural language to app

**Use Cases**:
- Accelerate app development
- Assist citizen developers
- Generate complex formulas
- Data exploration

### Copilot in Power Automate
**Features**:
- Flow creation from description
- Flow explanation
- Error troubleshooting
- Optimization suggestions

**Benefits**:
- Faster flow development
- Reduced errors
- Better practices
- Learning tool

## AI Hub

### What is AI Hub
Central location in Power Platform for:
- Discover AI capabilities
- Access AI models
- Manage AI projects
- Monitor AI usage
- Govern AI solutions

### AI Hub Features

**Model Catalog**:
```
Browse:
- Prebuilt AI models
- Custom models
- Partner models
- Azure AI services

Capabilities:
- Model details and documentation
- Try models
- Deploy to environments
- Track usage
```

**AI Project Management**:
```
Features:
- Create AI projects
- Organize models
- Collaborate with team
- Version control
- Deployment tracking
```

**Governance**:
```
Admin Controls:
- Who can create AI models
- Approved AI services
- Data policies
- Usage monitoring
- Cost tracking
```

## Proposing AI Features by Scenario

### Scenario 1: Invoice Processing
**Recommendation**: AI Builder Form Processing
```
Why:
- Prebuilt invoice model
- No code required
- Integrates with Power Automate
- Handles common invoice formats

Implementation:
- Power Automate trigger (email/SharePoint)
- AI Builder processes invoice
- Extract data to Dataverse/Excel
- Approval workflow
```

### Scenario 2: Customer Sentiment Analysis
**Recommendation**: AI Builder Sentiment Analysis
```
Why:
- Prebuilt model
- Supports multiple languages
- Easy integration
- Real-time analysis

Use:
- Analyze survey responses
- Monitor social media
- Process support tickets
- Track trends
```

### Scenario 3: Predictive Maintenance
**Recommendation**: AI Builder Prediction Model
```
Why:
- Custom model for specific equipment
- Train on historical data
- Integrate with IoT data
- Automated alerts

Process:
- Collect equipment sensor data
- Train prediction model
- Deploy in Power Automate
- Trigger maintenance workflows
```

## Selection Framework

| Need | Recommendation | Implementation Level |
|------|----------------|---------------------|
| Document processing | AI Builder prebuilt | Low-code |
| Custom classification | AI Builder custom model | Low-code |
| Complex AI scenarios | Azure AI + Power Platform | Pro-code |
| App building help | Copilot in Power Apps | No-code |
| Workflow automation | Copilot in Power Automate | Low-code |

## Best Practices

1. **Start with Prebuilt**: Use prebuilt models when possible
2. **Pilot Test**: Validate before full deployment
3. **Governance**: Implement AI governance early
4. **Training**: Educate makers on AI capabilities
5. **Monitor**: Track usage and costs
6. **Iterate**: Continuous improvement based on feedback

## AI Hub Governance

**Admin Setup**:
```
1. Enable AI Hub
   - Power Platform admin center
   - Enable for environments

2. Set Policies
   - Who can create AI models
   - Approval workflows
   - DLP policies for AI

3. Configure Monitoring
   - Usage dashboards
   - Cost tracking
   - Performance metrics

4. Establish Guidelines
   - AI development standards
   - Testing requirements
   - Deployment processes
```

## Cost Optimization

**AI Builder Credits**:
- Included in certain licenses
- Additional purchase available
- Monitor consumption
- Optimize model calls

**Strategies**:
- Cache results
- Batch processing
- Right-size models
- Use prebuilt when possible

## Related Resources

- [AI Builder](https://learn.microsoft.com/en-us/ai-builder/)
- [Copilot in Power Apps](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/ai-overview)
- [AI Hub](https://learn.microsoft.com/en-us/power-platform/admin/ai-hub)
- [Power Platform AI features](https://learn.microsoft.com/en-us/power-platform/admin/ai-features)
