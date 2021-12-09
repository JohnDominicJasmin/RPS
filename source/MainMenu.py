

from PyQt5 import QtCore, QtGui, QtWidgets
from images import ResourceImage
from screeninfo import get_monitors
import ChooseHand
from Audio import _Audio


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1000, 768)
        MainWindow.setFixedSize(1000,768)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background:rgb(81, 81, 81)")
        for m in get_monitors():
          screenHeight = m.height
          screenWidth = m.width
        MainWindow.setGeometry((screenWidth/2)-(1000/2),(screenHeight/2)-(768/2),1000,768)
        self.window = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 680, 291, 61))
        self.startButton = self.pushButton
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background:rgb(206, 206, 206);\n"
"color: rgb(0, 0, 0);")
        self.startButton.setObjectName("startButton")
  
     
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 330, 201, 321))
        self.label.setStyleSheet("image: url(:/new/images/Scissor.svg);")
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
        self.pushButton.clicked.connect(self.open_choose_hand_window)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rock Paper Scissors"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.label_3.setText(_translate("MainWindow", "ROCK\n"
"/PAPER/\n"
"SCISSOR"))

    def provide_click_listeners(self):
        self.pushButton.clicked.connect(self.open_choose_hand_window)

    def open_choose_hand_window(self):
        self.windows2 = QtWidgets.QMainWindow()
        self.ui = ChooseHand.ChooseHandWindow()
        self.ui.setupUi (self.windows2)
        self.ui.provide_click_listeners()
        self.soundclicks = _Audio()
        self.soundclicks.playClickingSound()
        self.windows2.show()  
        self.window.setVisible(False)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    sound = _Audio()
    sound.playBackgroundMusic()
    ui.setupUi(MainWindow)
    ui.provide_click_listeners()
    MainWindow.show()
 
    sys.exit(app.exec_())
