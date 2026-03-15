import requests
import os

def test_upload(filename, content=b"fake image content"):
    url = "http://127.0.0.1:8000/upload-document"
    
    # Create a temporary file to upload
    with open(filename, "wb") as f:
        f.write(content)
    
    try:
        with open(filename, "rb") as f:
            files = {"file": (filename, f, "image/png")}
            response = requests.post(url, files=files)
            print(f"Uploaded: {filename}")
            print(f"Response: {response.json()}")
            print("-" * 30)
    except Exception as e:
        print(f"Error uploading {filename}: {e}")
    finally:
        if os.path.exists(filename):
            os.remove(filename)

if __name__ == "__main__":
    # Test cases
    test_upload("my_bill.png")
    test_upload("id_card.jpg")
