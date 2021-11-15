from GameStrategy import Game_Strategy as Parent
import Rock
import Scissor
from PyQt5 import QtCore, QtGui, QtWidgets
from images import ResourceImage
import MainMenu as mm
import ResultDialog
from Constants import _Constants as constants

class Hand_Paper(Parent):

    def play_against(self,handStrategy) :
        self.strategy = handStrategy
            

    def get_score(self):
        self.hand_result = {
            Rock.Hand_Rock:1,
            Scissor.Hand_Scissor:-1,
            __class__: 0}
        return self.hand_result.get(self.strategy)          


    def set_ui_result(self):
        self.window = QtWidgets.QMainWindow()
        self.hand_window = {
            Rock.Hand_Rock: ResultDialog.UI_ResultDialog(constants.WIN,constants.OPPONENT_ROCK,constants.PLAYER_PAPER),
            Scissor.Hand_Scissor:ResultDialog.UI_ResultDialog(constants.LOSE,constants.OPPONENT_SCISSOR,constants.PLAYER_PAPER),
            __class__: ResultDialog.UI_ResultDialog(constants.DRAW, constants.OPPONENT_PAPER,constants.PLAYER_PAPER)
            }

        self.ui = self.hand_window.get(self.strategy)
        self.ui.setupUi(self.window)    
        self.window.show()
