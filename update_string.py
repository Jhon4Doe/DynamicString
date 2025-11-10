import requests
import json

# Replace with your actual API endpoint
api_endpoint = "https://<key-value>.execute-api.us-east-1.amazonaws.com/prod/value"

# Data to send
data = {
    "value": "new string value"
}

# Make PUT request
response = requests.put(
    api_endpoint,
    headers={"Content-Type": "application/json"},
    data=json.dumps(data)
)

# Print response
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")