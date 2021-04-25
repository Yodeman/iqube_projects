from flask import Flask, render_template, request, json, redirect, url_for
import connexion
import cv2
import os

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = ['.jpg', '.png']

app = Flask(__name__, static_url_path='/uploads', static_folder='uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return os.path.splitext(filename)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/uploads')
def render():
    #original = os.path.join(UPLOAD_FOLDER, 'original.jpg')
    #detected = os.path.join(UPLOAD_FOLDER, 'detected.jpg')
    return render_template('render.html')


@app.route('/edge', methods=["POST"])
def detect_edge():
    url = request.form['url']
    image = request.files['file']
    if url:
        cap = cv2.VideoCapture(url)
        retval, img = cap.read()
        if retval:
            cv2.imwrite(UPLOAD_FOLDER+'/original.jpg', img)
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img_edge = cv2.Canny(img_gray, 100, 200)
            cv2.imwrite(UPLOAD_FOLDER+'/detected.jpg', img_edge)
            return redirect(url_for('render'))

    elif image and allowed_file(image.filename):
        fname = UPLOAD_FOLDER+'/original.jpg'#+os.path.splitext(image.filename)[1]
        image.save(fname)
        img = cv2.imread(fname)
        if img is not None:
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img_edge = cv2.Canny(img_gray, 100, 200)
            cv2.imwrite(UPLOAD_FOLDER+'/detected.jpg', img_edge)
            return redirect(url_for('render'))


    return redirect(url_for('home'))
    #return help(request.files)

if __name__ == "__main__":
    app.run(debug=True)
