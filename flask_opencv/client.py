import requests
import json
import cv2

addr = 'http://localhost:5000'
test_url = addr + '/api/test'

content_type = 'image/png'
headers = {'content-type':content_type}

img = cv2.imread('./background.png')
_, img_encoded = cv2.imencode('.png', img)

response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)

print(json.loads(response.text))
