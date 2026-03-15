import requests
import json

def test_chat(message):
    url = "http://127.0.0.1:8000/chat"
    payload = {"message": message}
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        print(f"Message: {message}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        print("-" * 30)
    except Exception as e:
        print(f"Error testing {message}: {e}")

if __name__ == "__main__":
    # Test cases
    test_chat("I want to apply for electricity subsidy")
    test_chat("How to pay electric bill?")
    test_chat("Hello NovaBridge")
