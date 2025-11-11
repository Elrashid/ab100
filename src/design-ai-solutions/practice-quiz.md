# Practice Quiz: Design AI Solutions (40-45%)

## Instructions
- 35 questions covering the Design AI Solutions domain
- Multiple choice (single answer) and multiple select (multiple answers)
- Case study scenarios based on Microsoft certification format
- Answers and explanations provided at the end

---

## Case Study 1: Contoso Manufacturing

**Background:**
Contoso Manufacturing uses Dynamics 365 Supply Chain Management and wants to implement AI for predictive maintenance and demand forecasting. They have 50 manufacturing plants and 10,000 equipment units generating telemetry data.

**Requirements:**
- Predict equipment failures 48 hours in advance
- Forecast demand for 500 product SKUs
- Integrate with existing Dynamics 365
- Provide mobile access for technicians

---

### Question 1
You need to design the AI agent for predictive maintenance.

Which agent type should you recommend?

A. Prompt/response agent for conversational interface  
B. Task agent for scheduled predictions  
C. Autonomous agent with real-time monitoring and decision-making  
D. Code-first agent without AI

**Answer:** ||C||

---

### Question 2
The solution needs to process sensor data from equipment and trigger maintenance workflows.

Which THREE Azure AI services should you use? (Choose 3)

A. Azure OpenAI for natural language processing  
B. Azure Machine Learning for predictive models  
C. Azure IoT Hub for telemetry ingestion  
D. Azure AI Vision for image processing  
E. Azure Stream Analytics for real-time processing  
F. Azure Text Analytics

**Answer:** ||B, C, E||

---

## Case Study 2: Fabrikam Financial Services

**Background:**
Fabrikam is a financial services company using Dynamics 365 Customer Service. They want to implement an AI agent for customer inquiries that can:
- Answer product questions
- Check account balances
- Process simple transactions
- Escalate complex issues

**Compliance Requirements:**
- SOX compliance for financial data
- Audit all AI decisions
- Explainable AI required
- Data residency in US East region

---

### Question 3
You are designing the Copilot Studio agent for customer service.

Which TWO features should you enable for compliance? (Choose 2)

A. Conversation transcripts with audit logging  
B. Public web channel without authentication  
C. Generative AI with confidence score display  
D. Anonymous user access  
E. Response citations showing data sources

**Answer:** ||A, E||

---

### Question 4
The agent needs to check account balances from a secure banking system.

What is the BEST approach for integration?

A. Direct database connection  
B. Custom connector with OAuth 2.0 authentication  
C. Manual data entry  
D. Public API without authentication

**Answer:** ||B||

---

### Question 5
You need to design the agent behavior to ensure responsible AI.

Which THREE capabilities should you implement? (Choose 3)

A. Confidence thresholds for autonomous actions  
B. Human escalation for high-risk transactions  
C. Explainability for AI recommendations  
D. Unlimited autonomous transaction authority  
E. No logging to improve performance  
F. Bias testing and monitoring

**Answer:** ||A, B, C||

---

## General Questions

### Question 6
You are designing a solution that uses Azure OpenAI with custom business data in SharePoint and Dataverse.

Which pattern should you implement?

A. Fine-tune GPT-4 with all company data  
B. Retrieval-Augmented Generation (RAG)  
C. Prompt injection  
D. Manual data copying

**Answer:** ||B||

---

### Question 7
Your organization needs to customize Copilot for Dynamics 365 Sales to include industry-specific terminology.

What should you configure?

A. Retrain the base model  
B. Design custom business terms in Copilot settings  
C. Disable Copilot and build from scratch  
D. Use only default terminology

**Answer:** ||B||

---

### Question 8
You are designing a multi-agent solution with specialized agents for research, analysis, and reporting.

Which orchestration pattern is MOST appropriate?

A. No orchestration - agents work independently  
B. Centralized orchestrator coordinates agent sequence  
C. Random agent execution  
D. User manually triggers each agent

**Answer:** ||B||

---

### Question 9
You need to implement grounding data for a customer service agent. The data includes product manuals (PDF), CRM data (Dataverse), and knowledge articles (SharePoint).

Which THREE steps are required for data processing? (Choose 3)

A. Extract text from PDFs  
B. Delete all existing data  
C. Chunk documents into manageable segments  
D. Generate vector embeddings  
E. Disable all security  
F. Remove all metadata

**Answer:** ||A, C, D||

---

### Question 10
Your Copilot Studio agent needs to determine when to use Conversational Language Understanding (CLU) versus generative AI.

When should you use CLU?

A. For open-ended creative tasks  
B. For deterministic intent classification with known intents  
C. For all scenarios always  
D. Never, only use generative AI

**Answer:** ||B||

---

### Question 11
You are designing prompts for an autonomous agent that needs to perform multi-step reasoning.

Which prompt engineering technique should you use?

A. Zero-shot without examples  
B. Chain-of-thought (CoT) with step-by-step reasoning  
C. Minimal instructions  
D. No prompt structure

**Answer:** ||B||

---

### Question 12
You need to design a custom AI model in Azure AI Foundry for specialized document classification.

Which THREE components should you include? (Choose 3)

A. Model training pipeline  
B. Model registry for versioning  
C. No testing (trust the model)  
D. Deployment endpoints  
E. Ignore monitoring  
F. Manual deployments only

**Answer:** ||A, B, D||

---

### Question 13
Your organization uses Microsoft 365 and needs to extend Copilot with custom data from internal systems.

What should you create?

A. Completely new AI system  
B. Declarative agent or plugin for M365 Copilot  
C. Ignore M365 Copilot  
D. Manual processes only

**Answer:** ||B||

---

### Question 14
You are designing agent extensibility using Model Context Protocol (MCP).

What is the PRIMARY benefit of MCP?

A. Faster model training  
B. Standardized tool/resource exposure to LLMs  
C. Reduced costs  
D. Better UI design

**Answer:** ||B||

---

### Question 15
A retail company needs an AI agent that can interact with their legacy inventory system through the UI (no APIs available).

What should you implement?

A. Give up - no solution exists  
B. Agent with computer use (UI automation)  
C. Manual data entry  
D. Complete system replacement

**Answer:** ||B||

---

### Question 16
You are designing an agent for Dynamics 365 Field Service that can schedule technicians.

Which Microsoft agent should you leverage?

A. Build completely custom agent  
B. Copilot in Field Service with scheduling capabilities  
C. Generic chatbot  
D. No AI solution

**Answer:** ||B||

---

### Question 17
Your solution needs to orchestrate AI capabilities across Dynamics 365 Finance, Supply Chain, and Commerce.

What should be the foundation for data integration?

A. Manual data transfers  
B. Dataverse as unified data platform  
C. Separate databases with no integration  
D. Excel files

**Answer:** ||B||

---

### Question 18
You need to design row-level security for grounding data in a multi-tenant scenario.

Which approach should you use?

A. No security - all users see all data  
B. User context propagation with security trimming  
C. Single shared account  
D. Manual filtering by users

**Answer:** ||B||

---

### Question 19
You are designing a solution using Azure OpenAI that must comply with data residency requirements.

Which THREE considerations are important? (Choose 3)

A. Deploy Azure OpenAI in required region  
B. Configure data processing location  
C. Ignore compliance requirements  
D. Document data flows  
E. Allow data to go anywhere  
F. Store sensitive data on public internet

**Answer:** ||A, B, D||

---

### Question 20
Your Copilot Studio agent needs to call a Power Automate flow to update Dataverse records.

What should you configure?

A. No integration possible  
B. Connector action calling the flow  
C. Manual process  
D. Rebuild everything in code

**Answer:** ||B||

---

### Question 21
You need to apply the Power Platform Well-Architected Framework to your AI solution.

Which pillar addresses solution scalability and performance?

A. Security  
B. Cost Optimization  
C. Performance Efficiency  
D. Operational Excellence

**Answer:** ||C||

---

### Question 22
You are designing topics in Copilot Studio and need to handle situations where the agent doesn't understand the user.

What should you configure?

A. Delete the agent  
B. Fallback topic with generative answers  
C. Ignore confused users  
D. Close conversation immediately

**Answer:** ||B||

---

### Question 23
Your solution needs to provide voice interaction for a contact center agent.

Which Copilot Studio feature should you enable?

A. Text-only mode  
B. Voice mode with speech recognition and synthesis  
C. Disable all audio  
D. Manual phone calls only

**Answer:** ||B||

---

### Question 24
You are designing a solution that needs to explain AI decisions to business users.

Which feature should you implement?

A. Hide all AI logic  
B. Model interpretability with explanations  
C. No documentation  
D. Complex technical jargon only

**Answer:** ||B||

---

### Question 25
Your agent needs to process code from GitHub repositories and provide insights.

Which Microsoft agent capability should you use?

A. Manual code review  
B. Code-first generative pages with agent feeds  
C. No code processing  
D. Delete all code

**Answer:** ||B||

---

### Question 26
You need to design data access controls for an AI agent accessing sensitive customer data.

Which security model should you implement?

A. Everyone has full access  
B. Role-Based Access Control (RBAC) with least privilege  
C. No security  
D. Single shared password

**Answer:** ||B||

---

### Question 27
Your organization has multiple Dynamics 365 apps (Sales, Service, Marketing) and needs unified AI insights.

What should you design?

A. Separate AI for each app with no integration  
B. Multi-Dynamics 365 AI solution with shared intelligence  
C. No AI capabilities  
D. Manual reporting only

**Answer:** ||B||

---

### Question 28
You are designing an agent that needs to recommend products based on customer preferences.

Which AI capability should you implement?

A. Random selection  
B. AI Builder recommendation model  
C. Manual suggestions  
D. Always recommend the same product

**Answer:** ||B||

---

### Question 29
Your solution needs to detect and prevent prompt injection attacks.

Which THREE security measures should you implement? (Choose 3)

A. Input validation and sanitization  
B. No security (trust all users)  
C. System prompt protection  
D. Allow all inputs without checking  
E. Output filtering  
F. Disable all security features

**Answer:** ||A, C, E||

---

### Question 30
You need to design an autonomous agent that can reason about complex business scenarios.

What should you configure?

A. Simple rule-based logic  
B. Reasoning capabilities with LLM integration  
C. No reasoning capability  
D. Random decisions

**Answer:** ||B||

---

### Question 31
Your Copilot Studio agent needs to handle multiple conversation topics and maintain context.

What should you design?

A. Single topic for everything  
B. Multiple topics with context variables and topic redirection  
C. No topic structure  
D. Start new conversation for each question

**Answer:** ||B||

---

### Question 32
You are designing an AI solution for Dynamics 365 Finance that provides cash flow forecasting.

Which AI feature should you leverage?

A. Build custom model from scratch  
B. Built-in Finance Insights with cash flow forecasting  
C. Excel formulas  
D. Manual guessing

**Answer:** ||B||

---

### Question 33
Your solution needs to provide in-app help enriched with AI-generated guidance.

What should you implement?

A. No help system  
B. AI-powered in-app help with knowledge source integration  
C. Static help text only  
D. External help website

**Answer:** ||B||

---

### Question 34
You need to design prompt actions in Copilot Studio that can be reused across multiple topics.

What should you create?

A. Duplicate prompts in every topic  
B. Reusable prompt actions with parameters  
C. No reusability  
D. Hardcode everything

**Answer:** ||B||

---

### Question 35
Your organization needs to optimize AI agent performance in Microsoft 365 SharePoint sites.

Which THREE optimization techniques should you apply? (Choose 3)

A. Index relevant content  
B. Disable all search  
C. Configure metadata for better discovery  
D. Delete all documents  
E. Implement semantic search  
F. Remove all organization

**Answer:** ||A, C, E||

---

## Answer Key

| Question | Answer | Topic |
|----------|--------|-------|
| 1 | C | Agent types |
| 2 | B, C, E | Azure AI services |
| 3 | A, E | Compliance and auditing |
| 4 | B | Custom connectors |
| 5 | A, B, C | Responsible AI |
| 6 | B | RAG pattern |
| 7 | B | Customize Copilot D365 |
| 8 | B | Multi-agent orchestration |
| 9 | A, C, D | Data processing |
| 10 | B | CLU vs generative AI |
| 11 | B | Prompt engineering |
| 12 | A, B, D | Azure AI Foundry |
| 13 | B | M365 Copilot extensibility |
| 14 | B | Model Context Protocol |
| 15 | B | Computer use |
| 16 | B | Field Service agents |
| 17 | B | Multi-app data integration |
| 18 | B | Row-level security |
| 19 | A, B, D | Data residency |
| 20 | B | Copilot Studio flows |
| 21 | C | Power Platform WAF |
| 22 | B | Fallback handling |
| 23 | B | Voice mode |
| 24 | B | AI explainability |
| 25 | B | Code processing |
| 26 | B | Access controls |
| 27 | B | Multi-D365 solution |
| 28 | B | AI Builder |
| 29 | A, C, E | Security measures |
| 30 | B | Autonomous reasoning |
| 31 | B | Topic design |
| 32 | B | Finance AI features |
| 33 | B | In-app help |
| 34 | B | Prompt actions |
| 35 | A, C, E | M365 optimization |

---

## Detailed Explanations

### Case Study 1 - Explanations

**Question 1:** Autonomous agents are ideal for predictive maintenance because they:
- Monitor data continuously
- Make decisions independently
- Trigger actions (maintenance workflows)
- Learn from outcomes
- Require minimal human intervention

**Question 2:** The combination of:
- **Azure Machine Learning:** Build and train predictive models
- **Azure IoT Hub:** Ingest telemetry from equipment
- **Stream Analytics:** Process streaming data in real-time

### Case Study 2 - Explanations

**Question 3:** For SOX compliance:
- **Audit logging:** Track all interactions and decisions
- **Response citations:** Show data sources for transparency and validation

**Question 4:** Custom connectors with OAuth 2.0 provide:
- Secure authentication
- Token-based access
- Standard protocol
- Audit trail

### General Explanations

**Question 6 - RAG Pattern:**
RAG (Retrieval-Augmented Generation) is the correct approach because:
- Grounds responses in current data
- No model retraining needed
- Supports dynamic data
- More cost-effective than fine-tuning
- Better for frequently changing information

**Question 9 - Data Processing:**
The RAG pipeline requires:
1. **Text extraction:** Get content from various formats
2. **Chunking:** Break into segments (e.g., 500-1000 tokens)
3. **Embeddings:** Convert to vectors for semantic search

**Question 14 - MCP Benefits:**
Model Context Protocol provides:
- Standardized interface for tools
- Discoverable capabilities
- Consistent authentication
- Cross-platform compatibility

---

## Study Tips

1. **Understand Agent Types:**
   - Task: Single-purpose, deterministic
   - Autonomous: Self-directed, reasoning
   - Prompt/response: Conversational

2. **Security Patterns:**
   - Always propagate user context
   - Implement least privilege
   - Use OAuth 2.0 for APIs
   - Enable audit logging

3. **Data Processing:**
   - RAG for dynamic data
   - Chunking strategies
   - Vector embeddings
   - Semantic search

4. **Copilot Studio:**
   - Topics and entities
   - Fallback handling
   - Authentication
   - Connector actions

5. **Azure AI:**
   - Service selection
   - Regional deployment
   - Model registry
   - Monitoring

6. **Responsible AI:**
   - Explainability
   - Fairness testing
   - Human oversight
   - Compliance

---

## Additional Practice Resources

- [Copilot Studio Learning Path](https://learn.microsoft.com/en-us/training/modules/implement-copilot-studio/)
- [Azure AI Services Labs](https://learn.microsoft.com/en-us/azure/ai-services/)
- [Practice Assessments](https://learn.microsoft.com/en-us/credentials/)
- [Microsoft AI Skills Challenge](https://www.microsoft.com/en-us/cloudskillschallenge)
