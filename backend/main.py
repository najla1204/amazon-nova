from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

from agent_controller import AgentController
from document_parser import DocumentParser
from automation_controller import AutomationController

app = FastAPI(title="NovaBridge API")

# Setup Controllers
agent = AgentController()
doc_parser = DocumentParser()
automation = AutomationController()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

class AutomationRequest(BaseModel):
    task: str

class WorkflowRequest(BaseModel):
    message: str
    document_name: str

class DiscoveryRequest(BaseModel):
    message: str

class AgentRequest(BaseModel):
    message: str
    document_name: str

@app.get("/")
async def root():
    return {"message": "Welcome to NovaBridge AI Backend"}

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    """
    Endpoint for conversational AI assistant.
    """
    try:
        # The agent controller now returns intent and steps
        return await agent.get_response(request.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/discover-schemes")
async def discover_schemes_endpoint(request: DiscoveryRequest):
    """
    Uses Amazon Nova to discover eligible government schemes based on user needs.
    """
    try:
        return await agent.discover_schemes(request.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ai-agent")
async def ai_agent_endpoint(request: AgentRequest):
    """
    Unified AI Agent endpoint that orchestrates discovery, analysis, and automation.
    """
    try:
        return await agent.run_full_agent(request.message, request.document_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/upload-document")
async def upload_document(file: UploadFile = File(...)):
    """
    Endpoint for document image analysis.
    """
    try:
        content = await file.read()
        return await doc_parser.parse_document(content, filename=file.filename)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/start-automation")
async def start_automation(request: AutomationRequest):
    """
    Endpoint for triggering UI automation agents.
    """
    try:
        # For now, we trigger the full application workflow
        return await automation.start_application()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/run-workflow")
async def run_workflow(request: WorkflowRequest):
    """
    Orchestrates the full AI pipeline: Chat -> Doc Analysis -> Automation.
    """
    try:
        # 1. Detect Intent
        agent_resp = await agent.get_response(request.message)
        
        # 2. Parse Document (simulated with dummy bytes)
        doc_resp = await doc_parser.parse_document(b"", filename=request.document_name)
        
        # 3. Trigger Automation (simulated)
        auto_resp = await automation.start_application()
        
        return {
            "intent": agent_resp.get("intent"),
            "extracted_data": {
                "name": doc_resp.get("name"),
                "account_number": doc_resp.get("account_number"),
                "address": doc_resp.get("address")
            },
            "automation_status": auto_resp.get("status"),
            "application_id": auto_resp.get("application_id")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
