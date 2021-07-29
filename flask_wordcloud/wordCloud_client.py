import requests
import json

endpoint = "http://localhost:8052""/generate"

content_type = "text/html"
headers = {"content-type":content_type}

text = {}

with open('sample.txt', 'r') as f:
    text["text"] = f.read()

response = requests.post(endpoint, data=json.dumps(text), headers=headers)
print(f"Image URL: {json.loads(response.text)['URL']}")
