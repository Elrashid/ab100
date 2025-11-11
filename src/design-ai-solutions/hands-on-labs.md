# Hands-On Labs: Design AI Solutions

## Lab 1: Design and Build a Copilot Studio Agent

**Duration:** 60 minutes  
**Objective:** Create a functional customer service agent in Copilot Studio

### Prerequisites
- Copilot Studio license or trial
- Power Platform environment
- Sample FAQ data

### Steps

1. **Create New Agent**
   - Navigate to [Copilot Studio](https://copilotstudio.microsoft.com/)
   - Click "Create" → "New copilot"
   - Name: "Customer Support Agent"
   - Select environment

2. **Configure Topics**
   ```
   Topic: Order Status Inquiry
   
   Trigger Phrases:
   - "Where is my order"
   - "Track my order"
   - "Order status"
   - "Check order"
   
   Dialog Flow:
   1. Ask for order number
   2. Validate format (regex: ^ORD[0-9]{6}$)
   3. Call Power Automate flow to fetch status
   4. Display order information
   5. Ask if they need more help
   ```

3. **Design Conversation Flow**
   ```
   [User enters] → [Identify Intent]
                          ↓
                   [Route to Topic]
                          ↓
                   [Gather Information]
                          ↓
                   [Execute Action]
                          ↓
                   [Provide Response]
                          ↓
                   [Offer Next Steps]
   ```

4. **Add Entities**
   - Create custom entity: "OrderNumber"
   - Pattern: `ORD[0-9]{6}`
   - Add synonyms for common variations

5. **Integrate with Data**
   - Create Power Automate flow
   - Connect to Dataverse
   - Query order status
   - Return formatted response

6. **Test the Agent**
   - Use test chat panel
   - Test various scenarios:
     - Valid order number
     - Invalid format
     - Order not found
     - Multiple inquiries
   - Check fallback handling

7. **Add Generative Answers**
   - Enable generative AI
   - Add knowledge source: Company FAQ SharePoint site
   - Configure grounding settings
   - Set confidence threshold: 0.7

8. **Configure Authentication** (Optional)
   - Enable authentication
   - Select Azure AD
   - Configure scopes: User.Read
   - Test with authenticated user

### Expected Outcome
- Working Copilot Studio agent
- Multiple topics configured
- Integrated with backend data
- Generative AI enabled
- Tested and validated

---

## Lab 2: Implement RAG with Azure AI Search

**Duration:** 45 minutes  
**Objective:** Build a Retrieval-Augmented Generation system

### Steps

1. **Set Up Azure AI Search**
   ```bash
   # Create search service
   az search service create \
     --name contoso-search \
     --resource-group rg-ai-lab \
     --sku standard \
     --location eastus
   ```

2. **Prepare Documents**
   ```python
   # Sample documents structure
   documents = [
       {
           "id": "1",
           "title": "Product Return Policy",
           "content": "Our return policy allows returns within 30 days...",
           "category": "Policy",
           "last_updated": "2025-01-15"
       },
       {
           "id": "2",
           "title": "Shipping Information",
           "content": "We offer standard and expedited shipping...",
           "category": "Shipping",
           "last_updated": "2025-01-10"
       }
   ]
   ```

3. **Create Search Index**
   ```python
   from azure.search.documents.indexes import SearchIndexClient
   from azure.search.documents.indexes.models import (
       SearchIndex,
       SimpleField,
       SearchableField,
       SemanticConfiguration,
       SemanticField,
       VectorSearch,
       VectorSearchProfile
   )
   
   index = SearchIndex(
       name="knowledge-base",
       fields=[
           SimpleField(name="id", type="Edm.String", key=True),
           SearchableField(name="title", type="Edm.String"),
           SearchableField(name="content", type="Edm.String"),
           SearchableField(name="category", type="Edm.String", filterable=True),
           SimpleField(name="last_updated", type="Edm.DateTimeOffset")
       ],
       semantic_search=SemanticConfiguration(
           name="default",
           prioritized_fields=SemanticField(
               title_field="title",
               content_fields=["content"]
           )
       )
   )
   
   index_client.create_index(index)
   ```

4. **Index Documents**
   ```python
   from azure.search.documents import SearchClient
   
   search_client = SearchClient(
       endpoint=search_endpoint,
       index_name="knowledge-base",
       credential=credential
   )
   
   result = search_client.upload_documents(documents=documents)
   print(f"Indexed {len(result)} documents")
   ```

5. **Implement RAG Pattern**
   ```python
   from openai import AzureOpenAI
   
   def rag_query(user_question):
       # Step 1: Retrieve relevant documents
       search_results = search_client.search(
           search_text=user_question,
           top=3,
           select=["title", "content"]
       )
       
       # Step 2: Build context from results
       context = "\n\n".join([
           f"Document: {doc['title']}\n{doc['content']}"
           for doc in search_results
       ])
       
       # Step 3: Generate answer with context
       client = AzureOpenAI(
           api_key=api_key,
           api_version="2024-02-15-preview",
           azure_endpoint=endpoint
       )
       
       response = client.chat.completions.create(
           model="gpt-4",
           messages=[
               {"role": "system", "content": "You are a helpful assistant. Use the provided context to answer questions. If the answer isn't in the context, say so."},
               {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {user_question}"}
           ],
           temperature=0.7
       )
       
       return response.choices[0].message.content
   
   # Test
   answer = rag_query("What is your return policy?")
   print(answer)
   ```

6. **Add Semantic Ranking**
   ```python
   # Enhanced search with semantic ranking
   results = search_client.search(
       search_text=user_question,
       query_type="semantic",
       semantic_configuration_name="default",
       top=5
   )
   
   for result in results:
       print(f"Score: {result['@search.score']}")
       print(f"Title: {result['title']}")
       print(f"Reranker Score: {result['@search.reranker_score']}")
   ```

### Expected Outcome
- Azure AI Search index created
- Documents indexed with semantic search
- RAG system working
- Answers grounded in knowledge base

---

## Lab 3: Build a Task Agent with Azure Functions

**Duration:** 45 minutes  
**Objective:** Create a deterministic task agent for data processing

### Steps

1. **Create Azure Function**
   ```bash
   # Initialize function app
   func init TaskAgentApp --python
   cd TaskAgentApp
   func new --name DataProcessorAgent --template "HTTP trigger"
   ```

2. **Implement Task Logic**
   ```python
   import azure.functions as func
   import json
   import logging
   from datetime import datetime
   
   app = func.FunctionApp()
   
   @app.function_name(name="DataProcessorAgent")
   @app.route(route="process", methods=["POST"])
   def data_processor(req: func.HttpRequest) -> func.HttpResponse:
       logging.info('Task agent processing request')
       
       try:
           req_body = req.get_json()
           task_type = req_body.get('task_type')
           data = req_body.get('data')
           
           # Route to appropriate processor
           if task_type == 'validate_email':
               result = validate_email_task(data)
           elif task_type == 'format_phone':
               result = format_phone_task(data)
           elif task_type == 'calculate_total':
               result = calculate_total_task(data)
           else:
               return func.HttpResponse(
                   json.dumps({"error": "Unknown task type"}),
                   status_code=400
               )
           
           return func.HttpResponse(
               json.dumps({
                   "status": "success",
                   "result": result,
                   "timestamp": datetime.utcnow().isoformat()
               }),
               mimetype="application/json"
           )
           
       except Exception as e:
           logging.error(f"Error: {str(e)}")
           return func.HttpResponse(
               json.dumps({"error": str(e)}),
               status_code=500
           )
   
   def validate_email_task(email):
       import re
       pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
       is_valid = bool(re.match(pattern, email))
       return {
           "email": email,
           "is_valid": is_valid
       }
   
   def format_phone_task(phone):
       # Remove non-digits
       digits = ''.join(filter(str.isdigit, phone))
       # Format as (XXX) XXX-XXXX
       if len(digits) == 10:
           formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
           return {"formatted_phone": formatted}
       else:
           return {"error": "Invalid phone number length"}
   
   def calculate_total_task(items):
       total = sum(item.get('price', 0) * item.get('quantity', 0) 
                   for item in items)
       return {
           "total": total,
           "item_count": len(items)
       }
   ```

3. **Add Error Handling and Retries**
   ```python
   from tenacity import retry, stop_after_attempt, wait_exponential
   
   @retry(
       stop=stop_after_attempt(3),
       wait=wait_exponential(multiplier=1, min=2, max=10)
   )
   def process_with_retry(task_func, data):
       return task_func(data)
   ```

4. **Deploy to Azure**
   ```bash
   # Create function app
   az functionapp create \
     --resource-group rg-ai-lab \
     --consumption-plan-location eastus \
     --runtime python \
     --runtime-version 3.11 \
     --functions-version 4 \
     --name task-agent-app \
     --storage-account taskstorage
   
   # Deploy
   func azure functionapp publish task-agent-app
   ```

5. **Test the Agent**
   ```python
   import requests
   
   # Test email validation
   response = requests.post(
       "https://task-agent-app.azurewebsites.net/api/process",
       json={
           "task_type": "validate_email",
           "data": "user@example.com"
       }
   )
   print(response.json())
   
   # Test phone formatting
   response = requests.post(
       "https://task-agent-app.azurewebsites.net/api/process",
       json={
           "task_type": "format_phone",
           "data": "5551234567"
       }
   )
   print(response.json())
   ```

### Expected Outcome
- Deployed task agent function
- Multiple task handlers
- Error handling implemented
- API tested and working

---

## Lab 4: Design Autonomous Agent with Reasoning Loop

**Duration:** 60 minutes  
**Objective:** Build an autonomous agent that can plan and execute multi-step tasks

### Steps

1. **Install Required Packages**
   ```bash
   pip install semantic-kernel azure-ai-openai
   ```

2. **Create Agent Framework**
   ```python
   import semantic_kernel as sk
   from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
   from semantic_kernel.planning import ActionPlanner
   
   # Initialize kernel
   kernel = sk.Kernel()
   
   # Add Azure OpenAI
   kernel.add_service(
       AzureChatCompletion(
           deployment_name="gpt-4",
           endpoint=azure_endpoint,
           api_key=api_key
       )
   )
   ```

3. **Define Agent Skills**
   ```python
   from semantic_kernel.skill_definition import sk_function
   
   class ResearchSkill:
       @sk_function(
           description="Search the web for information",
           name="search_web"
       )
       def search_web(self, query: str) -> str:
           # Implement web search
           results = perform_web_search(query)
           return f"Search results for '{query}': {results}"
       
       @sk_function(
           description="Analyze a company's website",
           name="analyze_company"
       )
       def analyze_company(self, company_name: str) -> str:
           # Implement company analysis
           info = fetch_company_info(company_name)
           return f"Company analysis: {info}"
   
   class DataSkill:
       @sk_function(
           description="Query CRM database",
           name="query_crm"
       )
       def query_crm(self, query: str) -> str:
           # Query Dataverse
           results = execute_crm_query(query)
           return f"CRM data: {results}"
   
   # Register skills
   research_skill = kernel.import_skill(ResearchSkill(), "ResearchSkill")
   data_skill = kernel.import_skill(DataSkill(), "DataSkill")
   ```

4. **Implement Reasoning Loop**
   ```python
   class AutonomousAgent:
       def __init__(self, kernel):
           self.kernel = kernel
           self.planner = ActionPlanner(kernel)
           self.memory = []
       
       async def execute_goal(self, goal: str):
           print(f"Goal: {goal}")
           
           # Create plan
           plan = await self.planner.create_plan_async(goal)
           print(f"Plan created with {len(plan._steps)} steps")
           
           # Execute plan with reasoning loop
           for i, step in enumerate(plan._steps):
               print(f"\nStep {i+1}: {step.description}")
               
               # Execute step
               result = await step.invoke_async(self.kernel)
               
               # Store in memory
               self.memory.append({
                   "step": i+1,
                   "action": step.description,
                   "result": str(result)
               })
               
               # Evaluate if goal is met
               if self.is_goal_complete(goal, self.memory):
                   print("Goal achieved!")
                   break
               
               # Adjust plan if needed
               if self.needs_replanning(result):
                   print("Replanning...")
                   plan = await self.planner.create_plan_async(
                       goal,
                       context=self.get_context()
                   )
           
           return self.memory
       
       def is_goal_complete(self, goal, memory):
           # Check if goal is satisfied
           # Use LLM to evaluate completion
           context = "\n".join([
               f"{m['action']}: {m['result']}" 
               for m in memory
           ])
           # Evaluate with LLM
           return False  # Implement evaluation logic
       
       def needs_replanning(self, result):
           # Determine if plan needs adjustment
           return "error" in str(result).lower()
       
       def get_context(self):
           return "\n".join([
               f"{m['action']}: {m['result']}" 
               for m in self.memory
           ])
   ```

5. **Test the Agent**
   ```python
   import asyncio
   
   async def main():
       agent = AutonomousAgent(kernel)
       
       goal = """
       Research Contoso Corporation and create a summary including:
       1. Company overview
       2. Recent news
       3. Key decision makers
       4. Potential opportunities based on our CRM data
       """
       
       results = await agent.execute_goal(goal)
       
       print("\n=== Execution Summary ===")
       for item in results:
           print(f"Step {item['step']}: {item['action']}")
           print(f"Result: {item['result']}\n")
   
   asyncio.run(main())
   ```

### Expected Outcome
- Autonomous agent with reasoning
- Multi-step plan execution
- Dynamic replanning capability
- Goal evaluation logic

---

## Lab 5: Implement Model Context Protocol (MCP) Server

**Duration:** 45 minutes  
**Objective:** Build an MCP server to expose tools to AI agents

### Steps

1. **Install MCP SDK**
   ```bash
   pip install mcp
   ```

2. **Create MCP Server**
   ```python
   from mcp.server import Server
   from mcp.server.stdio import stdio_server
   from mcp.types import Tool, TextContent
   
   app = Server("crm-tools-server")
   
   @app.list_tools()
   async def list_tools() -> list[Tool]:
       return [
           Tool(
               name="get_account_info",
               description="Retrieve account information from CRM",
               inputSchema={
                   "type": "object",
                   "properties": {
                       "account_id": {
                           "type": "string",
                           "description": "The account ID"
                       }
                   },
                   "required": ["account_id"]
               }
           ),
           Tool(
               name="create_opportunity",
               description="Create a new sales opportunity",
               inputSchema={
                   "type": "object",
                   "properties": {
                       "account_id": {"type": "string"},
                       "name": {"type": "string"},
                       "estimated_value": {"type": "number"}
                   },
                   "required": ["account_id", "name"]
               }
           )
       ]
   
   @app.call_tool()
   async def call_tool(name: str, arguments: dict) -> list[TextContent]:
       if name == "get_account_info":
           account_id = arguments["account_id"]
           # Query CRM
           info = fetch_account_info(account_id)
           return [TextContent(
               type="text",
               text=f"Account Info: {info}"
           )]
       
       elif name == "create_opportunity":
           # Create opportunity in CRM
           result = create_crm_opportunity(arguments)
           return [TextContent(
               type="text",
               text=f"Created opportunity: {result}"
           )]
       
       else:
           raise ValueError(f"Unknown tool: {name}")
   
   def fetch_account_info(account_id):
       # Implement Dataverse query
       return {
           "id": account_id,
           "name": "Contoso Corp",
           "industry": "Technology",
           "annual_revenue": 5000000
       }
   
   def create_crm_opportunity(data):
       # Implement Dataverse create
       return {
           "id": "opp-123",
           "status": "created"
       }
   ```

3. **Run MCP Server**
   ```python
   async def main():
       async with stdio_server() as (read_stream, write_stream):
           await app.run(
               read_stream,
               write_stream,
               app.create_initialization_options()
           )
   
   if __name__ == "__main__":
       import asyncio
       asyncio.run(main())
   ```

4. **Configure Agent to Use MCP**
   ```json
   {
     "mcpServers": {
       "crm-tools": {
         "command": "python",
         "args": ["mcp_server.py"]
       }
     }
   }
   ```

5. **Test Integration**
   ```python
   # Agent using MCP tools
   from mcp.client import Client
   
   async def test_mcp():
       async with Client("crm-tools") as client:
           # List available tools
           tools = await client.list_tools()
           print("Available tools:", tools)
           
           # Call tool
           result = await client.call_tool(
               "get_account_info",
               {"account_id": "acc-001"}
           )
           print("Result:", result)
   
   asyncio.run(test_mcp())
   ```

### Expected Outcome
- MCP server exposing CRM tools
- Tools discoverable by agents
- Successful tool invocation
- Integration tested

---

## Additional Resources

- [Copilot Studio Documentation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/)
- [Azure AI Search Labs](https://learn.microsoft.com/en-us/azure/search/)
- [Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/)
