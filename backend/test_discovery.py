import requests
import json

def test_discovery(message):
    url = "http://127.0.0.1:8000/discover-schemes"
    payload = {"message": message}
    headers = {"Content-Type": "application/json"}
    
    try:
        print(f"User Query: {message}")
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            print(f"Response: {json.dumps(response.json(), indent=2)}")
        else:
            print(f"Error {response.status_code}: {response.text}")
        print("-" * 30)
    except Exception as e:
        print(f"Error testing discovery: {e}")

if __name__ == "__main__":
    # Test case
    test_discovery("I am a low income household struggling to pay electricity bills")
