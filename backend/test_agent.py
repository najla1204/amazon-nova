import requests
import json

def test_agent(message, document_name):
    url = "http://127.0.0.1:8000/ai-agent"
    payload = {
        "message": message,
        "document_name": document_name
    }
    headers = {"Content-Type": "application/json"}
    
    try:
        print(f"User Request: {message}")
        print(f"Document: {document_name}")
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            print("Agent Workflow Result:")
            print(json.dumps(response.json(), indent=2))
        else:
            print(f"Error {response.status_code}: {response.text}")
        print("-" * 50)
    except Exception as e:
        print(f"Error testing agent: {e}")

if __name__ == "__main__":
    # Test 1: Application Intent
    test_agent("I want to apply for electricity subsidy", "electricity_bill.jpg")
    
    # Test 2: Discovery/Informational Intent
    test_agent("I am a low income student, what help can I get?", "none")
