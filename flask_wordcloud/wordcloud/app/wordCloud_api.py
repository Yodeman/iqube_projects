import os
import json
import boto3
import wordcloud as wc
from flask import Flask, request, Response

app = Flask(__name__)
n = 0
with open("rootkey.csv", 'r') as f:
    file = f.readlines()
    accessKeyId = file[0].strip('\n').split('=')[1]
    accessSecretKey = file[1].strip('\n').split('=')[1]
    
path = "https://myflaskwordcloud.s3.eu-west-3.amazonaws.com/wordCloudImages/"
s3 = boto3.client("s3",
                  aws_access_key_id=accessKeyId,
                  aws_secret_access_key=accessSecretKey
                  )
@app.route('/', methods=["GET"])
def home():
    return "Welcome to my wordcloud api."


@app.route('/generate', methods=["POST", "GET"])
def generate():
    global n
    word_cloud = wc.WordCloud()
    r = json.loads(request.data)
    text = r.get("text", None)
    if text:
        fname = f"sample_{n}.png"
        word_cloud.generate(text)
        word_cloud.to_file(fname)
        img =  open(fname, "rb")
        s3.upload_fileobj(
                img, "myflaskwordcloud" , "wordCloudImages/"+fname,
                ExtraArgs={
                        "ACL":"public-read",
                        "ContentType":"image/png",
                    }
            )
        img.close()
        os.remove("./"+fname)
        img_uri = json.dumps({"URL":path+fname})
        n += 1
        return Response(response=img_uri, status=200, mimetype="application/json")

    return Response(response="", status=400, mimetype="application/json")

if __name__ == "__main__":
    app.run(host="localhost", port=8052, debug=True)
