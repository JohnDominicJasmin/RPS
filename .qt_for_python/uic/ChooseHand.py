# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/miko/python/RPS/source/ChooseHand.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 768)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.paper_picture_big = QtWidgets.QLabel(self.centralwidget)
        self.paper_picture_big.setGeometry(QtCore.QRect(380, 20, 281, 331))
        self.paper_picture_big.setStyleSheet("\n"
"image: url(:/new/images/Paper.svg);")
        self.paper_picture_big.setText("")
        self.paper_picture_big.setPixmap(QtGui.QPixmap("/home/miko/python/RPS/source/python/Papel (1).svg"))
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
        self.rockButton = QtWidgets.QPushButton(self.centralwidget)
        self.rockButton.setGeometry(QtCore.QRect(270, 600, 161, 141))
        self.rockButton.setStyleSheet("image: url(:/new/images/rock_small.svg);")
        self.rockButton.setText("")
        self.rockButton.setObjectName("rockButton")
        self.rockButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.rockButton_2.setGeometry(QtCore.QRect(440, 600, 141, 141))
        self.rockButton_2.setStyleSheet("\n"
"\n"
"image: url(:/new/images/paper_small.svg);")
        self.rockButton_2.setText("")
        self.rockButton_2.setObjectName("rockButton_2")
        self.rockButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.rockButton_3.setGeometry(QtCore.QRect(590, 600, 131, 141))
        self.rockButton_3.setStyleSheet("image: url(:/new/images/scissor_small.svg);")
        self.rockButton_3.setText("")
        self.rockButton_3.setObjectName("rockButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_play.setText(_translate("MainWindow", "LET\'S PLAY!"))
        self.label_option.setText(_translate("MainWindow", "PICK AN OPTION:"))
import img_rc
