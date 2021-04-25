from flask import Flask, request, Response, render_template
import jsonpickle
import connexion
import numpy as np
import cv2

#app = Flask(__name__)
app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')

@app.route('/')
def home():
    return 'Welcome'

"""@app.route('/api/test', methods=['POST'])
def test():
    r = request

    nparr = np.fromstring(r.data, np.uint8)

    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    response = {'message':'Image recieved. Image size = {}x{}'.format(img.shape[0], img.shape[1])}

    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")"""

app.run(host='localhost', port=8000, debug=True)
