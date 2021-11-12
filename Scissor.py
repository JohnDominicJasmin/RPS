from HandStrategy import HandStrategy as Parent

class Scissor(Parent):
    def play_against(self, handStrategy) :
        self.hand_result = {}