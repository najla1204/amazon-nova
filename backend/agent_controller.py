class AgentController:
    """
    Orchestrates conversation, intent detection, and workflow planning.
    """
    def __init__(self):
        # Keep NovaClient initialized for future integration
        from nova_client import NovaClient
        self.nova = NovaClient()
        
        # Rule-based intent mapping
        self.intent_rules = {
            "electricity subsidy": "apply_electricity_subsidy",
            "electric bill": "apply_electricity_subsidy",
            "power subsidy": "apply_electricity_subsidy"
        }
        
        # Workflow steps for each intent
        self.workflow_plans = {
            "apply_electricity_subsidy": [
                "collect_electricity_bill",
                "extract_account_information",
                "open_subsidy_portal",
                "fill_application_form",
                "submit_application"
            ],
            "general_query": [
                "analyze_user_query",
                "search_knowledge_base",
                "generate_response"
            ]
        }

    def detect_intent(self, message: str) -> str:
        """
        Detects user intent using simple rule-based keywords.
        """
        msg_lower = message.lower()
        for keyword, intent in self.intent_rules.items():
            if keyword in msg_lower:
                return intent
        return "general_query"

    def get_workflow_steps(self, intent: str):
        """
        Returns the appropriate workflow steps for a given intent.
        """
        return self.workflow_plans.get(intent, self.workflow_plans["general_query"])

    async def discover_schemes(self, message: str):
        """
        Calls NovaClient to discover eligible schemes based on user query.
        """
        return self.nova.discover_schemes(message)

    async def run_full_agent(self, message: str, document_name: str):
        """
        Orchestrates the full AI agent pipeline with step-by-step logging.
        """
        results = {
            "intent": None,
            "eligible_schemes": [],
            "extraction_results": None,
            "automation_status": "skipped",
            "application_id": None,
            "steps_completed": [],
            "status": "pending"
        }

        # Step 1: Intent Detection
        print("\n[AI Agent] Step 1: Detecting intent...")
        intent = self.detect_intent(message)
        results["intent"] = intent
        results["steps_completed"].append("intent_detection")
        print(f"[AI Agent] Detected intent: {intent}")

        # Step 2: Scheme Discovery (if general or about benefits)
        print("[AI Agent] Step 2: Discovering relevant schemes...")
        discovery = self.nova.discover_schemes(message)
        results["eligible_schemes"] = discovery.get("eligible_schemes", [])
        results["steps_completed"].append("scheme_discovery")
        print(f"[AI Agent] Found {len(results['eligible_schemes'])} potential schemes.")

        # Step 3: Document Parsing (if intent is to apply)
        if intent == "apply_electricity_subsidy":
            print("[AI Agent] Step 3: Parsing document for application...")
            from document_parser import DocumentParser
            doc_parser = DocumentParser()
            # Simulated dummy content for tool invocation
            doc_resp = await doc_parser.parse_document(b"", filename=document_name)
            results["extraction_results"] = doc_resp
            results["steps_completed"].append("document_parsing")
            print(f"[AI Agent] Extraction complete for: {document_name}")

            # Step 4: Automation
            print("[AI Agent] Step 4: Triggering automation workflow...")
            from automation_controller import AutomationController
            automation = AutomationController()
            auto_resp = await automation.start_application()
            results["automation_status"] = auto_resp.get("status")
            results["application_id"] = auto_resp.get("application_id")
            results["steps_completed"].append("application_submission")
            results["status"] = "success"
            print(f"[AI Agent] Automation complete. App ID: {results['application_id']}")
        else:
            print("[AI Agent] Step 3: Skipping application steps (not an 'apply' intent).")
            results["status"] = "informational"

        return results

    async def get_response(self, user_message: str):
        """
        Processes request: detects intent and returns workflow plan.
        """
        intent = self.detect_intent(user_message)
        steps = self.get_workflow_steps(intent)
        
        return {
            "intent": intent,
            "steps": steps
        }
