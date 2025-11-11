#!/usr/bin/env python3
"""
Update all pages with section numbers and page breaks
"""
import os
import re

# Define the page numbering structure based on SUMMARY.md
page_mappings = {
    # Plan AI Solutions (Section 1)
    'src/plan-ai-solutions/assess-agents-use.md': ('1.1.1', 'Assess the Use of Agents in Task Automation, Data Analytics, and Decision-Making'),
    'src/plan-ai-solutions/review-data-grounding.md': ('1.1.2', 'Review Data for Grounding'),
    'src/plan-ai-solutions/organize-business-data.md': ('1.1.3', 'Organize Business Solution Data'),
    'src/plan-ai-solutions/implement-ai-adoption-caf.md': ('1.2.1', 'Implement AI Adoption Process from Cloud Adoption Framework'),
    'src/plan-ai-solutions/design-ai-agents-strategy.md': ('1.2.2', 'Design Strategy for Building AI and Agents'),
    'src/plan-ai-solutions/design-multi-agent-solution.md': ('1.2.3', 'Design Multi-Agent Solutions'),
    'src/plan-ai-solutions/develop-prebuilt-agents-use-cases.md': ('1.2.4', 'Develop Use Cases for Prebuilt Agents'),
    'src/plan-ai-solutions/define-solution-rules-constraints.md': ('1.2.5', 'Define Solution Rules and Constraints'),
    'src/plan-ai-solutions/determine-generative-ai-knowledge-sources.md': ('1.2.6', 'Determine Use of Generative AI and Knowledge Sources'),
    'src/plan-ai-solutions/determine-custom-agents-vs-extend-copilot.md': ('1.2.7', 'Determine When to Build Custom Agents or Extend Microsoft 365 Copilot'),
    'src/plan-ai-solutions/determine-custom-ai-models.md': ('1.2.8', 'Determine When Custom AI Models Should Be Created'),
    'src/plan-ai-solutions/create-prompt-library-guidelines.md': ('1.2.9', 'Provide Guidelines for Creating a Prompt Library'),
    'src/plan-ai-solutions/develop-small-language-models-use-cases.md': ('1.2.10', 'Develop Use Cases for Customized Small Language Models'),
    'src/plan-ai-solutions/prompt-engineering-guidelines.md': ('1.2.11', 'Provide Prompt Engineering Guidelines and Techniques'),
    'src/plan-ai-solutions/include-ai-center-excellence-elements.md': ('1.2.12', 'Include Elements of Microsoft AI Center of Excellence'),
    'src/plan-ai-solutions/design-multi-dynamics365-ai-solutions.md': ('1.2.13', 'Design AI Solutions Using Multiple Dynamics 365 Apps'),
    'src/plan-ai-solutions/select-roi-criteria.md': ('1.3.1', 'Select ROI Criteria Including Total Cost of Ownership'),
    'src/plan-ai-solutions/create-roi-analysis.md': ('1.3.2', 'Create ROI Analysis for Proposed AI Solution'),
    'src/plan-ai-solutions/analyze-build-buy-extend.md': ('1.3.3', 'Analyze Whether to Build, Buy, or Extend AI Components'),
    'src/plan-ai-solutions/implement-model-router.md': ('1.3.4', 'Implement Model Router'),
    'src/plan-ai-solutions/hands-on-labs.md': ('1.4', 'Hands-On Labs: Plan AI Solutions'),
    'src/plan-ai-solutions/practice-quiz.md': ('1.5', 'Practice Quiz: Plan AI Solutions (20-25%)'),
    
    # Design AI Solutions (Section 2)
    'src/design-ai-solutions/design-business-terms-copilot-d365.md': ('2.1.1', 'Design Business Terms for Copilot in Dynamics 365'),
    'src/design-ai-solutions/design-customizations-copilot-d365.md': ('2.1.2', 'Design Customizations of Copilot in Dynamics 365'),
    'src/design-ai-solutions/design-connectors-copilot-sales.md': ('2.1.3', 'Design Connectors for Copilot in Dynamics 365 Sales'),
    'src/design-ai-solutions/design-agents-contact-center.md': ('2.1.4', 'Design Agents for Dynamics 365 Contact Center'),
    'src/design-ai-solutions/design-task-agents.md': ('2.1.5', 'Design Task Agents'),
    'src/design-ai-solutions/design-autonomous-agents.md': ('2.1.6', 'Design Autonomous Agents'),
    'src/design-ai-solutions/design-prompt-response-agents.md': ('2.1.7', 'Design Prompt and Response Agents'),
    'src/design-ai-solutions/propose-microsoft-ai-services.md': ('2.1.8', 'Propose Microsoft AI Services'),
    'src/design-ai-solutions/propose-code-first-generative-pages.md': ('2.1.9', 'Propose Code-First Generative Pages and Agent Feed'),
    'src/design-ai-solutions/design-topics-copilot-studio.md': ('2.1.10', 'Design Topics for Copilot Studio'),
    'src/design-ai-solutions/design-data-processing-grounding.md': ('2.1.11', 'Design Data Processing for AI Models and Grounding'),
    'src/design-ai-solutions/design-business-process-power-apps.md': ('2.1.12', 'Design Business Process with AI in Power Apps'),
    'src/design-ai-solutions/apply-power-platform-waf.md': ('2.1.13', 'Apply Power Platform Well-Architected Framework'),
    'src/design-ai-solutions/determine-nlp-clu-generative-ai.md': ('2.1.14', 'Determine NLP, CLU, or Generative AI Orchestration'),
    'src/design-ai-solutions/design-agents-flows-copilot-studio.md': ('2.1.15', 'Design Agents and Agent Flows with Copilot Studio'),
    'src/design-ai-solutions/design-prompt-actions-copilot-studio.md': ('2.1.16', 'Design Prompt Actions in Copilot Studio'),
    'src/design-ai-solutions/design-custom-models-ai-foundry.md': ('2.2.1', 'Design AI Solutions Using Custom Models in Azure AI Foundry'),
    'src/design-ai-solutions/design-agents-m365-copilot.md': ('2.2.2', 'Design Agents in Microsoft 365 Copilot'),
    'src/design-ai-solutions/design-agent-extensibility-copilot-studio.md': ('2.2.3', 'Design Agent Extensibility in Copilot Studio'),
    'src/design-ai-solutions/design-agent-extensibility-mcp.md': ('2.2.4', 'Design Agent Extensibility with Model Context Protocol'),
    'src/design-ai-solutions/design-agents-computer-use.md': ('2.2.5', 'Design Agents Using Computer Use in Copilot Studio'),
    'src/design-ai-solutions/design-agent-behaviors-copilot-studio.md': ('2.2.6', 'Design Agent Behaviors in Copilot Studio'),
    'src/design-ai-solutions/optimize-agents-m365.md': ('2.2.7', 'Optimize Solution Design Using Agents in Microsoft 365'),
    'src/design-ai-solutions/orchestrate-ai-finance-supply-chain.md': ('2.3.1', 'Orchestrate AI in Dynamics 365 Finance and Supply Chain'),
    'src/design-ai-solutions/orchestrate-ai-customer-experience.md': ('2.3.2', 'Orchestrate AI in Dynamics 365 Customer Experience and Service'),
    'src/design-ai-solutions/propose-m365-agents.md': ('2.3.3', 'Propose Microsoft 365 Agents for Business Scenarios'),
    'src/design-ai-solutions/orchestrate-m365-copilot-sales-service.md': ('2.3.4', 'Orchestrate Configuration of Microsoft 365 Copilot for Sales and Service'),
    'src/design-ai-solutions/propose-power-platform-ai-features.md': ('2.3.5', 'Propose Microsoft Power Platform AI Features'),
    'src/design-ai-solutions/design-interop-finance-ops-agents.md': ('2.3.6', 'Design Interoperability of Finance and Operations Agent Chats'),
    'src/design-ai-solutions/recommend-knowledge-sources-in-app-help.md': ('2.3.7', 'Recommend Adding Knowledge Sources to In-App Help'),
    'src/design-ai-solutions/hands-on-labs.md': ('2.4', 'Hands-On Labs: Design AI Solutions'),
    'src/design-ai-solutions/practice-quiz.md': ('2.5', 'Practice Quiz: Design AI Solutions (40-45%)'),
    
    # Deploy AI Solutions (Section 3)
    'src/deploy-ai-solutions/recommend-monitoring-tools.md': ('3.1.1', 'Recommend Process and Tools for Monitoring Agents'),
    'src/deploy-ai-solutions/analyze-backlog-user-feedback.md': ('3.1.2', 'Analyze Backlog and User Feedback'),
    'src/deploy-ai-solutions/apply-ai-tools-analysis-tuning.md': ('3.1.3', 'Apply AI-Based Tools for Analysis and Tuning'),
    'src/deploy-ai-solutions/monitor-agent-performance.md': ('3.1.4', 'Monitor Agent Performance and Metrics'),
    'src/deploy-ai-solutions/interpret-telemetry-data.md': ('3.1.5', 'Interpret Telemetry Data for Performance Tuning'),
    'src/deploy-ai-solutions/recommend-testing-process-metrics.md': ('3.2.1', 'Recommend Process and Metrics to Test Agents'),
    'src/deploy-ai-solutions/create-validation-criteria.md': ('3.2.2', 'Create Validation Criteria for Custom AI Models'),
    'src/deploy-ai-solutions/validate-prompt-best-practices.md': ('3.2.3', 'Validate Effective Copilot Prompt Best Practices'),
    'src/deploy-ai-solutions/design-end-to-end-test-scenarios.md': ('3.2.4', 'Design End-to-End Test Scenarios'),
    'src/deploy-ai-solutions/build-test-cases-strategy.md': ('3.2.5', 'Build Strategy for Creating Test Cases Using Copilot'),
    'src/deploy-ai-solutions/design-alm-data.md': ('3.3.1', 'Design ALM Process for Data in AI Models and Agents'),
    'src/deploy-ai-solutions/design-alm-copilot-studio.md': ('3.3.2', 'Design ALM Process for Copilot Studio Agents'),
    'src/deploy-ai-solutions/design-alm-azure-ai-services.md': ('3.3.3', 'Design ALM Process for Azure AI Services Agents'),
    'src/deploy-ai-solutions/design-alm-custom-models.md': ('3.3.4', 'Design ALM Process for Custom AI Models'),
    'src/deploy-ai-solutions/design-alm-finance-supply-chain.md': ('3.3.5', 'Design ALM Process for AI in Dynamics 365 Finance and Supply Chain'),
    'src/deploy-ai-solutions/design-alm-customer-experience.md': ('3.3.6', 'Design ALM Process for AI in Dynamics 365 Customer Experience'),
    'src/deploy-ai-solutions/design-security-agents.md': ('3.4.1', 'Design Security for Agents'),
    'src/deploy-ai-solutions/design-governance-agents.md': ('3.4.2', 'Design Governance for Agents'),
    'src/deploy-ai-solutions/design-model-security.md': ('3.4.3', 'Design Model Security'),
    'src/deploy-ai-solutions/analyze-vulnerabilities.md': ('3.4.4', 'Analyze Solution and AI Vulnerabilities'),
    'src/deploy-ai-solutions/review-responsible-ai-principles.md': ('3.4.5', 'Review Solution for Responsible AI Principles'),
    'src/deploy-ai-solutions/validate-data-residency-compliance.md': ('3.4.6', 'Validate Data Residency and Movement Compliance'),
    'src/deploy-ai-solutions/design-access-controls-grounding-data.md': ('3.4.7', 'Design Access Controls on Grounding Data'),
    'src/deploy-ai-solutions/design-audit-trails.md': ('3.4.8', 'Design Audit Trails for Changes'),
    'src/deploy-ai-solutions/hands-on-labs.md': ('3.5', 'Hands-On Labs: Deploy AI Solutions'),
    'src/deploy-ai-solutions/practice-quiz.md': ('3.6', 'Practice Quiz: Deploy AI Solutions (30-35%)'),
}

def update_file(filepath, number, title):
    """Update a file with page break and numbered title"""
    full_path = os.path.join('/home/user/ab100', filepath)
    
    if not os.path.exists(full_path):
        print(f"Warning: {full_path} does not exist")
        return False
    
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the first heading
    lines = content.split('\n')
    first_heading_idx = -1
    for i, line in enumerate(lines):
        if line.startswith('# '):
            first_heading_idx = i
            break
    
    if first_heading_idx == -1:
        print(f"Warning: No heading found in {filepath}")
        return False
    
    # Create new heading with number
    new_heading = f"# {number} {title}"
    
    # Add page break at the beginning if not already present
    page_break = '<div style="page-break-before: always;"></div>\n'
    
    # Check if page break already exists at the start
    if lines[0].strip().startswith('<div style="page-break'):
        # Already has page break, just update heading
        lines[first_heading_idx] = new_heading
    else:
        # Add page break and update heading
        lines[first_heading_idx] = new_heading
        lines.insert(0, page_break)
    
    # Write updated content
    new_content = '\n'.join(lines)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✓ Updated: {number} - {title}")
    return True

def main():
    """Update all pages with numbering and page breaks"""
    print("Updating all pages with section numbers and page breaks...\n")
    
    updated_count = 0
    failed_count = 0
    
    for filepath, (number, title) in sorted(page_mappings.items()):
        if update_file(filepath, number, title):
            updated_count += 1
        else:
            failed_count += 1
    
    print(f"\n{'='*60}")
    print(f"Summary: {updated_count} files updated, {failed_count} failed")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
