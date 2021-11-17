from PyQt5.QtCore import QCoreApplication
from PyQt5.QtMultimedia import QSound
import sys

def playBackgroundMusic():
   __make_sound("bgm")


def playClickingSound():
   __make_sound("mouseclick")




def __make_sound(file_name):
    app = QCoreApplication(sys.argv)
    sound = QSound("source/sounds/"+file_name+".wav")
    sound.play()
    sys.exit(app.exec_())


playBackgroundMusic()