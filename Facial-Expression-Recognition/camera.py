import cv2
from model import FacialExpressionModel
import numpy as np
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

"rgb = cv2.VideoCapture(0)"
facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_SIMPLEX

def __get_data__(fname):
    """
    __get_data__: Gets data from the VideoCapture object and classifies them
    to a face or no face. 
    
    returns: tuple (faces in image, frame read, grayscale frame)
    """
    
    fr = cv2.imread(fname)
  
    gray = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
    faces = facec.detectMultiScale(gray, 1.3, 5)
    
    return faces, fr, gray

def start_app(cnn,fname):
    skip_frame = 10
    data = []
    flag = False
    ix = 0
    while True:
        ix += 1
        
        faces, fr, gray_fr = __get_data__(fname)
        for (x, y, w, h) in faces:
            fc = gray_fr[y:y+h, x:x+w]
            
            roi = cv2.resize(fc, (48, 48))
            pred = cnn.predict_emotion(roi[np.newaxis, :, :, np.newaxis])

            cv2.putText(fr, pred, (x, y), font, 1, (255, 255, 0), 2)
            cv2.rectangle(fr,(x,y),(x+w,y+h),(255,0,0),2)

        if cv2.waitKey(1) == 27:
            break
        cv2.imshow('Filter', fr)
    cv2.destroyAllWindows()
def runn(fname):
    model = FacialExpressionModel("face_model.json", "face_model.h5")
    start_app(model,fname)
    

if __name__ == '__main__':
    pass
    # app = QApplication(sys.argv)
    # win = QMainWindow()
   
    # b1 = QtWidgets.QPushButton(win)
    # b1.setGeometry(50,50,100,100)
    # button1 = b1.geometry()
    # b1.setText("run")
    # b1.clicked.connect(runn())
    # print(button1)

    # win.show()
    # app.exec()
    
    #start_app(model)