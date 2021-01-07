import sys
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QFont
import camera


def openImage():
    win = QMainWindow()
    img,_ = QFileDialog.getOpenFileName(win,"Open Image","~","Image Files (*.jpg *.png)")
    camera.runn(img)

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(500,500,500,400)
    win.setWindowTitle("Facial Expression")
    win.setStyleSheet("background-color : white;")

    lb3 = QtWidgets.QLabel(win)
    lb3.setGeometry(80,10,340,40)
    lb3.setText(" HCM University of Technology and Education")
    lb3.setFont(QFont('Times',17,QFont.Bold))
    



    
    lblogo2 = QtWidgets.QLabel(win)
    lblogo2.setGeometry(190,50,100,63)
    lblogo2.setStyleSheet("background-image : url(/Users/mac/Desktop/UTE/Image processing /workspace/faceDectection/Facial-Expression-Recognition-Challenge/img/newlogo-2.jpg)")

    b2 = QtWidgets.QPushButton(win)
    b2.setGeometry(200,150,100,63)
    button2 = b2.geometry()
    b2.setText("Import Picture")
    #b2.setStyleSheet("color : white)")
    #b2.setStyleSheet("background-image : url(/Users/mac/Desktop/newlogo-2.jpg)")
    print(button2)

    lb = QtWidgets.QLabel(win)
    lb.setGeometry(300,280,300,20)
    lb.setText("Dinh Van Truong - 18110060")
    #lb.setStyleSheet("border: 1.5px solid black;")
    lb.setFont(QFont('Times',13))

    lb2 = QtWidgets.QLabel(win)
    lb2.setGeometry(300,300,300,20)
    lb2.setText("Nguyen Hoang Vu - 18110398")
    #lb2.setStyleSheet("border: 1.5px solid black;")
    lb2.setFont(QFont('Times',13))

    lblogo = QtWidgets.QLabel(win)
    lblogo.setGeometry(330,320,50,50)
    #lblogo.setStyleSheet("background-image : url(/Users/mac/Desktop/logo3-2.jpg)")


   
    


    

    b2.clicked.connect(openImage)
    

    win.show()
    app.exec()


window()