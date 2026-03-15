# NovaBridge

NovaBridge is an AI-powered system designed to assist elderly and non-technical users in applying for government subsidies. By leveraging voice interaction and intelligent automation, NovaBridge bypasses the need to navigate complex websites, making essential services more accessible.

## Architecture

NovaBridge follows a modern AI agent architecture:

- **Frontend**: A simple, voice-first React interface.
- **Backend**: FastAPI service for orchestration and API management.
- **AI Core (Amazon Nova)**:
    - **Nova 2 Lite**: Reasoning and intent classification.
    - **Nova 2 Sonic**: Real-time voice interaction (STT/TTS).
    - **Nova Act**: UI automation agents for interacting with government portals.
- **Orchestration**: LangChain for managing agentic workflows.

## Project Structure

```text
├── backend/              # FastAPI application
├── frontend/             # React (Vite) dashboard
├── agents/               # LangChain agent logic
├── automation/           # Nova Act browser automation
├── voice/                # Voice processing (Sonic)
├── document_processing/  # Document parsing (Nova Vision/Lite)
├── utils/                # Shared utilities
└── docs/                 # Documentation and diagrams
```

## Tech Stack

- **Backend**: Python 3.10+, FastAPI
- **Frontend**: React, Tailwind CSS
- **AI**: AWS Bedrock (Amazon Nova 2 Lite, Sonic, Act)
- **Framework**: LangChain, Boto3

## Getting Started

### Backend Setup
1. `cd backend`
2. `python -m venv venv`
3. `source venv/bin/activate` # or `venv\Scripts\activate` on Windows
4. `pip install -r requirements.txt`

### Frontend Setup
1. `cd frontend`
2. `npm install`
3. `npm run dev`
