from HandStrategy import HandStrategy as Parent


class Paper(Parent):
    def play_against(self, handStrategy) :
        self.hand_result = {
            Rock:1,
            Scissor:-1,
            self.__class__: 0}

        return self.hand_result.get(handStrategy)          

