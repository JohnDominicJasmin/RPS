
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout, QWidget, QDesktopWidget, QPushButton
from PyQt5.QtCore import QRect
from screeninfo import get_monitors
from images import ResourceImage
from AbstractHandStrategy import Abstract_Strategy
import Rock
import Scissor
import Paper
import Enemy
from random import randint
from Audio import _Audio
import MainMenu
from GameUtils import Game_Utils
import OverallResultDialog as dialog_result
from Constants import _Constants


player = Game_Utils().Scores()
enemy = Game_Utils().Scores()              
rounds = Game_Utils().Rounds()


class ChooseHandWindow(object):

    def setupUi(self, MainWindow):  
        self.enemy = Enemy.Enemy_Hand
 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 768)
        MainWindow.setFixedSize(1000,768)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
    
        for m in get_monitors():
            screenHeight = m.height
            screenWidth = m.width
        MainWindow.setGeometry((screenWidth/2)-(1000/2),(screenHeight/2)-(768/2),1000,768)
        self.window = MainWindow
       
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.paper_picture_big = QtWidgets.QLabel(self.centralwidget)
        self.paper_picture_big.setGeometry(QtCore.QRect(380, 20, 281, 331))
        self.paper_picture_big.setStyleSheet("\n"
"image: url(:/new/images/Paper.svg);")
        self.paper_picture_big.setObjectName("paper_picture_big")

        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
    
        self.label_play = QtWidgets.QLabel(self.centralwidget)
        self.label_play.setGeometry(QtCore.QRect(390, 460, 251, 51))
        self.label_play.setFont(font)
        self.label_play.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_play.setAlignment(QtCore.Qt.AlignCenter)
        self.label_play.setObjectName("label_play")

        font = QtGui.QFont()
        font.setPointSize(13.5)
        font.setWeight(60)    

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
    
    
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setGeometry(QRect(5, 5, 31, 31))
        self.backButton.setStyleSheet(u"image: url(source/images/back.svg);")


        self.paperButton = QPushButton(self.centralwidget)
        self.paperButton.setObjectName(u"paperButton")
        self.paperButton.setGeometry(QRect(440, 600, 141, 141))
        self.paperButton.setStyleSheet(u"image: url(:/new/images/paper_small.svg);")
        
    
        self.win_label = QtWidgets.QLabel(self.centralwidget)
        self.win_label.setObjectName(u"win_label")
        self.win_label.setGeometry(QRect(90, 100, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.win_label.setFont(font)
        self.win_label.setStyleSheet(u"color: rgb(136, 134, 134);")
        self.win_label.setAlignment(QtCore.Qt.AlignCenter)
        self.win_score_label = QtWidgets.QLabel(self.centralwidget)
        self.win_score_label.setObjectName(u"win_score_label")
        self.win_score_label.setGeometry(QRect(110, 150, 58, 51))
        self.win_score_label.setFont(font)
        self.win_score_label.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.win_score_label.setAlignment(QtCore.Qt.AlignCenter)

        self.lose_score_label = QtWidgets.QLabel(self.centralwidget)
        self.lose_score_label.setObjectName(u"lose_score_label")
        self.lose_score_label.setGeometry(QRect(830, 140, 58, 51))
        self.lose_score_label.setFont(font)
        self.lose_score_label.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lose_score_label.setAlignment(QtCore.Qt.AlignCenter)

        self.rounds_label = QtWidgets.QLabel(self.centralwidget)
        self.rounds_label.setObjectName(u"rounds_label")
        self.rounds_label.setGeometry(QRect(440, 10, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.rounds_label.setFont(font)
        self.rounds_label.setStyleSheet(u"color: rgb(255, 15, 15);")
        self.rounds_label.setAlignment(QtCore.Qt.AlignCenter)



        self.rounds_label.setText("ROUND: "+str(rounds.getRounds()))
        self.win_score_label.setText(str(player.getScore()))     
        self.lose_score_label.setText(str(enemy.getScore()))
    


        self.lose_label = QtWidgets.QLabel(self.centralwidget)
        self.lose_label.setObjectName(u"lose_label")
        self.lose_label.setGeometry(QRect(820, 90, 81, 41))
        font1 = QtGui.QFont()
        font1.setPointSize(22)
        self.lose_label.setFont(font1)
        self.lose_label.setStyleSheet(u"color: rgb(136, 134, 134);")
        self.lose_label.setAlignment(QtCore.Qt.AlignCenter)
        self.scissorButton = QPushButton(self.centralwidget)
        self.scissorButton.setObjectName(u"scissorButton")
        self.scissorButton.setGeometry(QRect(590, 600, 131, 141))
        self.scissorButton.setStyleSheet(u"image: url(:/new/images/scissor_small.svg);")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def provide_click_listeners(self):
    
        self.scissorButton.clicked.connect(self.scissor_button_on_click)
        self.rockButton.clicked.connect(self.rock_button_on_click)
        self.paperButton.clicked.connect(self.paper_button_on_click)
        self.backButton.clicked.connect(self.back_button_on_click)

    def scissor_button_on_click(self):
        self.playAs(Scissor.Hand_Scissor)

    def rock_button_on_click(self):
        self.playAs(Rock.Hand_Rock)

    def paper_button_on_click(self):
        self.playAs(Paper.Hand_Paper)
    
    def back_button_on_click(self):
  
        self.open_main_menu_dialog()
        self.soundclicks = _Audio()
        self.soundclicks.playClickingSound()

    def open_draw_dialog(self):
        self.open_dialog(dialog_result.Ui_MainWindow(_Constants.TITLE_DRAW_RESULT,_Constants.DESCRIPTION_DRAW_RESULT))

    def open_main_menu_dialog(self):
        self.open_dialog(MainMenu.Ui_MainWindow())

    def open_win_dialog(self):  
        self.open_dialog(dialog_result.Ui_MainWindow(_Constants.TITLE_WIN_RESULT,_Constants.DESCRIPTION_WIN_RESULT))
        
    def open_lose_dialog(self):
        self.open_dialog(dialog_result.Ui_MainWindow(_Constants.TITLE_LOSE_RESULT,_Constants.DESCRIPTION_LOSE_RESULT))     
    

    def open_dialog(self, dialog):
        self.dialog_window = QtWidgets.QMainWindow()
        self.dialog_ui = dialog
        self.dialog_ui.setupUi(self.dialog_window)
        #provide listeners
        self.dialog_ui.provide_click_listeners()
        self.dialog_window.show()
        self.window.setVisible(False)


    def playAs(self,strategy):
        self.strategy = Abstract_Strategy(self.enemy.create_enemy())
        self.strategy.play_against(strategy)
        score = self.strategy.get_score()
        rounds.incrementRounds()
        self.open_result_ui()
        self.update_score(score)
        self.play_sound_accordingly(score)
        self.window.setVisible(False)


    def open_result_ui(self):

            if(rounds.getRounds() == _Constants.ROUND_LIMIT):
                self.open_dialog_result()
            else:
                self.strategy.set_ui_result()


    def open_dialog_result(self):

         if(player.getScore() > enemy.getScore()):
             self.open_win_dialog()
         if(player.getScore() < enemy.getScore()):
             self.open_lose_dialog()
         if(player.getScore() == enemy.getScore()):
             self.open_draw_dialog()

         player.score = 0
         enemy.score = 0
         rounds.reset()

        



    def update_score(self,score):
        if score == -1:
            enemy.addScore(1)
        else:
            player.addScore(score)
        

    def play_sound_accordingly(self, score):

        self.sound = _Audio()
        if score == -1:
            self.sound.playLoseSound()

        if score == 0:
            self.sound.playDrawSound()

        if score == 1:
            self.sound.playWinSound()



        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.win_label.setText(_translate("MainWindow", u"WIN", None))
        self.window.setWindowTitle(_translate("Dialog", "  "))
        self.lose_label.setText(_translate("MainWindow", u"LOSE", None))
        self.label_play.setText(_translate("MainWindow", "LET\'S PLAY!"))
        self.label_option.setText(_translate("MainWindow", "PICK AN OPTION:"))

   
