from GameStrategy import Game_Strategy as Parent
import Paper 
import Rock
import ResultDialog
from Constants import _Constants as constants
from PyQt5 import QtCore, QtGui, QtWidgets
from images import ResourceImage

class Hand_Scissor(Parent):
    

    def play_against(self,handStrategy) :
        self.strategy = handStrategy


    def get_score(self):
        self.hand_result = {
            Paper.Hand_Paper:1,
            Rock.Hand_Rock:-1,
            __class__:0
        }
        return self.hand_result.get(self.strategy)
    


    def set_ui_result(self):

        self.window = QtWidgets.QMainWindow()

        self.hand_window = {
            Paper.Hand_Paper: ResultDialog.UI_ResultDialog(constants.WIN,constants.OPPONENT_PAPER, constants.PLAYER_SCISSOR),
            Rock.Hand_Rock:ResultDialog.UI_ResultDialog(constants.LOSE, constants.OPPONENT_ROCK, constants.PLAYER_SCISSOR),
            __class__: ResultDialog.UI_ResultDialog(constants.DRAW, constants.OPPONENT_SCISSOR, constants.PLAYER_SCISSOR)
            }

        self.ui = self.hand_window.get(self.strategy)    
        self.ui.setupUi(self.window)
        self.window.show()