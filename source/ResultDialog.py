
from PyQt5 import QtCore, QtGui, QtWidgets
from images import ResourceImage
from screeninfo import get_monitors
from Constants import _Constants as constants
from Audio import _Audio
import ChooseHand 


class UI_ResultDialog(object):

    def __init__(self,label_text,picture_opponent,picture_player):
      self.label_text = label_text
      self.picture_opponent = picture_opponent
      self.picture_player = picture_player



    def setupUi(self, MainWindow):

        MainWindow.resize(1000, 768)
        MainWindow.setFixedSize(1000,768)
        self.result_text = QtWidgets.QLabel(MainWindow)
        self.result_text.setGeometry(QtCore.QRect(400, 320, 191, 41))
        for m in get_monitors():
          screenHeight = m.height
          screenWidth = m.width
        MainWindow.setGeometry((screenWidth/2)-(1000/2),(screenHeight/2)-(768/2),1000,768)
        MainWindow.setStyleSheet("background-color:rgb(255, 255, 255)")
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.window = MainWindow
        self.result_text.setFont(font)
        self.result_text.setAlignment(QtCore.Qt.AlignCenter)
        self.result_text.setStyleSheet("color:rgb(0,0,0)")
        self.push_button_play_again = QtWidgets.QPushButton(MainWindow)
        self.push_button_play_again.setGeometry(QtCore.QRect(335, 372, 320, 60))
        self.push_button_play_again.setStyleSheet("color:rgb(0,0,0)")
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.push_button_play_again.setFont(font)
        self.push_button_play_again.clicked.connect(self.open_choose_hand_window)
        self.label_picture_player = QtWidgets.QLabel(MainWindow)
        self.label_picture_player.setGeometry(QtCore.QRect(390, 436, 201, 350)) 
        self.label_picture_player.setStyleSheet(self.picture_player)

        self.label_picture_opponent = QtWidgets.QLabel(MainWindow)
        self.label_picture_opponent.setGeometry(QtCore.QRect(400, -25, 201, 350))
        self.label_picture_opponent.setStyleSheet(self.picture_opponent)
   

   
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
       

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.result_text.setText(_translate("Dialog", self.label_text))
        self.push_button_play_again.setText(_translate("Dialog", "PLAY AGAIN"))
    
    def open_choose_hand_window(self):
        self.windows2 = QtWidgets.QMainWindow()
        self.ui = ChooseHand.ChooseHandWindow()
        self.ui.setupUi (self.windows2)
        self.ui.provide_click_listeners()
        self.soundclicks = _Audio()
        self.soundclicks.playClickingSound()
        self.windows2.show()
        self.window.close()

