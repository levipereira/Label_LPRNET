# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap, QFont, QKeySequence
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QWidget,QApplication, QMainWindow
import os
import glob

pathDir = None
pathDir_images = None
pathDir_labels = None
image_list = []
index = 0
curentid = -1
zoom = 1

help_txt = "Keyboard shortcuts \n\nNEXT : KEY UP \nBACK: KEY DOWN \nDELETE: PAGE DOWN \n"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(991, 400)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.btBrowse = QtWidgets.QPushButton(self.centralWidget)
        self.btBrowse.setGeometry(QtCore.QRect(30, 10, 99, 27))
        self.btBrowse.setCheckable(False)
        self.btBrowse.setObjectName("btBrowse")

        self.lbText = QtWidgets.QLabel(self.centralWidget)
        self.lbText.setGeometry(QtCore.QRect(240, 10, 200, 35))
        self.lbText.setObjectName("lbText")

        self.txtHelp = QtWidgets.QLabel(self.centralWidget)
        self.txtHelp.setGeometry(QtCore.QRect(580, 200, 180, 180))
        self.txtHelp.setObjectName("txtHelp")
        
        
        self.lbImage = QtWidgets.QLabel(self.centralWidget)
        self.lbImage.setGeometry(QtCore.QRect(30, 110, 531, 192))
        self.lbImage.setObjectName("lbImage")
        self.lbImage.setStyleSheet("border: 2px solid blue");

        self.tbEdit = QtWidgets.QLineEdit(self.centralWidget)
        #self.tbEdit.setGeometry(QtCore.QRect(580, 100, 381, 51))
        self.tbEdit.setGeometry(QtCore.QRect(30, 50, 381, 51))
        self.tbEdit.setObjectName("tbEdit")
        self.tbEdit.setFont(QFont("Times",15))

        self.btBack = QtWidgets.QPushButton(self.centralWidget)
        self.btBack.setGeometry(QtCore.QRect(580, 180, 99, 27))
        self.btBack.setObjectName("btBack")

        self.btNext = QtWidgets.QPushButton(self.centralWidget)
        self.btNext.setGeometry(QtCore.QRect(720, 180, 99, 27))
        self.btNext.setObjectName("btNext")

        self.btDelete = QtWidgets.QPushButton(self.centralWidget)
        self.btDelete.setGeometry(QtCore.QRect(860, 180, 99, 27))
        self.btDelete.setObjectName("btDelete")

        self.btZoomIn = QtWidgets.QPushButton(self.centralWidget)
        #self.btZoomIn.setGeometry(QtCore.QRect(30, 330, 99, 27))
        self.btZoomIn.setGeometry(QtCore.QRect(580, 110, 99, 27))
        self.btZoomIn.setObjectName("btZoomIn")

        self.btZoomOut = QtWidgets.QPushButton(self.centralWidget)
        #self.btZoomOut.setGeometry(QtCore.QRect(170, 330, 99, 27))
        self.btZoomOut.setGeometry(QtCore.QRect(720, 110, 99, 27))
        self.btZoomOut.setObjectName("btZoomOut")


        MainWindow.setCentralWidget(self.centralWidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Label LPRNET"))
        self.btBrowse.setText(_translate("MainWindow", "Browse"))
        self.btBrowse.clicked.connect(self.Browse)
        

        self.lbText.setText(_translate("MainWindow", "None")    )

        self.txtHelp.setText(_translate("MainWindow", help_txt)    )
        
        
        self.btBack.setText(_translate("MainWindow", "Back"))
        self.btBack.clicked.connect(self.Back)
        
        self.btNext.setText(_translate("MainWindow", "Next"))
        self.btNext.clicked.connect(self.Next)
        
        self.btDelete.setText(_translate("MainWindow", "Delete"))
        self.btDelete.clicked.connect(self.Delete)

        self.btZoomIn.setText(_translate("MainWindow", "Zoom++"))
        self.btZoomIn.clicked.connect(self.ZoomIn)
        self.btZoomOut.setText(_translate("MainWindow", "Zoom--"))
        self.btZoomOut.clicked.connect(self.ZoomOut)
        self.tbEdit.textChanged.connect(self.TextChanged)

    def manage_last_session(self, set_index):
        global pathDir,index
        
        path_last_session = os.path.join(pathDir, '.last_session' ) 
        if os.path.exists(path_last_session):
            if set_index:
                file_last_session = open(path_last_session, "w")
                index_data = [str(index)]
                file_last_session.writelines(index_data)
                file_last_session.close()
            else:
                file_last_session = open(path_last_session, "r")
                index_data = file_last_session.readlines()
                if index_data[0].isnumeric():
                    index=int(index_data[0])
                file_last_session.close()

        else:
            file_last_session = open(path_last_session, "w")
            index_data= [str(index)]
            file_last_session.writelines(index_data)
            file_last_session.close()

    def Browse(self,MainWindow):
        global pathDir,pathDir_images,pathDir_labels, image_list,index,curentid
        pathDir = None
        image_list = []
        curentid = -1
        self.lbText.setText("None")
        self.tbEdit.setText("")
        self.lbImage.clear()
        pathDir = os.path.normpath(QtWidgets.QFileDialog.getExistingDirectory(self.centralWidget))
        pathDir_images=os.path.join(pathDir, "image")
        pathDir_labels=os.path.join(pathDir, "label")
        try:
            for ext in ('*.jpeg', '*.png', '*.jpg'):
                image_list.extend(glob.glob(os.path.join(pathDir_images, ext)))
        except:
            pass
        image_list = sorted(image_list, key=os.path.basename)
        if len(image_list):
            self.manage_last_session(False)
            if len(image_list)-1 < index :
                index = 0 
            self.loadData(image_list[index])
    
    def Reload_Dir(self,MainWindow):
        global pathDir,pathDir_images,pathDir_labels,image_list,index,curentid
        pathDir = None
        image_list = []
        curentid = -1
        self.lbText.setText("None")
        self.tbEdit.setText("")
        self.lbImage.clear()
        try:
            for ext in ('*.jpeg', '*.png', '*.jpg'):
                image_list.extend(glob.glob(os.path.join(pathDir_images, ext)))
        except:
            pass
        
        if len(image_list):
            self.manage_last_session(False)
            if len(image_list)-1 < index :
                index = 0 
            self.loadData(image_list[index])

    def Next(self,MainWindow):
        global image_list,index
        if(len(image_list)) :
            text =self.tbEdit.text().rstrip()
            base_txt=os.path.basename(image_list[index])
            pre_txt_path=os.path.join(pathDir_labels, str(os.path.splitext(base_txt)[0])+".txt")
            #pre_txt_path = image_list[index][:-3]+'txt'
            open(pre_txt_path,'w',encoding="utf-8").write(text.upper())
            if index<len(image_list)-1:
                index+=1
            self.manage_last_session(True)
            self.loadData(image_list[index])

    def Back(self,MainWindow):
        global image_list,index
        if(len(image_list)) :
            text =self.tbEdit.text().rstrip()
            base_txt=os.path.basename(image_list[index])
            pre_txt_path=os.path.join(pathDir_labels, str(os.path.splitext(base_txt)[0])+".txt")
            #pre_txt_path = image_list[index][:-3]+'txt'

            open(pre_txt_path,'w',encoding="utf-8").write(text.upper())
            if index>0:
                index-=1
            self.manage_last_session(True)
            self.loadData(image_list[index])

    def Delete(self,MainWindow):
        global image_list,index
        if (len(image_list)) :
            file_img=image_list[index]
            base_txt=os.path.basename(image_list[index])
            file_txt=os.path.join(pathDir_labels, str(os.path.splitext(base_txt)[0])+".txt")
            #file_txt=str(os.path.splitext(image_list[index])[0])+".txt"
            if file_img is not None:
                if os.path.exists(file_img):
                    os.remove(file_img)
            if file_txt is not None:
                if os.path.exists(file_txt):
                    os.remove(file_txt)
            image_list.pop(index)
            
            if (len(image_list)):
                if (len(image_list)-1) < index:
                    index=len(image_list)-1
                self.manage_last_session(True)
                self.loadData(image_list[index])
            else:
                self.manage_last_session(False)
                self.Reload_Dir(self)

    def ZoomIn(self,MainWindow):
        global zoom,image_list,index
        if(len(image_list)) :
            if zoom < 10 :
                zoom += 1
                image = QImage(image_list[index])
                ratio = max(1,max(image.width()/self.lbImage.frameGeometry().width(),image.height()/self.lbImage.frameGeometry().height()))
                image = image.scaled(int(zoom*image.width()/ratio),int(zoom*image.height()/ratio))
                pixmap = QPixmap().fromImage(image)
                self.lbImage.setPixmap(pixmap)

    def ZoomOut(self,MainWindow):
        global zoom,image_list,index
        if(len(image_list)) :
            if zoom > 1 :
                zoom -= 1
                image = QImage(image_list[index])
                ratio = max(1,max(image.width()/self.lbImage.frameGeometry().width(),image.height()/self.lbImage.frameGeometry().height()))
                image = image.scaled(int(zoom*image.width()/ratio),int(zoom*image.height()/ratio))
                pixmap = QPixmap().fromImage(image)
                self.lbImage.setPixmap(pixmap)

    def TextChanged(self,MainWindow):
        global curentid,index
        if len(image_list) and  curentid==index :
            text =self.tbEdit.text().rstrip()
            base_txt=os.path.basename(image_list[index])
            pre_txt_path=os.path.join(pathDir_labels, str(os.path.splitext(base_txt)[0])+".txt")
            #pre_txt_path = image_list[index][:-3]+'txt'
            open(pre_txt_path,'w',encoding="utf-8").write(text.upper())

    def loadData(self,img_path):
        global w,zoom,curentid,index,pathDir_labels
        zoom = 2 #reset zoom
        base_txt=os.path.basename(image_list[index])
        txt_path=os.path.join(pathDir_labels, str(os.path.splitext(base_txt)[0])+".txt")
        #txt_path = img_path[:-3]+'txt'
        text=str(index+1) + " of " + str(len(image_list)) + "\n" + str(os.path.basename(img_path))
        self.lbText.setText(text)
        image = QImage(img_path)
        ratio = max(1,max(image.width()/self.lbImage.frameGeometry().width(),image.height()/self.lbImage.frameGeometry().height()))
        #image = image.scaled(int(image.width()/ratio),int(image.height()/ratio))
        image = image.scaled(int(zoom*image.width()/ratio),int(zoom*image.height()/ratio))
        pixmap = QPixmap().fromImage(image)
        self.lbImage.setPixmap(pixmap)
        if os.path.exists(txt_path):
            self.tbEdit.setText(open(txt_path, "r",encoding="utf-8").read().rstrip())
        else:
            self.tbEdit.setText("")
        self.tbEdit.setFocus()
        curentid=index

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Up:
            self.Next(self)
        if e.key() == Qt.Key_Down:
            self.Back(self)
        if e.key() == Qt.Key_PageDown:
            self.Delete(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

