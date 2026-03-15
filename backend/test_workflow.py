import requests
import json

def test_workflow():
    url = "http://127.0.0.1:8000/run-workflow"
    payload = {
        "message": "I want electricity subsidy",
        "document_name": "electricity_bill.png"
    }
    headers = {"Content-Type": "application/json"}
    
    try:
        print("Running full workflow orchestration...")
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        print("-" * 30)
    except Exception as e:
        print(f"Error running workflow: {e}")

if __name__ == "__main__":
    test_workflow()
