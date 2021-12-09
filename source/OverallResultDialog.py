


from PyQt5 import QtCore, QtGui, QtWidgets
from screeninfo import get_monitors
import MainMenu

class Ui_MainWindow(object):



    def __init__(self,title,description):
        self.title = title
        self.description = description

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(847, 469)
        MainWindow.setFixedSize(847,469)
        MainWindow.setWindowTitle("")
        MainWindow.setStyleSheet("background-color: rgb(72, 72, 72);")
        for m in get_monitors():
          screenHeight = m.height
          screenWidth = m.width
        MainWindow.setGeometry((screenWidth/2)-(847/2),(screenHeight/2)-(469/2),847,469)
        self.window = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 30, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 130, 641, 171))
        font = QtGui.QFont()
        font.setPointSize(75)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 360, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(194, 194, 194);\n"
"color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.provide_click_listeners()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def provide_click_listeners(self):
        self.pushButton.clicked.connect(self.__open_main_menu)
       
    def __open_main_menu(self):
        self.dialog_window = QtWidgets.QMainWindow()
        self.dialog_ui = MainMenu.Ui_MainWindow()
        self.dialog_ui.setupUi(self.dialog_window)
        self.dialog_window.show()
        self.window.setVisible(False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", self.title))
        self.label_2.setText(_translate("MainWindow", self.description))
        self.pushButton.setText(_translate("MainWindow", "Ok"))



