<div style="page-break-before: always;"></div>

# 2.1.10 Design Topics for Copilot Studio

## Overview

Topics are the building blocks of Copilot Studio agents, defining conversation flows, logic, and responses. Properly designed topics ensure effective user interactions.

## Topic Types

### System Topics
Pre-built topics that handle common scenarios:
- **Greeting**: Welcome users
- **Goodbye**: End conversations
- **Escalate**: Transfer to human
- **Start Over**: Reset conversation
- **Fallback**: Handle unrecognized input

### Custom Topics
User-defined topics for specific business needs:
- **Transactional**: Complete specific tasks
- **Informational**: Provide information
- **Navigational**: Guide users through processes

## Topic Structure

### Basic Components
```
Topic: Check Order Status
├─ Trigger Phrases
│  - "Where is my order"
│  - "Order status"
│  - "Track my order"
├─ Entities
│  - Order Number
│  - Email Address
├─ Dialog Nodes
│  - Collect order number
│  - Validate order
│  - Display status
│  - Offer additional help
└─ End Conversation
```

### Node Types
- **Message**: Display information
- **Question**: Collect user input
- **Condition**: Branching logic
- **Action**: Call external services
- **Variable Management**: Set/get variables
- **Topic Redirect**: Call another topic

## Fallback Design

### Fallback Topic Purpose
Handle scenarios when the agent doesn't understand user intent or lacks information.

### Fallback Strategy
```
Level 1: Clarification
"I'm not sure I understood. Could you rephrase that?"

Level 2: Suggestion
"I can help you with:
- Check order status
- Return an item
- Contact support
Which would you like help with?"

Level 3: Escalation
"I'd like to connect you with a team member who can better assist you."
```

### Implementation
```
Fallback Topic:
1. Acknowledge didn't understand
2. Check attempt count
   - First attempt: Ask for clarification
   - Second attempt: Offer menu of options
   - Third+ attempt: Escalate to human
3. Track fallback reasons for improvement
```

## Best Practices

### Topic Design
1. **Single Purpose**: One topic = one task
2. **Clear Triggers**: Comprehensive trigger phrases
3. **Conversational Flow**: Natural dialogue
4. **Error Handling**: Plan for unexpected inputs
5. **Context Awareness**: Use variables
6. **Reusability**: Create modular topics

### Trigger Phrases
```
Good Examples (Varied):
- "I want to return an item"
- "Start a return"
- "Return something I bought"
- "How do I send something back"

Poor Examples (Too Similar):
- "Return item"
- "Return product"
- "Return purchase"
```

### Conversation Flow
```
Good Flow:
Agent: "I can help with your return. What's your order number?"
User: "12345"
Agent: "Thanks! I found your order. Which item would you like to return?"
[Show list of items]

Poor Flow:
Agent: "Order number?"
User: "12345"
Agent: "Item ID?"
[Too abrupt, not conversational]
```

## Advanced Techniques

### Generative Answers Integration
```
Hybrid Approach:
- Use topics for structured workflows
- Use generative answers for open-ended questions
- Fallback to generative when topic confidence low
```

### Entity Extraction
```
User: "I want to return the blue widget from order 12345"

Extracted Entities:
- action: return
- product: blue widget
- order_number: 12345

Agent uses entities to streamline conversation
```

### Context Variables
```
Global Variables:
- user_name
- user_email
- account_id

Topic Variables:
- selected_product
- order_total
- return_reason

Use throughout conversation for personalization
```

## Testing Topics

### Test Scenarios
- Happy path (expected flow)
- Variations (different phrasing)
- Interruptions (topic switching)
- Invalid input
- Edge cases

### Track Analytics
- Topic trigger frequency
- Completion rate
- Abandonment points
- Escalation rate
- User satisfaction

## Related Resources

- [Copilot Studio topics](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-create-edit-topics)
- [Fallback topic](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-system-fallback-topic)
- [Entities](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-entities-slot-filling)
