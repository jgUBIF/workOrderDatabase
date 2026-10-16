import requests
import json

url = "https://portal.ubreakifix.net/api/workorders"

headers = {
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "priority": "u=1, i",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36",
    "x-channel-id": "paste from chrome",
    "x-fs-session": "paste from chrome",
    "x-response-id": "paste from chrome",
    "cookie": "paste from chrome"
}

# The JSON payload converted to a Python dictionary
payload = {
    "page": 1,
    "pageSize": 10,
    "deviceTypeIds": [],
    "serviceOutcome": [],
    "programIds": [],
    "needsAttention": False,
    "order": "closed,DESC",
    "tab": None,
    "primaryFilter": "Closed",
}

# Making the POST request
response = requests.post(url, headers=headers, json=payload)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print("Success!")
    print(data)
else:
    print(f"Failed with status code: {response.status_code}")
    print(response.text)


with open("data.json", "w") as file:
    json.dump(data, file)
