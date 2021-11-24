from PyQt5.QtCore import QCoreApplication
from PyQt5.QtMultimedia import QSound
import sys
from Constants import _Constants as constants


class _Audio:
   def playBackgroundMusic(self):
      self.__play(constants.BACKGROUND_MUSIC)
      self.sound.setLoops(20)
      self.sound.Loop()


   def playClickingSound(self):
      self.__play(constants.MOUSE_CLICK)
  
   def playGameOverSound(self):
      self.__play(constants.GAMEOVER_SOUND)

   def playLoseSound(self):
      self.__play(constants.LOSE_SOUND)

   def playDrawSound(self):
      self.__play(constants.DRAW_SOUND)

   def playVictorySound(self):
      self.__play(constants.VICTORY_SOUND) 

   def playWinSound(self):
      self.__play(constants.WIN_SOUND)

   def __play(self,file_name):
      self.sound = QSound(constants.SOUND_DIRECTORY + file_name + constants.SOUND_FILE_FORMAT)
      
      self.sound.play()
   
