<div style="page-break-before: always;"></div>

# 2.1.16 Design Prompt Actions in Copilot Studio

## Overview

Prompt actions in Copilot Studio allow you to leverage generative AI to create dynamic, context-aware responses and actions within your agent conversations.

## What Are Prompt Actions?

### Definition
Prompt actions are reusable AI components that take inputs, process them through a language model (like GPT), and return generated content.

### Key Features
- Natural language processing
- Dynamic content generation
- Context-aware responses
- Reusable across topics
- Customizable behavior

## Types of Prompt Actions

### 1. Text Generation
Generate content based on prompts

**Use Cases**:
- Email drafting
- Response generation
- Content summarization
- Translation

**Example**:
```
Prompt Action: Draft Customer Email

Input:
- Customer Name
- Issue Description
- Resolution Steps

Prompt Template:
"Draft a professional email to {CustomerName} addressing their issue: {IssueDescription}.
Explain that we have resolved it using these steps: {ResolutionSteps}.
Maintain a friendly, helpful tone."

Output: Generated email text
```

### 2. Data Extraction
Extract structured information from unstructured text

**Use Cases**:
- Parse customer feedback
- Extract entities from messages
- Identify action items

**Example**:
```
Prompt Action: Extract Action Items

Input:
- Meeting Notes

Prompt Template:
"Extract all action items from these meeting notes: {MeetingNotes}
Return as a JSON array with fields: task, owner, due_date"

Output: Structured data
```

### 3. Classification
Categorize or classify content

**Use Cases**:
- Sentiment analysis
- Topic classification
- Priority assessment

**Example**:
```
Prompt Action: Classify Support Ticket

Input:
- Ticket Description

Prompt Template:
"Classify this support ticket into one of these categories:
- Technical Issue
- Billing Question
- Feature Request
- General Inquiry

Ticket: {TicketDescription}

Return only the category name."

Output: Category
```

### 4. Transformation
Transform content from one format to another

**Use Cases**:
- Simplification
- Formalization
- Reformatting

## Creating Prompt Actions

### Step-by-Step Process

**1. Define Purpose**
```
What should this action do?
What inputs does it need?
What output should it produce?
Who will use it?
```

**2. Create Prompt Template**
```
Best Practices:
- Be specific and clear
- Provide context
- Define output format
- Include examples if needed
- Set constraints

Example:
"You are a professional customer service agent.
Summarize this customer complaint in 2-3 sentences,
highlighting the main issue and requested resolution.

Complaint: {CustomerComplaint}

Summary:"
```

**3. Configure Parameters**
```
Inputs:
- Name: CustomerComplaint
- Type: Text
- Required: Yes
- Description: Full text of customer complaint

Outputs:
- Name: Summary
- Type: Text
- Description: Concise summary of complaint
```

**4. Set Model Parameters**
```
Temperature: 0.7 (balance creativity/consistency)
Max Tokens: 150 (limit response length)
Top P: 0.9 (nucleus sampling)
Stop Sequences: ["\n\n"] (stop at double newline)
```

**5. Test and Refine**
```
Test with:
- Typical inputs
- Edge cases
- Unexpected inputs
- Various lengths

Refine based on:
- Output quality
- Consistency
- Accuracy
- Cost/performance
```

## Using Prompt Actions in Topics

### Integration Pattern

**Topic Flow**:
```
1. Collect user input
2. Store in variable
3. Call prompt action
4. Use generated output
5. Display or process result
```

**Example Topic: Email Draft Assistance**
```
Topic: Draft Response Email

Conversation:
Agent: "I'll help you draft a response. What's the customer's concern?"
User: "They want a refund for late delivery"

Node: Store Input
Set variable: CustomerConcern = "refund for late delivery"

Node: Call Prompt Action
Action: DraftResponseEmail
Input: CustomerConcern, CustomerName, OrderNumber
Output → EmailDraft

Node: Present Draft
Agent: "Here's a draft email:
{EmailDraft}

Would you like me to send this or make changes?"

Branch:
- Send → Send email action
- Changes → Collect feedback, regenerate
```

## Advanced Techniques

### Chain-of-Thought Prompting
```
Prompt:
"Let's approach this step-by-step:
1. Identify the main issue from this customer message
2. Determine the appropriate department to handle it
3. Suggest the next best action
4. Provide reasoning for your suggestion

Customer Message: {Message}"

Benefits:
- More accurate results
- Explainable decisions
- Better complex reasoning
```

### Few-Shot Learning
```
Prompt:
"Classify customer sentiment as Positive, Neutral, or Negative.

Examples:
'Love this product!' → Positive
'It's okay, nothing special' → Neutral
'Worst purchase ever' → Negative

Now classify: {CustomerFeedback}"

Benefits:
- Improved accuracy
- Consistent formatting
- Better edge case handling
```

### Context Injection
```
Prompt:
"Using the following company policy:
{CompanyPolicy}

And this customer history:
{CustomerHistory}

Draft a personalized response to: {CustomerInquiry}"

Benefits:
- Grounded in facts
- Consistent with policy
- Personalized responses
```

## Best Practices

### Prompt Design
1. **Clear Instructions**: Be explicit about what you want
2. **Output Format**: Specify desired format
3. **Constraints**: Set boundaries and limitations
4. **Context**: Provide relevant background
5. **Examples**: Show desired outputs

### Performance
1. **Token Optimization**: Minimize unnecessary tokens
2. **Caching**: Reuse for identical inputs
3. **Batch Processing**: Group similar requests
4. **Right-Size Models**: Use appropriate model tier

### Quality Assurance
1. **Validation**: Check outputs against criteria
2. **Fallbacks**: Handle low-confidence responses
3. **Human Review**: Spot-check generated content
4. **Feedback Loops**: Learn from corrections

### Security
1. **Input Sanitization**: Clean user inputs
2. **Output Validation**: Check for sensitive data
3. **Prompt Injection Prevention**: Guard against manipulation
4. **Access Control**: Limit who can use actions

## Monitoring and Iteration

### Metrics to Track
- **Success Rate**: % of successful generations
- **Average Confidence**: Model confidence scores
- **Cost**: Token usage and costs
- **Latency**: Response time
- **User Satisfaction**: Ratings of generated content

### Continuous Improvement
```
Process:
1. Collect usage data
2. Analyze failures and low-quality outputs
3. Identify patterns
4. Refine prompts
5. A/B test variations
6. Deploy improvements
7. Monitor impact
```

## Example Library

### Customer Service
```
1. Draft Apology Email
2. Summarize Support Ticket
3. Generate FAQ Answers
4. Classify Urgency
5. Extract Customer Intent
```

### Sales
```
1. Personalize Outreach Message
2. Generate Meeting Summary
3. Draft Proposal Section
4. Qualify Lead Description
5. Suggest Next Best Action
```

### HR
```
1. Draft Job Description
2. Summarize Resume
3. Generate Interview Questions
4. Create Onboarding Checklist
5. Draft Performance Feedback
```

## Related Resources

- [Prompt actions in Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/)
- [Azure OpenAI best practices](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering)
- [Prompt engineering guide](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/advanced-prompt-engineering)
