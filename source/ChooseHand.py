# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChooseHand.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout, QWidget, QDesktopWidget, QPushButton
from PyQt5.QtCore import QRect
from screeninfo import get_monitors
from images import ResourceImage
from AbstractHandStrategy import Abstract_Strategy
import Rock
import Scissor



class ChooseHandWindow(object):

    

    def setupUi(self, MainWindow):  
        self.strategy = Abstract_Strategy(Scissor.Hand_Scissor)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 768)
        MainWindow.setFixedSize(1000,768)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        for m in get_monitors():
            screenHeight = m.height
            screenWidth = m.width
        MainWindow.setGeometry((screenWidth/2)-(1000/2),(screenHeight/2)-(768/2),1000,768)
        MainWindow.setFixedSize(1000,768)
        
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.paper_picture_big = QtWidgets.QLabel(self.centralwidget)
        self.paper_picture_big.setGeometry(QtCore.QRect(380, 20, 281, 331))
        self.paper_picture_big.setStyleSheet("\n"
"image: url(:/new/images/Paper.svg);")
        self.paper_picture_big.setText("")
        self.paper_picture_big.setPixmap(QtGui.QPixmap("python/Papel (1).svg"))
        self.paper_picture_big.setObjectName("paper_picture_big")
        self.label_play = QtWidgets.QLabel(self.centralwidget)
        self.label_play.setGeometry(QtCore.QRect(390, 460, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.label_play.setFont(font)
        self.label_play.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_play.setAlignment(QtCore.Qt.AlignCenter)
        self.label_play.setObjectName("label_play")
        self.label_option = QtWidgets.QLabel(self.centralwidget)
        self.label_option.setGeometry(QtCore.QRect(440, 520, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_option.setFont(font)
        self.label_option.setStyleSheet("color: rgb(28, 28, 28);")
        self.label_option.setObjectName("label_option")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(300, 610, 431, 131))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.pictureshorizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.pictureshorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pictureshorizontalLayout.setObjectName("pictureshorizontalLayout")
        self.rockButton = QPushButton(self.centralwidget)
        self.rockButton.setObjectName(u"rockButton")
        self.rockButton.setGeometry(QRect(270, 600, 161, 141))
        self.rockButton.setStyleSheet(u"image: url(:/new/images/rock_small.svg);")
        self.paperButton = QPushButton(self.centralwidget)
        self.paperButton.setObjectName(u"paperButton")
        self.paperButton.setGeometry(QRect(440, 600, 141, 141))
        self.paperButton.setStyleSheet(u"\n"
"\n"
"image: url(:/new/images/paper_small.svg);")
        self.scissorButton = QPushButton(self.centralwidget)
        self.scissorButton.setObjectName(u"scissorButton")
        self.scissorButton.setGeometry(QRect(590, 600, 131, 141))
        self.scissorButton.setStyleSheet(u"image: url(:/new/images/scissor_small.svg);")
        self.scissorButton.clicked.connect(self.scissor_button_on_click)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def scissor_button_on_click(self):
        print(self.strategy.play_against(Rock.Hand_Rock))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_play.setText(_translate("MainWindow", "LET\'S PLAY!"))
        self.label_option.setText(_translate("MainWindow", "PICK AN OPTION:"))

   