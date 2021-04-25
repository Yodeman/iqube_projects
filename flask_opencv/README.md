### EDGE DETECTION API

##### This API takes as input image or url to an image, performs edge detection on the image and then return the image.

There are two ways to use this API:

#### via a web interface.

Run `python flask_connexion.py` on your terminal to start the server and then open `http://127.0.0.1:5000/` on your browser.

#### API

Here, the user sends a POST request to the server. the server expects a json data of the format `{'url':'url_of_image', 'file':'encoded image or {}-if no image file'}`