import os
import torch
import cv2 as cv
import numpy as np
from facenet_pytorch import MTCNN, InceptionResnetV1

def get_frame(cap):
    """
    Capture image frm webcam
    """
    ret, frame = cap.read()
    if ret: return frame

def img_to_encoding(img, model):
    """
    Convert image to features vector.
    """
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img_tensor = torch.from_numpy(img).to(torch.float32)
    img_tensor = img_tensor.permute(2, 0, 1)[:3]
    encoding = model(img_tensor.unsqueeze(0))

    return encoding

def init_database(dbase, model):
    """
    Initialise the system database.
    """
    for img in os.listdir("./dataset"):
        print(img)
        employee = img.split('.')[0]
        img_arr = cv.imread("./dataset/"+img, cv.IMREAD_COLOR)
        dbase[employee] = img_to_encoding(img_arr, model)

def verify(name, img, dbase, model):
    """
    Check if the image detected by the system matches what the
    entity in front of the system claims.

    Returns: real if there is a match and color encoding
             fake if the images do not match and color encoding
    """
    encoding = img_to_encoding(img, model)

    #compute distance between detected image and real image
    diff = encoding - dbase[name]
    dist = np.linalg.norm(diff.detach().numpy())
    print(dist)

    if dist < 0.2:
        return "real", (0, 255, 255)

    return "fake", (0, 0, 255)
    
def main(cap, cnn, name, dbase, model):
    n = 0
    while True:
        frame = get_frame(cap)
        boxes, probs = cnn.detect(frame, landmarks=False)
        if isinstance(boxes, np.ndarray):
            x1, y1, x2, y2 = boxes[0].astype(int)
            x1 -= 50; y1 -= 40; x2 += 30; y2 += 40
            if n > 20:
                cropped = frame[y1:y2, x1:x2]
                text, color = verify(name, cropped, dbase, model)
                t_size = cv.getTextSize(text, cv.FONT_HERSHEY_PLAIN, 1, 1)[0]
                cv.putText(frame, text,
                    (x1, y1+t_size[1]+4), cv.FONT_HERSHEY_PLAIN, 1, color, 2
                )
            cv.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0),  2, 8, 0)
        cv.imshow("WebCam", frame)
        n += 1

        c = cv.waitKey(5)
        if c==27:
            break

if __name__ == "__main__":
    name = input("Please enter your registered name: ")
    dbase = {}
    cap = cv.VideoCapture(0)
    mtcnn = MTCNN(keep_all = True)
    resnet = InceptionResnetV1(pretrained='vggface2').eval()
    init_database(dbase, resnet)
    main(cap, mtcnn, name, dbase, resnet)
