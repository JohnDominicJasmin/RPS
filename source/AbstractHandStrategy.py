
import GameStrategy as Interface

class Abstract_Strategy :

    def __init__(self, strategy) :
        self.strategy = strategy


    def play_against(self, strategy) :
        self.strategy.play_against(strategy)


    def get_score(self):
        return self.strategy.get_score()


    def set_ui_result(self):
        self.strategy.set_ui_result()    