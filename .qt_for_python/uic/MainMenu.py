# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/miko/python/RPS/source/MainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1000, 768)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background:rgb(81, 81, 81)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 680, 291, 61))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background:rgb(206, 206, 206);\n"
"color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 330, 201, 321))
        self.label.setStyleSheet("image: url(:/new/images/Scissor.svg);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/home/miko/python/RPS/source/Tesoura (1).svg"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 40, 431, 171))
        font = QtGui.QFont()
        font.setFamily("Noto Serif Thin")
        font.setPointSize(35)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rock Paper Scissors"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.label_3.setText(_translate("MainWindow", "ROCK\n"
"/PAPER/\n"
"SCISSOR"))
import img_rc
