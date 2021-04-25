from flask import request, json, Response
import jsonpickle
import cv2
import numpy as np

def detect(image):
    r = jsonpickle.decode(request.data)
    url = r.get('url', None)
    img = r.get('file', None)
    if url:
        cap = cv2.VideoCapture(url)
        retval, img = cap.read()
        if retval:
            #cv2.imwrite(UPLOAD_FOLDER+'/original.jpg', img)
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img_edge = cv2.Canny(img_gray, 100, 200)
            _, img_encode = cv2.imencode('.jpg', img_edge)
            response_pickled = jsonpickle.encode({'output':img_encode.tostring()})
            return Response(response=response_pickled, status=200, mimetype="application/json")
    elif img:
        nparr = np.fromstring(img, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_edge = cv2.Canny(img_gray, 100, 200)
        _, img_encode = cv2.imencode('.jpg', img_edge)
        response_pickled = jsonpickle.encode({'output':img_encode.tostring()})
        return Response(response=response_pickled, status=200, mimetype="application/json")
    
    return Response(response=jsonpickle.encode({'output':''}), status=404, mimetype="application/json")
