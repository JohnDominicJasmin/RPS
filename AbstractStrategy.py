class AbstractStrategy :
    def __init__(self, strategy) :
        self.strategy = strategy


    def  playAgainst(self, strategy) :
        return  self.strategy.play_against(strategy)