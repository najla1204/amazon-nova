import requests
import json

def test_automation():
    url = "http://127.0.0.1:8000/start-automation"
    payload = {"task": "apply for electricity subsidy"}
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        print("Triggering automation workflow...")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        print("-" * 30)
    except Exception as e:
        print(f"Error triggering automation: {e}")

if __name__ == "__main__":
    test_automation()
