<div style="page-break-before: always;"></div>

# 2.1.7 Design Prompt and Response Agents

## Overview

Prompt and response agents are conversational AI systems optimized for understanding user prompts and generating appropriate responses. They form the foundation of chatbots, virtual assistants, and conversational interfaces.

## Core Design Principles

### Natural Conversation Flow
- Understand user intent
- Maintain context across turns
- Provide relevant, helpful responses
- Handle ambiguity gracefully
- Support multi-turn dialogues

### Response Quality
- Accurate and factual
- Concise yet complete
- Appropriate tone
- Contextually relevant
- Actionable when needed

## Architecture Patterns

### Basic Pattern
```
[User Prompt] → [Intent Recognition] → [Entity Extraction] → [Response Generation] → [User Response]
```

### Advanced Pattern with Context
```
[User Prompt]
     ↓
[Context Management] ← [Conversation History]
     ↓
[Intent & Entity Recognition]
     ↓
[Knowledge Retrieval] ← [Knowledge Sources]
     ↓
[Response Generation] ← [Prompt Templates]
     ↓
[Post-Processing]
     ↓
[User Response]
```

## Response Generation Strategies

### Template-Based Responses
```
Intent: check_order_status
Template: "Your order #{order_number} is {status}.
          Expected delivery: {delivery_date}."
Variables: Populated from system data
```

### Generative AI Responses
```
Approach: Use LLM with grounding data
Benefits:
- Natural, varied responses
- Handle unexpected questions
- Contextually aware
- No template maintenance

Challenges:
- Potential hallucinations
- Response consistency
- Cost considerations
```

### Hybrid Approach
```
Decision Tree:
├─ Known scenario → Template response (fast, consistent)
├─ Unknown but in knowledge base → Generative with grounding
└─ Unknown → Generative with disclaimer or escalation
```

## Prompt Engineering for Agents

### System Prompt Design

**Role Definition**:
```
You are a professional customer service agent for [Company Name].
You help customers with orders, returns, and product questions.
You are friendly, professional, and solution-oriented.
```

**Behavioral Guidelines**:
```
Always:
- Greet customers warmly
- Ask clarifying questions when needed
- Provide specific, actionable information
- Offer to escalate for complex issues
- Thank customers for their patience

Never:
- Make promises beyond your authority
- Provide medical, legal, or financial advice
- Share confidential information
- Use informal or unprofessional language
```

**Response Format**:
```
Format your responses as follows:
1. Acknowledge the customer's request
2. Provide the requested information or solution
3. Offer additional help if relevant
4. Close professionally

Keep responses under 150 words unless detailed explanation needed.
```

### User Prompt Handling

**Intent Clarification**:
```
Ambiguous Prompt: "It's not working"

Agent Response:
"I'd be happy to help! To assist you better, could you let me know:
1. Which product or service isn't working?
2. What happens when you try to use it?
3. When did this issue start?"
```

**Context Incorporation**:
```
Turn 1:
User: "I want to return something"
Agent: "I can help with that. What would you like to return?"

Turn 2:
User: "The blue one"
Agent: [Uses context - knows customer has order #12345 with blue item]
"I see you have the Blue Widget from order #12345.
Would you like to start a return for this item?"
```

## Context Management

### Session Context
```json
{
  "session_id": "abc123",
  "user_id": "user456",
  "conversation_history": [
    {"role": "user", "content": "I need help with my order"},
    {"role": "agent", "content": "I'd be happy to help..."}
  ],
  "extracted_entities": {
    "order_number": "12345",
    "issue_type": "delivery_delay"
  },
  "user_sentiment": "neutral",
  "last_interaction": "2024-01-15T10:30:00Z"
}
```

### Long-Term Memory
```
Customer Profile:
- Previous interactions
- Preferences
- Purchase history
- Communication style
- Resolution history
```

## Response Quality Optimization

### Confidence Scoring
```
Response Generation:
1. Generate response
2. Assess confidence (0-1)
3. Decision:
   - Confidence > 0.8: Return response
   - Confidence 0.5-0.8: Add disclaimer
   - Confidence < 0.5: Escalate or ask for clarification
```

### Response Validation
```
Checks Before Sending:
✓ Factually accurate (grounded in knowledge)
✓ Appropriate tone
✓ Answers the question
✓ No sensitive information leaked
✓ Policy compliant
✓ Actionable next steps provided
```

### A/B Testing
```
Test Variations:
- Response length (concise vs. detailed)
- Tone (formal vs. friendly)
- Structure (bullets vs. paragraphs)
- Call-to-action placement

Measure:
- User satisfaction
- Task completion
- Follow-up questions
- Escalation rate
```

## Handling Special Scenarios

### Escalation
```
Trigger Conditions:
- User explicitly requests human
- Multiple failed resolution attempts
- High-stakes situation
- Negative sentiment threshold exceeded
- Agent confidence too low

Escalation Process:
1. Acknowledge escalation
2. Summarize conversation for human agent
3. Set expectations (wait time)
4. Seamless handoff with context
```

### Multi-Intent Prompts
```
Prompt: "I want to check my order status and also update my address"

Agent Approach:
1. Identify both intents
2. Prioritize or sequence
3. Address each:
   "I can help you with both! Let me first check your order status,
    then we'll update your address."
4. Handle each intent
5. Confirm both complete
```

### Handling Errors
```
Scenarios:
- Didn't understand: "I'm not sure I understood. Could you rephrase?"
- Missing information: "I need your order number to help with this."
- System error: "I'm having trouble accessing that information.
                 Let me connect you with someone who can help."
```

## Implementation Patterns

### Copilot Studio Implementation

**Topic Structure**:
```
Topic: Product Inquiry
Trigger Phrases:
- "Tell me about [product]"
- "Product information"
- "What is [product]"

Nodes:
1. Identify product (entity extraction)
2. Retrieve product information (data call)
3. Generate response (generative answer or template)
4. Offer related help
5. End conversation or continue
```

**Generative Answers**:
```
Configuration:
- Enable generative answers
- Add knowledge sources (SharePoint, websites)
- Set content moderation
- Configure response length
- Add boosted topics for priority scenarios
```

### Azure OpenAI Implementation

**Function Calling**:
```python
# Conceptual example
functions = [
    {
        "name": "get_order_status",
        "description": "Retrieve order status by order number",
        "parameters": {
            "order_number": {"type": "string"}
        }
    }
]

response = openai.ChatCompletion.create(
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ],
    functions=functions,
    function_call="auto"
)
```

## Monitoring and Improvement

### Key Metrics
- **Resolution Rate**: % of issues resolved without escalation
- **User Satisfaction**: CSAT, thumbs up/down
- **Response Time**: Average time to respond
- **Accuracy**: Correct responses vs. total
- **Engagement**: Conversation length, completion rate

### Continuous Improvement
```
Improvement Loop:
1. Collect conversation logs
2. Analyze failures and successes
3. Identify patterns
4. Update:
   - Prompts
   - Knowledge base
   - Response templates
   - Intent models
5. A/B test changes
6. Deploy improvements
7. Monitor impact
```

### Common Issues and Fixes

| Issue | Symptom | Fix |
|-------|---------|-----|
| Hallucinations | Incorrect information | Add grounding, lower temperature |
| Repetitive responses | Same phrasing | Increase temperature, vary templates |
| Off-topic | Irrelevant responses | Improve system prompt, add guardrails |
| Too verbose | Long-winded | Adjust prompt, set length limits |
| Too terse | Insufficient detail | Prompt for completeness |

## Best Practices

1. **Clear System Prompts**: Define role and behavior explicitly
2. **Ground in Knowledge**: Use retrieval-augmented generation
3. **Validate Responses**: Check before sending
4. **Maintain Context**: Track conversation state
5. **Handle Gracefully**: Errors, ambiguity, escalations
6. **Monitor Quality**: Continuous measurement
7. **Iterate Rapidly**: Frequent improvements
8. **User-Centric**: Design for user needs
9. **Transparent**: Acknowledge limitations
10. **Secure**: Protect sensitive information

## Testing Strategy

### Test Scenarios
```
Categories:
- Happy path (standard requests)
- Edge cases (unusual requests)
- Error conditions (invalid input)
- Multi-turn conversations
- Context switching
- Escalation triggers
- Performance under load
```

### Test Data
```
Create diverse test prompts:
- Different phrasings of same intent
- Typos and grammatical errors
- Ambiguous requests
- Multi-intent prompts
- Out-of-scope requests
- Offensive content (filtering test)
```

## Related Resources

- [Copilot Studio generative answers](https://learn.microsoft.com/en-us/microsoft-copilot-studio/nlu-boost-conversations)
- [Azure OpenAI prompt engineering](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering)
- [Conversational AI best practices](https://learn.microsoft.com/en-us/azure/architecture/guide/ai/conversational-ai-overview)
