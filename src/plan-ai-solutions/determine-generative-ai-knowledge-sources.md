<div style="page-break-before: always;"></div>

# 1.2.6 Determine Use of Generative AI and Knowledge Sources

## Overview

Generative AI in Copilot Studio enables agents to provide dynamic, contextual responses using grounding data from various knowledge sources.

## Generative AI Capabilities in Copilot Studio

### Generative Answers
- Dynamic responses based on knowledge sources
- Natural language understanding
- Context-aware conversations
- Multi-turn dialogues

### Integration Points
- Classic topics (rules-based)
- Generative topics (AI-driven)
- Hybrid approaches
- Fallback mechanisms

## Knowledge Source Types

### SharePoint
- **Use Case**: Document libraries, policies, procedures
- **Benefits**: Version control, permissions, familiar to users
- **Considerations**: Indexing time, file format support

### OneDrive
- **Use Case**: Personal or shared documents
- **Benefits**: Easy access, Microsoft 365 integration
- **Considerations**: Permission management, file organization

### Websites and URLs
- **Use Case**: Public documentation, knowledge bases
- **Benefits**: Always up-to-date, external content
- **Considerations**: Content stability, access reliability

### Dataverse
- **Use Case**: Structured business data, CRM records
- **Benefits**: Secure, governed, real-time data
- **Considerations**: Table design, data volume

### Custom Data Sources
- **Use Case**: Legacy systems, external databases
- **Benefits**: Comprehensive coverage
- **Considerations**: Integration complexity, maintenance

## When to Use Generative AI

### Good Fit Scenarios
✅ Large knowledge bases (documents, FAQs)
✅ Varied user questions
✅ Need for natural conversation
✅ Content changes frequently
✅ Complex queries requiring synthesis

### Poor Fit Scenarios
❌ Highly structured workflows
❌ Transactional processes
❌ Deterministic decision trees
❌ Real-time critical systems
❌ Scenarios requiring exact reproducibility

## Knowledge Source Configuration

### Connection Setup
1. Add knowledge source in Copilot Studio
2. Configure authentication
3. Select content (sites, libraries, tables)
4. Enable indexing
5. Test retrieval

### Optimization
- **Chunking**: Break content into meaningful segments
- **Metadata**: Add descriptive information
- **Relevance**: Improve search accuracy
- **Freshness**: Set update frequency
- **Filtering**: Limit scope for performance

## Grounding Strategies

### Single Source Grounding
- Use one knowledge source
- Simpler setup
- Limited coverage

### Multi-Source Grounding
- Combine multiple sources
- Comprehensive answers
- Ranked retrieval
- Source attribution

### Hybrid Approach
- Topics for structured flows
- Generative for open-ended questions
- Best of both worlds

## Content Quality Guidelines

### Document Preparation
- Clear, concise writing
- Logical structure
- Descriptive headings
- Consistent formatting
- Regular updates

### Metadata Requirements
- Document titles
- Descriptions
- Keywords/tags
- Last modified dates
- Owner information

## Responsible AI Considerations

### Content Validation
- Verify accuracy before indexing
- Regular content audits
- Version control
- Approval workflows

### Bias Prevention
- Diverse content sources
- Inclusive language
- Regular review
- User feedback loops

### Privacy and Security
- Access control enforcement
- PII detection
- Data classification
- Audit trails

## Monitoring and Optimization

### Key Metrics
- Answer quality ratings
- Source relevance scores
- Query success rates
- Response times
- User satisfaction

### Continuous Improvement
- Analyze failed queries
- Update knowledge sources
- Refine prompts
- Adjust grounding parameters

## Best Practices

1. Start with high-quality, authoritative sources
2. Implement source attribution
3. Regular content refresh cycles
4. Monitor and respond to feedback
5. Combine with traditional topics for critical flows
6. Test with diverse queries
7. Document knowledge source strategy

## Common Pitfalls

- Outdated content in knowledge sources
- Poor document structure
- Too many sources (noise)
- Inadequate permissions
- No content governance
- Ignoring user feedback

## Related Resources

- [Generative answers in Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/nlu-boost-conversations)
- [Knowledge sources configuration](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-base-setup)
