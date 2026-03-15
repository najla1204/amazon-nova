from langchain_aws import ChatBedrock
import os

def get_nova_lite_agent():
    """
    Returns a ChatBedrock instance configured with Amazon Nova Lite 2.
    """
    return ChatBedrock(
        model_id=os.getenv("NOVA_LITE_MODEL_ID", "amazon.nova-lite-v1:0"),
        model_kwargs={"temperature": 0.5}
    )

class SubsidyAgent:
    def __init__(self):
        self.llm = get_nova_lite_agent()
    
    def process_request(self, user_voice_input: str):
        # Reasoning logic for subsidy application
        pass
