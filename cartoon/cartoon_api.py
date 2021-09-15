import os, io, base64, cloudinary
import numpy as np
import cv2 as cv
from cloudinary.uploader import upload
from datetime import datetime
from PIL import Image
from flask import Flask, request, Response, json
from app.cartoonizer import cartoonize, gray_cartoon

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10*1024*1024
cloudinary.config(
    cloud_name="anonymouspo",
    api_key = "448685946715782",
    api_secret = "Qs7buIA0kvqsg7fh8XJyG4E3RU8",
    secure=True,
)

def load_file(file, fname):
    if fname.rsplit('.')[1].lower() in ('png', 'jpg', 'jpeg'):
        #Convert image to cartoon
        img = Image.open(file)
        img_arr = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
        return img_arr
    return ""

def encode_img(img):
    """
    Encode image into base64
    """
    #encode the image
    cart = Image.fromarray(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    cart_arr = io.BytesIO()
    cart.save(cart_arr, format="PNG")
    encoded_img = base64.b64encode(cart_arr.getvalue()).decode("ascii")
    return encoded_img


@app.route('/color', methods=['POST'])
def color():
    file = request.files['file']
    fname = file.filename
    img_arr = load_file(file, fname)
    if isinstance(img_arr, np.ndarray):
        cart = Image.fromarray(cv.cvtColor(img_arr, cv.COLOR_BGR2RGB))
        img_fname = f"{datetime.now().microsecond}_{fname}"
        cart.save(img_fname)
        upload(img_fname, public_id=img_fname)
        os.remove("./"+img_fname)
        
        cart = cartoonize(img_arr)
        encoded_img = encode_img(cart)
        return Response(
               response=json.dumps({"img":encoded_img, "warning":""}),
               status=200,
               mimetype="application/json"
               )
    else:
        return Response(
                response=json.dumps(
                    {"img":"",
                    "warning":"Error, Could not process file. Ensure file is in right format."
                    }),
                status=400,
                mimetype="application/json"
                )
@app.route("/grayscale", methods=["POST"])
def grayscale():
    file = request.files['file']
    fname = file.filename
    img_arr = load_file(file, fname)
    if isinstance(img_arr, np.ndarray):
        cart = Image.fromarray(cv.cvtColor(img_arr, cv.COLOR_BGR2RGB))
        img_fname = f"{datetime.now().microsecond}_{fname}"
        cart.save(img_fname)
        upload(img_fname, public_id=img_fname)
        os.remove("./"+img_fname)
        cart = gray_cartoon(img_arr)
        encoded_img = encode_img(cart)
        return Response(
               response=json.dumps({"img":encoded_img, "warning":""}),
               status=200,
               mimetype="application/json"
               )
    else:
        return Response(
                response=json.dumps(
                    {"img":"",
                    "warning":"Error, Could not process file. Ensure file is in right format."
                    }),
                status=400,
                mimetype="application/json"
                )

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
