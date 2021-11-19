from PyQt5.QtCore import QCoreApplication
from PyQt5.QtMultimedia import QSound
import sys
from Constants import _Constants as constants
def playBackgroundMusic():
   __play(constants.BACKGROUND_MUSIC)

def playClickingSound():
   __play(constants.MOUSE_CLICK)

def playGameOverSound():
   __play(constants.GAMEOVER_SOUND)

def playLoseSound():
   __play(constants.LOSE_SOUND)

def playVictorySound():
   __play(constants.VICTORY_SOUND) 

def playWinSound():
   __play(constants.WIN_SOUND)

def __play(file_name):
    app = QCoreApplication(sys.argv)
    sound = QSound(constants.SOUND_DIRECTORY+file_name+constants.SOUND_FILE_FORMAT)
    sound.play()
    sys.exit(app.exec_())


playBackgroundMusic()