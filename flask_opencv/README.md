### EDGE DETECTION API

##### This API takes as input image or url to an image, performs edge detection on the image and then return the image.

There are two ways to use this API:

### via a web interface.

Run `python flask_connexion.py` on your terminal to start the server and then open `http://127.0.0.1:5000/` on your browser.

![web_interface](https://github.com/Yodeman/iqube_projects/blob/main/flask_opencv/web_interface.png)

![output](https://github.com/Yodeman/iqube_projects/blob/main/flask_opencv/output.png)

### API

Here, the user sends a POST request to the server. Run `python server.py` on the terminal to start the server, request is to be sent to `http://localhost:8000/api/edge` the server expects a json data of the format `{'url':'url_of_image', 'file':'encoded image or {}-if no image file'}`. This [notebook](https://github.com/Yodeman/iqube_projects/blob/main/flask_opencv/consuming_api.ipynb) explains how to consume the api.
