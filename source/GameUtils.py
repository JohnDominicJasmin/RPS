

class Game_Utils():


    class Rounds():
        rounds = 0

        def getRounds(self):
            return self.rounds

        def incrementRounds(self):
            self.rounds += 1

        def reset(self):
            self.rounds = 0


    class Scores():

        score = 0
   
        def getScore(self):
            return self.score

   
        def addScore(self,scoreValue):
            self.score += scoreValue
        

        def reset(self):
            self.score = 0
        