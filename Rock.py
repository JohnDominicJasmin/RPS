from HandStrategy import HandStrategy as Parent
from Paper import Paper
from Scissor import Scissor



class Rock(Parent):
    def play(self,handStrategy):
        self.hand_result = {
            Scissor:1,
            Paper:-1,
            self.__class__:0}
        return self.hand_result.get(handStrategy)    

