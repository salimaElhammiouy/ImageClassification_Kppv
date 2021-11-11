# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 18:16:03 2021

@author: pc
"""


from sklearn.datasets import * # chargement du package datasets contenant plusieurs jeu de données
import pandas as pd # Chargement de Pandas
import matplotlib.pyplot as plt # import de Matplotlib
import numpy as np
from sklearn.model_selection import train_test_split # classe utilitaire pour découper les jeux de données
from sklearn.neighbors import KNeighborsClassifier # import de la classe de K-NN
from PyQt5.QtWidgets import (QMainWindow,QComboBox, QTextEdit, QVBoxLayout, QPushButton, QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PIL.ImageQt import ImageQt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PIL import Image


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
       
        #*********Button**
        
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(900, 200, 181, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton"
                                      "{"
                                      "background-color : rgb(255, 85, 127);"
                                      "}"
                                      "QPushButton::pressed"
                                      "{"
                                      "background-color:white;"
                                      "}"
                                      )
        
        
        
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(900, 300, 181, 31))
        self.pushButton2.setObjectName("pushButton")
        self.pushButton2.setStyleSheet("QPushButton"
                                      "{"
                                      "background-color : rgb(255, 85, 127);"
                                      "}"
                                      "QPushButton::pressed"
                                      "{"
                                      "background-color:white;"
                                      "}"
                                      )
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(900, 250, 181, 31))
        self.pushButton3.setObjectName("pushButton")
        self.pushButton3.setStyleSheet("QPushButton"
                                      "{"
                                      "background-color : rgb(255, 85, 127);"
                                      "}"
                                      "QPushButton::pressed"
                                      "{"
                                      "background-color:white;"
                                      "}"
                                      )
        #****** label *****
        self.ImageOrigine = QtWidgets.QLabel(self.centralwidget)
        self.ImageOrigine.setGeometry(QtCore.QRect(410, 140, 100, 100))
        self.ImageOrigine.setText("")
        self.ImageOrigine.setObjectName("label_3")
        
        self.ImageOrigine.setStyleSheet("background-color:rgb(255, 85, 127) ;")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 50, 911, 21))
        font=QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(100, 300, 851, 231))
        self.label_7.setText("Veuillez choisir votre image aprés avoir lancer l'aprentissage")
        self.label_7.setObjectName("label_7")
        font=QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        #*****line for sperate **
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(100, 100, 800, 561))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
    
       
        
       
        self.pushButton.clicked.connect(self.apprentissage)
        self.pushButton2.clicked.connect(self.test)
        self.pushButton3.clicked.connect(self.inputdial)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reconnaissance des Images KPPV "))
               
        self.pushButton.setText(_translate("MainWindow", "apprentissage"))
        self.pushButton2.setText(_translate("MainWindow", "Tester"))
        self.pushButton3.setText(_translate("MainWindow", "Choisir l'image de test"))
        self.label.setText(_translate("MainWindow", "Image à testé:"))
    def inputdial(self):
        #**********input***
        self.value, self.done = QtWidgets.QInputDialog.getInt(
        self.centralwidget, 'Image de test', 'choisissez de 1347:1797') 
        fig = Figure(figsize=(5, 4), dpi=100)
        self.displayImage(self.value)
        sc=plt.imshow(data_digit['images'][self.value], cmap='Greys_r')
        image1 = Image.fromarray(np.uint8( sc.get_cmap()(sc.get_array())*255))
        if (self.done):
            qimage = ImageQt(image1)
            pixmap = QtGui.QPixmap.fromImage(qimage)
            pixmap5 = pixmap.scaled(100, 100,QtCore.Qt.KeepAspectRatio)
            self.ImageOrigine.setPixmap(pixmap5)
          
            

    def apprentissage(self):
          KNN.fit(x_train, y_train)
          print("apprentissage done !!")
    
         
    def displayImage(self,i):
           plt.imshow(data_digit['images'][i], cmap='Greys_r')
           plt.show()

    def test(self):
    #Afficher un élement de la matrice format image 
           print(KNN.score(x_test,y_test))
           test = np.array(data_digit['data'][self.value])
           test1 = test.reshape(1,-1)
    #prédiction 
           k=KNN.predict(test1)
           print(k)
           self.label_7.setText("le chiffre est bien : =====> "+str(k))



if __name__ == "__main__":
    import sys
    #Affichage de jeu de données 
    data_digit = load_digits() # chargement du dataset MNIST predefinie dans sklearn
    
    
    # Création d'un dataframe Panda 1797 image en totale
    dig = pd.DataFrame(data_digit['data'][0:1797])
    dig.head() 
    data_digit.keys()
    
    train_x = data_digit.data
    train_y =  data_digit.target
    x_train,x_test,y_train,y_test=train_test_split(train_x,train_y,test_size=0.25,shuffle=False)
    KNN = KNeighborsClassifier(7,weights='distance', algorithm='kd_tree',p=1, metric='minkowski')
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_()) 
    







