# WORDCLOUD API

A flask API that receives text and returns the url to the generated wordcloud image.

![sample](https://github.com/Yodeman/iqube_projects/blob/main/flask_wordcloud/sample.jpg)

The live API can be called just like below:
``` python
import requests
import json

endpoint = "https://paul-wordcloud-app.herokuapp.com/generate"

content_type = "text/html"
headers = {"content-type":content_type}

text = {}

#load the text file.
with open('sample.txt', 'r') as f:
    text["text"] = f.read()

#The api expects a json file.    
data = json.dumps(text)

response = requests.post(endpoint, data=data, headers=headers)

#Get the returned urls
response = json.loads(response.text)["URL"]
print(f"Image URL: {response}")
```
