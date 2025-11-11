<div style="page-break-before: always;"></div>

# 1.4 Hands-On Labs: Plan AI Solutions

## Lab 1: Assess Agent Use Cases

**Duration:** 30 minutes  
**Objective:** Evaluate and document potential agent use cases in your organization

### Prerequisites
- Access to Microsoft 365 or Power Platform trial
- Business process documentation
- Stakeholder availability

### Steps

1. **Identify Business Processes**
   - List 5-10 repetitive business processes
   - Document current time/effort required
   - Note pain points and inefficiencies

2. **Assess Agent Suitability**
   - For each process, evaluate:
     - Is it rule-based or requires reasoning?
     - Is data available and accessible?
     - What's the automation potential?
   - Use scoring matrix (1-5):
     - Frequency
     - Complexity
     - Data availability
     - Business impact

3. **Create Use Case Document**
   ```markdown
   ## Use Case: Customer Query Routing
   
   **Current State:**
   - Manual email triage
   - 2 hours/day
   - 15% misrouted
   
   **Proposed Agent:**
   - Autonomous routing agent
   - Email analysis + intent classification
   - Route to appropriate department
   
   **Expected Benefits:**
   - 90% automation rate
   - <1 second response time
   - 95% accuracy
   
   **Data Requirements:**
   - Historical email data
   - Department taxonomy
   - Routing rules
   ```

4. **Prioritize Use Cases**
   - Calculate ROI estimate
   - Assess technical feasibility
   - Consider change management impact
   - Select top 3 for pilot

### Expected Outcome
- Documented use case portfolio
- Prioritized implementation roadmap
- ROI projections

---

## Lab 2: Design Multi-Agent Solution Architecture

**Duration:** 45 minutes  
**Objective:** Design a multi-agent system for a business scenario

### Scenario
**Company:** Contoso Sales Corp  
**Problem:** Inefficient lead processing and opportunity management

### Steps

1. **Identify Required Agents**
   - Lead Qualification Agent
   - Research Agent (company info)
   - Scheduling Agent
   - Follow-up Agent

2. **Define Agent Capabilities**
   ```
   Agent: Lead Qualification
   Type: Autonomous
   Inputs: Lead form, website data
   Processing: Score using ML model
   Outputs: Qualified/Disqualified + score
   Actions: Create opportunity OR send nurture email
   
   Agent: Research Agent
   Type: Task agent
   Inputs: Company name
   Processing: Web search + API calls
   Outputs: Company profile
   Data Sources: LinkedIn, company website, news
   ```

3. **Design Orchestration**
   ```
   Lead Form Submitted
         ↓
   [Lead Qualification Agent]
         ↓
   Score > 70? → Yes → [Research Agent]
         ↓                    ↓
         No            [Create Rich Profile]
         ↓                    ↓
   [Nurture Campaign]  [Scheduling Agent]
                            ↓
                    [Book Sales Meeting]
                            ↓
                    [Follow-up Agent]
   ```

4. **Document Integration Points**
   - Dataverse (leads, opportunities)
   - Exchange (email, calendar)
   - External APIs (LinkedIn, ZoomInfo)
   - Azure OpenAI (reasoning)

5. **Create Architecture Diagram**
   - Use Visio or draw.io
   - Show agents, data flows, dependencies
   - Document security boundaries

### Expected Outcome
- Multi-agent architecture diagram
- Agent specification documents
- Integration requirements
- Data flow documentation

---

## Lab 3: Build a Prompt Library

**Duration:** 30 minutes  
**Objective:** Create a governed prompt library with templates

### Steps

1. **Set Up Repository**
   ```bash
   # Create folder structure
   mkdir prompt-library
   cd prompt-library
   mkdir -p templates/{sales,support,operations}
   mkdir -p versions
   touch README.md
   ```

2. **Create Prompt Template**
   ```markdown
   # Prompt: Opportunity Summarization
   
   **Version:** 1.0  
   **Category:** Sales  
   **Owner:** Sales Ops Team  
   **Last Updated:** 2025-11-11
   
   ## Prompt Template
   
   ```
   You are a sales assistant analyzing opportunity data.
   
   Opportunity Details:
   - Name: {{opportunity_name}}
   - Value: {{opportunity_value}}
   - Stage: {{opportunity_stage}}
   - Last Activity: {{last_activity}}
   - Engagement Score: {{engagement_score}}
   
   Task: Provide a concise summary (3-4 sentences) highlighting:
   1. Current status and momentum
   2. Key risk factors
   3. Recommended next actions
   
   Format: Professional, data-driven, actionable
   ```
   
   ## Variables
   - `opportunity_name`: String
   - `opportunity_value`: Currency
   - `opportunity_stage`: Enum
   - `last_activity`: Date
   - `engagement_score`: Integer (0-100)
   
   ## Usage Examples
   [Include 2-3 examples with expected outputs]
   
   ## Testing Criteria
   - Accuracy: >90%
   - Relevance: High
   - Length: 50-75 words
   
   ## Change Log
   - v1.0 (2025-11-11): Initial version
   ```

3. **Create Governance Document**
   ```markdown
   # Prompt Library Governance
   
   ## Review Process
   1. Create prompt in dev branch
   2. Test with sample data
   3. Submit PR with test results
   4. Peer review (2 approvers)
   5. Security review (if sensitive)
   6. Merge to main
   
   ## Versioning
   - Semantic versioning (major.minor.patch)
   - Major: Breaking changes
   - Minor: New functionality
   - Patch: Bug fixes
   
   ## Quality Standards
   - Clear instructions
   - Defined variables
   - Example outputs
   - Success criteria
   - Change log maintained
   ```

4. **Implement Version Control**
   ```bash
   git init
   git add .
   git commit -m "Initialize prompt library"
   git remote add origin [your-repo]
   git push -u origin main
   ```

5. **Create Testing Framework**
   - Define test cases
   - Expected outputs
   - Validation criteria
   - Automated testing (optional)

### Expected Outcome
- Structured prompt library
- Governance procedures
- Version-controlled repository
- Testing framework

---

## Lab 4: Implement Model Router

**Duration:** 45 minutes  
**Objective:** Build an intelligent model routing system

### Steps

1. **Set Up Azure Resources**
   ```bicep
   // Deploy multiple Azure OpenAI models
   resource gpt4 'Microsoft.CognitiveServices/accounts@2023-05-01' = {
     name: 'openai-gpt4'
     location: 'eastus'
     sku: { name: 'S0' }
     kind: 'OpenAI'
     properties: {
       customSubDomainName: 'contoso-gpt4'
     }
   }
   
   resource gpt35 'Microsoft.CognitiveServices/accounts@2023-05-01' = {
     name: 'openai-gpt35'
     location: 'eastus'
     sku: { name: 'S0' }
     kind: 'OpenAI'
   }
   ```

2. **Create Routing Logic**
   ```python
   class ModelRouter:
       def __init__(self):
           self.models = {
               'gpt-4': {'cost': 0.03, 'latency': 2.0, 'quality': 0.95},
               'gpt-3.5': {'cost': 0.002, 'latency': 0.5, 'quality': 0.85},
               'phi-3': {'cost': 0.0001, 'latency': 0.1, 'quality': 0.75}
           }
       
       def route(self, request):
           complexity = self.analyze_complexity(request)
           priority = request.get('priority', 'normal')
           
           if complexity > 0.8 or priority == 'high':
               return 'gpt-4'
           elif complexity > 0.5:
               return 'gpt-3.5'
           else:
               return 'phi-3'
       
       def analyze_complexity(self, request):
           prompt = request['prompt']
           
           # Factors indicating complexity
           factors = {
               'length': len(prompt) > 500,
               'reasoning': any(word in prompt.lower() 
                   for word in ['analyze', 'compare', 'evaluate']),
               'structured_output': 'json' in prompt.lower(),
               'multi_step': prompt.count('step') > 2
           }
           
           return sum(factors.values()) / len(factors)
   ```

3. **Implement with Azure Functions**
   ```python
   import azure.functions as func
   import logging
   
   def main(req: func.HttpRequest) -> func.HttpResponse:
       logging.info('Model router processing request')
       
       request_data = req.get_json()
       router = ModelRouter()
       
       # Route to appropriate model
       model = router.route(request_data)
       
       # Call selected model
       response = call_model(model, request_data['prompt'])
       
       return func.HttpResponse(
           json.dumps({
               'model_used': model,
               'response': response,
               'cost_estimate': router.models[model]['cost']
           }),
           mimetype="application/json"
       )
   ```

4. **Add Monitoring**
   ```python
   from opencensus.ext.azure import metrics_exporter
   
   exporter = metrics_exporter.new_metrics_exporter(
       connection_string='InstrumentationKey=...'
   )
   
   # Track metrics
   metrics = {
       'model_usage': {},
       'total_cost': 0,
       'avg_latency': {}
   }
   
   def track_request(model, latency, cost):
       metrics['model_usage'][model] = \
           metrics['model_usage'].get(model, 0) + 1
       metrics['total_cost'] += cost
       # Send to Application Insights
   ```

5. **Test Routing Logic**
   ```python
   # Test cases
   test_cases = [
       {'prompt': 'What is 2+2?', 'expected': 'phi-3'},
       {'prompt': 'Analyze the competitive landscape...', 
        'expected': 'gpt-4'},
       {'prompt': 'Summarize this document', 'expected': 'gpt-3.5'}
   ]
   
   for test in test_cases:
       result = router.route(test)
       assert result == test['expected']
   ```

### Expected Outcome
- Working model router
- Cost optimization achieved
- Monitoring dashboard
- Test coverage >80%

---

## Lab 5: Create ROI Analysis

**Duration:** 30 minutes  
**Objective:** Build a comprehensive ROI model for AI implementation

### Steps

1. **Gather Current State Metrics**
   ```
   Process: Invoice Processing
   
   Current Metrics:
   - Volume: 1,000 invoices/month
   - Processing time: 15 minutes/invoice
   - Error rate: 5%
   - Labor cost: $25/hour
   - FTE: 2 employees
   ```

2. **Define AI Solution**
   ```
   Proposed Solution: AI Document Intelligence Agent
   
   Capabilities:
   - OCR + entity extraction
   - Validation against PO
   - Exception routing
   - Automated approval (under $1,000)
   ```

3. **Calculate Costs**
   ```python
   # Implementation Costs
   costs = {
       'development': {
           'azure_ai_services': 5000,  # One-time setup
           'integration': 15000,
           'training': 5000,
           'change_management': 10000
       },
       'ongoing_monthly': {
           'azure_ai_services': 500,
           'storage': 100,
           'support': 1000,
           'maintenance': 500
       }
   }
   
   total_implementation = sum(costs['development'].values())
   monthly_operational = sum(costs['ongoing_monthly'].values())
   
   print(f"Implementation: ${total_implementation:,}")
   print(f"Monthly Operational: ${monthly_operational:,}")
   ```

4. **Calculate Benefits**
   ```python
   # Time Savings
   invoices_per_month = 1000
   current_time_per_invoice = 15  # minutes
   new_time_per_invoice = 2  # minutes (exceptions only)
   automation_rate = 0.85
   
   time_saved_monthly = (
       invoices_per_month * 
       automation_rate * 
       (current_time_per_invoice - new_time_per_invoice) / 60
   )
   
   hourly_rate = 25
   monthly_savings = time_saved_monthly * hourly_rate
   annual_savings = monthly_savings * 12
   
   # Error Reduction
   current_error_cost = invoices_per_month * 0.05 * 50  # $50/error
   new_error_cost = invoices_per_month * 0.01 * 50
   error_savings = (current_error_cost - new_error_cost) * 12
   
   total_annual_benefit = annual_savings + error_savings
   ```

5. **Create ROI Report**
   ```python
   # ROI Calculation
   first_year_benefit = total_annual_benefit
   first_year_cost = (
       total_implementation + 
       (monthly_operational * 12)
   )
   
   roi_year_1 = (
       (first_year_benefit - first_year_cost) / 
       first_year_cost * 100
   )
   
   payback_period = total_implementation / monthly_savings
   
   print(f"""
   ROI Analysis Summary
   ====================
   
   Implementation Cost: ${total_implementation:,}
   Annual Operational Cost: ${monthly_operational * 12:,}
   Annual Benefits: ${total_annual_benefit:,.0f}
   
   Year 1 ROI: {roi_year_1:.1f}%
   Payback Period: {payback_period:.1f} months
   
   3-Year Value:
   - Total Benefits: ${total_annual_benefit * 3:,.0f}
   - Total Costs: ${total_implementation + (monthly_operational * 36):,.0f}
   - Net Value: ${(total_annual_benefit * 3) - (total_implementation + (monthly_operational * 36)):,.0f}
   """)
   ```

### Expected Outcome
- Detailed ROI model
- Cost-benefit analysis
- Multi-year projections
- Executive summary

---

## Additional Resources

- [Azure AI Studio](https://ai.azure.com/)
- [Power Platform Labs](https://learn.microsoft.com/en-us/training/powerplatform/)
- [AI Builder Labs](https://learn.microsoft.com/en-us/training/modules/get-started-with-ai-builder/)
- [Copilot Studio Labs](https://learn.microsoft.com/en-us/training/modules/implement-copilot-studio/)
