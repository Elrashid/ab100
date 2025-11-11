# Design AI Solutions Using Custom Models in Azure AI Foundry

## Overview

Azure AI Foundry (formerly Azure AI Studio) provides a comprehensive platform for designing, building, deploying, and managing custom AI models and solutions.

## When to Use Azure AI Foundry

### Ideal Scenarios
✅ Need custom AI models for specific domains
✅ Require fine-tuning of foundation models
✅ Complex multi-model orchestration
✅ Advanced prompt engineering workflows
✅ Custom evaluation and testing
✅ Full MLOps lifecycle management

### Not Ideal For
❌ Simple chatbot with standard Q&A (use Copilot Studio)
❌ Basic document processing (use AI Builder)
❌ Out-of-box scenarios (use pre-built services)

## Key Capabilities

### 1. Model Catalog
**Access to Models**:
- **Azure OpenAI**: GPT-4, GPT-3.5, embeddings
- **Open Source Models**: Llama, Mistral, Phi
- **Microsoft Models**: Phi-3 family
- **Partner Models**: Cohere, Meta, etc.

**Model Selection Criteria**:
```
Consider:
- Task type (generation, embedding, classification)
- Performance requirements
- Cost constraints
- Latency requirements
- Licensing terms
```

### 2. Prompt Flow

**Visual Workflow Designer**:
```
Components:
- LLM nodes (model calls)
- Python nodes (custom code)
- Prompt templates
- Data connectors
- Evaluation nodes
```

**Example Flow**:
```
[User Query]
    ↓
[Embedding Node] → Generate query embedding
    ↓
[Vector Search] → Find relevant documents
    ↓
[Context Preparation] → Format retrieved docs
    ↓
[LLM Node] → Generate response with context
    ↓
[Post-Processing] → Format and validate
    ↓
[Response]
```

### 3. Fine-Tuning

**Supported Models**:
- GPT-3.5-turbo
- GPT-4
- Select open-source models

**Process**:
```
1. Prepare Training Data
   Format: JSONL with prompt/completion pairs
   Size: Minimum 50-100 examples (more is better)

2. Upload Data
   - Validate format
   - Review samples

3. Configure Training
   - Select base model
   - Set hyperparameters (learning rate, epochs)
   - Validation split

4. Train Model
   - Monitor progress
   - Review metrics

5. Deploy
   - Create deployment
   - Test performance
   - Monitor usage

6. Evaluate
   - Compare to base model
   - Validate on test set
   - Iterate if needed
```

**Training Data Example**:
```json
{"prompt": "Classify this support ticket: Customer can't log in", "completion": "Technical Issue"}
{"prompt": "Classify this support ticket: When is my refund coming?", "completion": "Billing Question"}
{"prompt": "Classify this support ticket: Can you add feature X?", "completion": "Feature Request"}
```

### 4. Evaluation

**Built-in Evaluations**:
- **Groundedness**: Is response based on provided context?
- **Relevance**: Does response address the query?
- **Coherence**: Is response well-structured?
- **Fluency**: Is response grammatically correct?
- **Similarity**: Comparison to reference answers

**Custom Evaluations**:
```python
# Conceptual example
def custom_evaluation(response, expected):
    # Business-specific validation
    has_required_fields = check_fields(response)
    follows_policy = validate_policy(response)
    accuracy = calculate_accuracy(response, expected)

    return {
        "score": accuracy,
        "has_required_fields": has_required_fields,
        "policy_compliant": follows_policy
    }
```

### 5. Deployment

**Deployment Options**:
- **Managed Online Endpoint**: Serverless, auto-scaling
- **Real-time Endpoint**: Dedicated compute
- **Batch Endpoint**: Async batch processing

**Configuration**:
```yaml
deployment:
  name: customer-service-model
  model: gpt-4-fine-tuned
  instance_type: Standard_DS3_v2
  instance_count: 2
  scale_settings:
    min_instances: 1
    max_instances: 5
    target_utilization: 70
```

## Design Patterns

### Pattern 1: RAG (Retrieval-Augmented Generation)

**Architecture**:
```
[Query] → [Embed] → [Vector Search] → [Retrieve Top K]
    ↓
[Combine Query + Retrieved Docs]
    ↓
[LLM Generate] → [Response]
```

**Implementation in Prompt Flow**:
```
Nodes:
1. Input: User query
2. Embedding: Convert query to vector
3. Vector Search: Find similar documents
4. Prompt Template: Inject retrieved docs
5. LLM: Generate grounded response
6. Output: Return to user
```

**Benefits**:
- Reduces hallucinations
- Up-to-date information
- Traceable sources
- Cost-effective vs. fine-tuning for knowledge

### Pattern 2: Multi-Model Orchestration

**Use Case**: Complex workflow using multiple models

**Example**:
```
Customer Support Flow:
1. Classification Model → Categorize inquiry
2. Sentiment Model → Assess urgency
3. If technical issue:
   - Specialized tech model → Generate solution
4. If billing:
   - Billing model → Handle billing query
5. Summary Model → Create case summary
```

### Pattern 3: Agent with Tools

**Concept**: LLM with access to external tools/APIs

**Implementation**:
```python
# Conceptual
tools = [
    {
        "name": "search_knowledge_base",
        "description": "Search company knowledge base",
        "parameters": {"query": "string"}
    },
    {
        "name": "create_ticket",
        "description": "Create support ticket",
        "parameters": {"title": "string", "description": "string"}
    }
]

# LLM decides which tool to use
response = llm.chat(
    messages=conversation,
    tools=tools,
    tool_choice="auto"
)

# Execute tool if requested
if response.tool_calls:
    tool_result = execute_tool(response.tool_calls[0])
    # Continue conversation with tool result
```

## Integration with Microsoft Ecosystem

### Power Platform
```
Integration:
- Custom connector to AI Foundry endpoint
- Use in Power Apps/Power Automate
- Dataverse for data storage
```

### Dynamics 365
```
Integration:
- Call AI Foundry models from plugins
- Real-time scoring in business processes
- Batch processing for analytics
```

### Microsoft 365
```
Integration:
- Copilot extensibility
- Teams bot integration
- SharePoint content processing
```

## Best Practices

### Model Development
1. **Start Simple**: Baseline with pre-trained models
2. **Iterative Improvement**: Incremental fine-tuning
3. **Version Control**: Track model versions
4. **Evaluation First**: Establish metrics before building
5. **Cost Awareness**: Monitor token usage

### Prompt Engineering
1. **Systematic Testing**: Test variations
2. **Version Prompts**: Track prompt versions
3. **Temperature Tuning**: Adjust for use case
4. **Context Management**: Optimize context length
5. **Output Validation**: Verify format and content

### Deployment
1. **Blue-Green Deployments**: Zero-downtime updates
2. **A/B Testing**: Compare model versions
3. **Monitoring**: Track performance metrics
4. **Scaling**: Auto-scale based on demand
5. **Fallbacks**: Graceful degradation

### Operations
1. **Monitoring**: Real-time performance tracking
2. **Logging**: Comprehensive request logging
3. **Alerts**: Proactive issue detection
4. **Cost Management**: Budget alerts and caps
5. **Security**: API key rotation, network security

## Example: Custom Customer Service Model

### Requirement
Build a model that understands company-specific products and policies

### Approach
```
Step 1: Base Model Selection
- Choose: GPT-4 (good generalist capabilities)

Step 2: Knowledge Grounding (RAG)
- Index: Product docs, policy documents, FAQs
- Vector Store: Azure AI Search
- Embedding Model: text-embedding-ada-002

Step 3: Fine-Tuning (Optional)
- Collect: 500 historical support conversations
- Format: Customer query → Agent response pairs
- Fine-tune: GPT-3.5-turbo for cost efficiency

Step 4: Prompt Flow
- Classify intent
- Retrieve relevant documents
- Generate response with GPT-4
- Validate against policies
- Return formatted response

Step 5: Evaluation
- Groundedness: 95% (responses use retrieved docs)
- Relevance: 92% (answers the question)
- Policy Compliance: 98% (follows guidelines)

Step 6: Deployment
- Deploy to managed endpoint
- Integrate with Dynamics 365 Customer Service
- Monitor and iterate
```

## Monitoring and Optimization

### Key Metrics
- **Request Latency**: p50, p95, p99
- **Token Usage**: Input/output tokens per request
- **Cost**: $ per request, daily spend
- **Error Rate**: % of failed requests
- **Model Accuracy**: Custom metrics

### Optimization Techniques
- **Caching**: Cache frequent queries
- **Batching**: Group similar requests
- **Prompt Compression**: Reduce token usage
- **Model Selection**: Right-size for task
- **Load Balancing**: Distribute across instances

## Related Resources

- [Azure AI Foundry documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/)
- [Prompt flow](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/prompt-flow)
- [Fine-tuning](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/fine-tuning)
- [Model catalog](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/model-catalog)
