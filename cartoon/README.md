
# CARTOON API
<p float="left">
    <img src="./sample3.png" width="320" height="250">
    <img src="./sample2.png" width="320" height="250">
    <img src="./sample1.png" width="320" height="250">
</p>

This API takes images from user and turns the uploaded image to cartoon.
The two supported endpoints are:
- **color**
- **grayscale**

        import requests, json, base64, io
        from PIL import Image
        
        addr = "https://paul-cartoon.herokuapp.com/grayscale"
        content_type = "multipart/form-data"
        headers = {"content-type":content_type}
        
        files = {"file":("lydia.jpg", open("./my_imgs/lydia.jpg", "rb"))}
        response = requests.post(addr, files=files)
        r = json.loads(response.text)
        
        img = r["img"].encode("ascii")
        img = base64.decodebytes(img)
        buffer_ = io.BytesIO(img)
        img = Image.open(buffer_)
        img.show()
