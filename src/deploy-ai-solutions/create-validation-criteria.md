<div style="page-break-before: always;"></div>

# 3.2.2 Create Validation Criteria for Custom AI Models

## Overview

Validation criteria ensure custom AI models meet quality, performance, and business requirements before deployment.

## Validation Dimensions

### 1. Accuracy
**Metrics**:
- Overall accuracy
- Precision
- Recall
- F1 Score
- AUC-ROC (classification)
- RMSE, MAE (regression)

**Thresholds**:
```
Minimum Requirements:
- Accuracy: >85%
- Precision: >80%
- Recall: >80%
- F1 Score: >0.8

Ideal Targets:
- Accuracy: >95%
- Precision: >90%
- Recall: >90%
```

### 2. Fairness
**Metrics**:
- Demographic parity
- Equal opportunity
- Predictive parity
- Disparate impact ratio

**Validation**:
```
Test across groups:
- Gender
- Age
- Geography
- Other protected attributes

Requirement: <10% difference in accuracy across groups
```

### 3. Robustness
**Tests**:
- Input variations
- Missing data
- Adversarial examples
- Out-of-distribution data

**Criteria**:
```
- Graceful degradation with poor input
- Error rate <2% on edge cases
- Confidence calibration accurate
- No catastrophic failures
```

### 4. Performance
**Metrics**:
- Inference latency
- Throughput
- Resource utilization
- Cost per prediction

**Targets**:
```
- Latency: <200ms (p95)
- Throughput: >100 predictions/sec
- CPU: <70% average
- Cost: <$0.01 per prediction
```

### 5. Explainability
**Requirements**:
- Feature importance available
- Prediction explanations
- Decision transparency
- Audit trail

**Validation**:
```
- Can explain top 5 factors per prediction
- Explanations align with domain knowledge
- Confidence scores calibrated
```

## Validation Process

### 1. Data Validation
```
Checks:
- Data quality (completeness, accuracy)
- Data balance (class distribution)
- Data leakage detection
- Train/test split verification
```

### 2. Model Validation
```
Tests:
- Holdout set evaluation
- Cross-validation
- Temporal validation (if time-series)
- Domain expert review
```

### 3. Business Validation
```
Verify:
- Solves business problem
- Meets ROI requirements
- Acceptable to stakeholders
- Integrates with processes
```

### 4. Compliance Validation
```
Ensure:
- Regulatory compliance
- Privacy requirements
- Security standards
- Ethical guidelines
```

## Validation Checklist

### Pre-Deployment
- [ ] Accuracy meets thresholds on test set
- [ ] Fairness validated across groups
- [ ] Performance meets SLA requirements
- [ ] Security testing passed
- [ ] Bias testing completed
- [ ] Explainability validated
- [ ] Business stakeholder approval
- [ ] Legal/compliance review
- [ ] Documentation complete
- [ ] Rollback plan ready

### Post-Deployment
- [ ] Production metrics match test metrics
- [ ] No data drift detected
- [ ] User acceptance positive
- [ ] Business KPIs improving
- [ ] Costs within budget
- [ ] No security incidents
- [ ] Monitoring configured
- [ ] Support team trained

## Validation Scenarios

### Classification Model
```
Example: Customer churn prediction

Validation Criteria:
- Accuracy: >90%
- Precision (churn): >85% (minimize false positives)
- Recall (churn): >80% (catch most churners)
- Fair across customer segments
- Explainable predictions
- Real-time inference <100ms
```

### NLP Model
```
Example: Sentiment analysis

Validation Criteria:
- Accuracy: >92%
- Works across languages
- Handles slang/emojis
- Confidence scores calibrated
- Consistent across demographics
- Latency <50ms
```

### Generative Model
```
Example: Response generation

Validation Criteria:
- Relevance: >90% (human eval)
- Factual accuracy: >95% (grounded in data)
- Toxicity: <1% (content filtering)
- Consistency: Similar inputs → similar outputs
- No PII leakage
```

## Continuous Validation

### Monitoring
```
Track in Production:
- Actual accuracy vs. baseline
- Distribution drift
- Performance degradation
- Error patterns
```

### Revalidation Triggers
```
When to Revalidate:
- Accuracy drops >5%
- Data distribution changes significantly
- Business requirements change
- Regulatory changes
- After model updates
```

## Tools and Frameworks

- **Azure Machine Learning**: Model validation tools
- **Responsible AI Toolkit**: Fairness, explainability
- **WhyLabs**: Data and model monitoring
- **Great Expectations**: Data validation
- **Custom scripts**: Business-specific validation

## Best Practices

1. **Baseline Early**: Establish validation criteria before building
2. **Iterative Validation**: Validate throughout development
3. **Real-World Testing**: Beta test with actual users
4. **Document Everything**: Validation results and decisions
5. **Stakeholder Involvement**: Include business and legal
6. **Continuous Monitoring**: Validation doesn't end at deployment
7. **Version Control**: Track model versions and validation results

## Related Resources

- [Azure ML model validation](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-validate-machine-learning-models)
- [Responsible AI](https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai)
- [ML model evaluation](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-understand-automated-ml)
