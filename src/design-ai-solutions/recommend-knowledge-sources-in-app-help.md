# Recommend the Process of Adding Knowledge Sources to In-App Help and Guidance for Dynamics 365 Finance or Supply Chain Management Apps

## Overview

Enriching in-app help in Dynamics 365 F&O with custom knowledge sources improves user productivity by providing contextual, organization-specific guidance.

## Knowledge Source Options

### Native Help Content
- Microsoft standard documentation
- Task guides
- How-to articles
- Video tutorials

### Custom Knowledge Sources
- **Internal Documentation**: Company-specific procedures
- **SharePoint**: Policy documents, SOPs
- **Training Materials**: Custom guides
- **FAQ Database**: Common questions and answers
- **Best Practices**: Organizational knowledge

## Implementation Process

### Step 1: Identify Knowledge Sources

**Assess Current Help Needs**:
```
Analyze:
- Common support tickets
- User questions
- Training requests
- Process documentation gaps

Identify:
- High-value topics
- Frequently needed info
- Complex processes
- Organization-specific procedures
```

### Step 2: Prepare Content

**Content Requirements**:
```
Format:
- Clear, concise language
- Step-by-step instructions
- Screenshots where helpful
- Searchable text

Organization:
- Logical categorization
- Consistent structure
- Proper metadata
- Version control
```

### Step 3: Configure Integration

**SharePoint Integration**:
```
Setup:
1. Create SharePoint site for help content
2. Organize by module/process
3. Set appropriate permissions
4. Enable search indexing

F&O Configuration:
- Add SharePoint as knowledge source
- Configure search settings
- Map content to F&O areas
- Set context triggers
```

**Custom Help Pane**:
```
Development:
- Create custom help control
- Connect to knowledge sources
- Implement search functionality
- Add context awareness

Deployment:
- Add to relevant forms
- Configure for user roles
- Test thoroughly
- Train users
```

### Step 4: Implement Contextual Help

**Context-Aware Help**:
```
Trigger Conditions:
- Current form/page
- User role
- Transaction type
- Process step

Display Relevant:
- Specific procedures
- Related articles
- Video tutorials
- Quick tips
```

### Step 5: Enable Search

**Search Configuration**:
```
Search Sources:
- Microsoft documentation
- Custom SharePoint content
- Internal knowledge base
- FAQs

Search Features:
- Keyword search
- Filtering by category
- Relevance ranking
- Recent searches
```

## Best Practices

### Content Quality
1. **User-Centric**: Write for your users' skill level
2. **Current**: Keep content up-to-date
3. **Accurate**: Verify all procedures
4. **Complete**: Cover all steps
5. **Searchable**: Use clear terminology

### Organization
1. **Categorization**: Logical grouping
2. **Tagging**: Comprehensive metadata
3. **Hierarchy**: Clear information architecture
4. **Consistency**: Standard templates

### Maintenance
1. **Regular Reviews**: Quarterly content audits
2. **User Feedback**: Collect and act on feedback
3. **Analytics**: Track usage patterns
4. **Updates**: Align with system changes

## Integration Patterns

### Pattern 1: Embedded Help Panel
```
F&O Form → Help Panel (sidebar)
    ↓
Context Detection
    ↓
Search Knowledge Sources
    ↓
Display Relevant Articles
```

### Pattern 2: Intelligent Search
```
User Search Query
    ↓
Search Across:
- F&O help
- SharePoint
- Custom sources
    ↓
Ranked Results
    ↓
Suggested Articles
```

### Pattern 3: Task Guidance
```
User Starts Process
    ↓
System Detects Task
    ↓
Offers Guided Walkthrough
    ↓
Step-by-Step Help
    ↓
Completion Confirmation
```

## Measuring Success

### Key Metrics
- Help content usage
- Search effectiveness (click-through)
- User satisfaction ratings
- Support ticket reduction
- Task completion time

### Continuous Improvement
```
Process:
1. Collect metrics
2. Analyze user behavior
3. Identify gaps
4. Update content
5. Monitor impact
6. Iterate
```

## Tools and Technologies

### Content Creation
- Microsoft Word/SharePoint
- Screen capture tools (SnagIt, etc.)
- Video recording
- Diagram tools

### Integration
- SharePoint Framework (SPFx)
- Power Apps
- Azure Search
- Microsoft Graph

## Related Resources

- [Dynamics 365 F&O help system](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/help-overview)
- [Task recorder](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/task-recorder)
- [SharePoint integration](https://learn.microsoft.com/en-us/sharepoint/dev/)
