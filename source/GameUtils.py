

class Game_Utils():

    score = 0
    rounds = 0

    def getScore(self):
        return self.score

    def getRounds(self):
        return self.rounds

    def incrementRounds(self):
        self.rounds += 1

    def setScore(self,scoreValue):
        self.score += scoreValue
        

