import os
import json
import wordcloud as wc
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/generate', methods=["POST"])
def generate():
    word_cloud = wc.WordCloud()
    r = json.loads(request.data)
    text = r.get("text", None)
    if text:
        fname = "sample.jpg"
        word_cloud.generate(text)
        word_cloud.to_file(fname)
        img_uri = json.dumps({"URL":os.path.join(os.getcwd(), fname)})
        return Response(response=img_uri, status=200, mimetype="application/json")

    return Response(response="", status=200, mimetype="application/json")

if __name__ == "__main__":
    app.run(host="localhost", port=8052, debug=True)
