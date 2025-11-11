# Practice Quiz: Deploy AI Solutions (30-35%)

## Instructions
- 25 questions covering the Deploy AI Solutions domain
- Multiple choice (single answer) and multiple select (multiple answers)
- Case study scenarios based on Microsoft certification format
- Answers and explanations provided at the end

---

## Case Study: Northwind Traders

**Background:**
Northwind Traders has deployed an AI agent for customer service using Copilot Studio integrated with Dynamics 365 Customer Service. The agent handles 1,000+ queries daily across email, web chat, and Microsoft Teams.

**Current Issues:**
- Response times degraded from 2s to 8s
- Confidence scores dropped from 0.85 to 0.65
- 15% of queries result in errors
- Users complain about irrelevant answers

**Requirements:**
- Improve performance and accuracy
- Implement comprehensive monitoring
- Ensure compliance (SOX, GDPR)
- Establish ALM process

---

### Question 1
You need to implement monitoring to identify the performance degradation root cause.

Which THREE metrics should you track? (Choose 3)

A. Response latency by query type  
B. Office temperature  
C. Confidence score distribution  
D. Cafeteria menu  
E. Error rates and types  
F. Employee parking spaces

**Answer:** ||A, C, E||

---

### Question 2
The agent's confidence scores have dropped significantly.

What should you do FIRST to diagnose the issue?

A. Delete the agent and start over  
B. Analyze telemetry data to identify patterns in low-confidence queries  
C. Ignore the issue  
D. Disable monitoring

**Answer:** ||B||

---

### Question 3
You need to implement an ALM process for deploying agent updates.

Which THREE environments should you establish? (Choose 3)

A. Development  
B. Personal laptops  
C. Test/UAT  
D. Random servers  
E. Production  
F. Break room computers

**Answer:** ||A, C, E||

---

## Case Study: Contoso Healthcare

**Background:**
Contoso Healthcare is deploying an AI solution for patient triage using custom Azure OpenAI models. The solution must comply with HIPAA and maintain detailed audit logs.

**Requirements:**
- HIPAA compliance
- Audit all AI interactions
- Model updates without downtime
- Data residency in US regions only

---

### Question 4
You need to ensure HIPAA compliance for the AI solution.

Which THREE measures are required? (Choose 3)

A. Encryption of PHI at rest and in transit  
B. Public internet access to all data  
C. Business Associate Agreement with Microsoft  
D. No access controls  
E. Audit logging of all PHI access  
F. Allow any user to access any data

**Answer:** ||A, C, E||

---

### Question 5
You must implement audit logging that captures all AI interactions with patient data.

What should you log?

A. Nothing - auditing slows performance  
B. User ID, query, response, timestamp, and confidence score  
C. Only errors  
D. Random sample of 10% of queries

**Answer:** ||B||

---

### Question 6
The solution requires zero-downtime deployment for model updates.

Which deployment strategy should you use?

A. Take system offline for 2 hours  
B. Blue-green deployment with traffic switching  
C. Delete production and redeploy  
D. No deployment strategy

**Answer:** ||B||

---

## General Questions

### Question 7
You are implementing Application Insights for an AI agent.

Which custom metric is MOST important for monitoring AI quality?

A. Server CPU usage  
B. AI confidence scores  
C. Network bandwidth  
D. Disk space

**Answer:** ||B||

---

### Question 8
Your team needs to analyze user feedback to improve the agent.

What is the BEST approach?

A. Ignore all feedback  
B. Categorize feedback, identify patterns, and prioritize improvements using RICE framework  
C. Random changes  
D. Delete negative feedback

**Answer:** ||B||

---

### Question 9
You need to create validation criteria for an AI model before production deployment.

Which THREE factors should you validate? (Choose 3)

A. Model accuracy meets threshold (e.g., >90%)  
B. Model file size is exactly 1GB  
C. Fairness across demographic groups  
D. Server room is painted blue  
E. Robustness to adversarial inputs  
F. Developer's favorite color

**Answer:** ||A, C, E||

---

### Question 10
You are testing prompts for a customer service agent.

Which THREE best practices should you follow? (Choose 3)

A. Clear, specific instructions  
B. Vague, ambiguous wording  
C. Examples of desired outputs  
D. No structure or format  
E. Explicit output format specification  
F. Random punctuation

**Answer:** ||A, C, E||

---

### Question 11
You need to design end-to-end test scenarios for a multi-app AI solution spanning Sales and Service.

What should you test?

A. Only individual components in isolation  
B. Complete business process flow across both apps  
C. Nothing - assume it works  
D. Only the UI

**Answer:** ||B||

---

### Question 12
Your organization wants to use Copilot to generate test cases.

What is the BEST use of AI for testing?

A. Replace all manual testing immediately  
B. Generate diverse test scenarios and edge cases to augment manual testing  
C. No AI in testing  
D. Only test happy path

**Answer:** ||B||

---

### Question 13
You need to design the ALM process for custom AI models in Azure ML.

Which THREE components are essential? (Choose 3)

A. Model registry with versioning  
B. No version control  
C. CI/CD pipelines for training and deployment  
D. Manual deployments only  
E. Monitoring for data drift  
F. Random model updates

**Answer:** ||A, C, E||

---

### Question 14
Your Copilot Studio solution needs ALM across Dev, Test, and Prod environments.

What should you use?

A. Manual exports and imports  
B. Power Platform solutions with automated pipelines  
C. No environment separation  
D. Random deployments

**Answer:** ||B||

---

### Question 15
You are implementing ALM for data used in AI training.

Which tool is designed for data version control?

A. Microsoft Word  
B. DVC (Data Version Control)  
C. Paint  
D. Calculator

**Answer:** ||B||

---

### Question 16
You need to implement security for AI agents to prevent prompt injection.

Which THREE measures should you implement? (Choose 3)

A. Input validation and sanitization  
B. Accept all inputs without checking  
C. System prompt protection  
D. Disable all security  
E. Output filtering  
F. Trust all users completely

**Answer:** ||A, C, E||

---

### Question 17
Your organization must implement governance for AI agents.

What should the governance framework include?

A. Only technical specs  
B. Policies, approval processes, risk management, and compliance monitoring  
C. No governance  
D. Random rules

**Answer:** ||B||

---

### Question 18
You need to validate data residency compliance for an AI solution.

What should you verify?

A. Nothing - assume compliance  
B. Azure resources in correct regions, data processing location, no cross-border transfers  
C. Any region is fine  
D. Ignore regulations

**Answer:** ||B||

---

### Question 19
You are implementing row-level security for AI agent grounding data.

What is the MOST important principle?

A. Everyone sees everything  
B. Propagate user context and filter data based on permissions  
C. No security needed  
D. Single shared account

**Answer:** ||B||

---

### Question 20
You need to design audit trails that meet SOX compliance.

What is the minimum retention period for audit logs?

A. 1 day  
B. 1 month  
C. 7 years  
D. Delete immediately

**Answer:** ||C||

---

### Question 21
Your AI model's accuracy has degraded from 95% to 78% over 3 months.

What is the MOST likely cause?

A. The model is tired  
B. Data drift - input data distribution has changed  
C. Random variation  
D. Full moon

**Answer:** ||B||

---

### Question 22
You need to monitor agent performance post-deployment.

Which KQL query identifies queries with low confidence scores?

A. `requests | count`  
B. `customMetrics | where name == "agent.confidence" and value < 0.7`  
C. `delete *`  
D. `show tables`

**Answer:** ||B||

---

### Question 23
You are implementing responsible AI principles.

Which THREE should you prioritize? (Choose 3)

A. Fairness across demographic groups  
B. Maximizing profit only  
C. Transparency and explainability  
D. Hiding all information  
E. Accountability with human oversight  
F. No ethical considerations

**Answer:** ||A, C, E||

---

### Question 24
You need to test for bias in an AI model used for loan approval.

What should you measure?

A. Nothing  
B. Approval rates across demographic groups and disparate impact  
C. Only overall accuracy  
D. Random metrics

**Answer:** ||B||

---

### Question 25
Your organization needs to implement a rollback strategy for AI deployments.

What should you maintain?

A. Nothing - no rollback needed  
B. Previous model version, documented rollback steps, and automated rollback capability  
C. Delete everything after deployment  
D. Hope for the best

**Answer:** ||B||

---

## Answer Key

| Question | Answer | Topic |
|----------|--------|-------|
| 1 | A, C, E | Monitoring metrics |
| 2 | B | Telemetry analysis |
| 3 | A, C, E | ALM environments |
| 4 | A, C, E | HIPAA compliance |
| 5 | B | Audit logging |
| 6 | B | Zero-downtime deployment |
| 7 | B | Monitoring AI quality |
| 8 | B | User feedback analysis |
| 9 | A, C, E | Model validation |
| 10 | A, C, E | Prompt testing |
| 11 | B | End-to-end testing |
| 12 | B | AI for testing |
| 13 | A, C, E | MLOps ALM |
| 14 | B | Power Platform ALM |
| 15 | B | Data version control |
| 16 | A, C, E | Agent security |
| 17 | B | Governance framework |
| 18 | B | Data residency |
| 19 | B | Row-level security |
| 20 | C | SOX retention |
| 21 | B | Data drift |
| 22 | B | KQL monitoring |
| 23 | A, C, E | Responsible AI |
| 24 | B | Bias testing |
| 25 | B | Rollback strategy |

---

## Detailed Explanations

### Case Study 1 - Explanations

**Question 1:** Essential monitoring metrics:
- **Response latency:** Identify performance bottlenecks
- **Confidence scores:** Track AI quality
- **Error rates:** Find failure patterns

**Question 2:** Telemetry analysis should be first because:
- Provides data-driven insights
- Identifies patterns and trends
- Guides remediation efforts
- Avoids guesswork

**Question 3:** Standard ALM environments:
- **Development:** Build and test changes
- **Test/UAT:** User validation
- **Production:** Live system

### Case Study 2 - Explanations

**Question 4:** HIPAA requirements:
- **Encryption:** Protect PHI at rest and in transit
- **BAA:** Legal requirement with cloud provider
- **Audit logging:** Track all PHI access

**Question 6:** Blue-green deployment:
- Deploy to "green" environment
- Test thoroughly
- Switch traffic from "blue" to "green"
- Keep "blue" for quick rollback

### General Explanations

**Question 7 - Confidence Scores:**
Confidence scores directly indicate AI quality:
- Low confidence → potential wrong answers
- Trending down → model degradation
- Varies by query type → training gaps

**Question 13 - MLOps Components:**
Essential for production ML:
- **Model registry:** Track versions, lineage
- **CI/CD:** Automate training, testing, deployment
- **Drift monitoring:** Detect when retraining needed

**Question 19 - Row-Level Security:**
Critical for multi-user AI systems:
- Pass user identity to data layer
- Apply same permissions as direct access
- Filter results before AI processing
- Audit who accessed what

**Question 21 - Data Drift:**
Model accuracy degradation often caused by:
- Input data distribution changes
- New patterns not in training data
- Concept drift (relationships change)
- Solution: Retrain model with recent data

---

## Study Tips

1. **Monitoring:**
   - Know key metrics: latency, confidence, errors
   - Understand Application Insights/Azure Monitor
   - KQL query basics

2. **ALM:**
   - Dev → Test → Prod flow
   - CI/CD pipelines
   - Blue-green deployment
   - Infrastructure as Code

3. **Testing:**
   - Model validation criteria
   - End-to-end scenarios
   - Performance testing
   - Bias testing

4. **Security:**
   - Prompt injection prevention
   - Data access controls
   - Audit logging
   - Compliance (HIPAA, SOX, GDPR)

5. **Responsible AI:**
   - Fairness testing
   - Explainability
   - Transparency
   - Accountability

6. **Data Management:**
   - Data versioning
   - Drift detection
   - Quality validation
   - Lineage tracking

---

## Common Exam Scenarios

### Scenario 1: Performance Issues
- **Symptoms:** Slow response, timeouts
- **Diagnosis:** Check telemetry, identify bottleneck
- **Solution:** Optimize, scale, or improve prompts

### Scenario 2: Accuracy Degradation
- **Symptoms:** Lower confidence, wrong answers
- **Diagnosis:** Data drift, model staleness
- **Solution:** Retrain model, update knowledge

### Scenario 3: Compliance Requirements
- **Requirements:** HIPAA, SOX, GDPR
- **Implementation:** Encryption, audit, access controls
- **Validation:** Regular compliance checks

### Scenario 4: Deployment Failures
- **Problem:** Production issues after deployment
- **Prevention:** Comprehensive testing, staged rollout
- **Recovery:** Quick rollback capability

---

## Additional Practice Resources

- [Azure Monitor Labs](https://learn.microsoft.com/en-us/azure/azure-monitor/)
- [Azure DevOps Pipelines](https://learn.microsoft.com/en-us/training/paths/az-400-work-azure-repos-version-control/)
- [Responsible AI Toolbox](https://responsibleaitoolbox.ai/)
- [MLOps on Azure](https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment)
- [Power Platform ALM](https://learn.microsoft.com/en-us/power-platform/alm/)
