#This is based on 
#https://sites.google.com/site/unclebobconsultingllc/home/articles/the-bowling-game-an-example-of-test-first-pair-programming
#Ported from Java to see if I could translate it into Python.

class Game:
    def __init__(self):
        self.itsScorer = Scorer()

    def score(self):
        return self.scoreForFrame(self.itsCurrentFrame)

    def add(self, pins):
        self.itsScorer.addThrow(pins)
        self.adjustCurrentFrame(pins);

    def adjustCurrentFrame(self, pins):
        if(self.firstThrowInFrame == True):
            if(self.adjustFrameForStrike(pins) == False):
                self.firstThrowInFrame = False
            else:
                self.firstThrowInFrame = True
                self.advanceFrame()

    def adjustFrameForStrike(self, pins):
        if(pins == 10):
            self.advanceFrame()
            return True
        
        return False

    def advanceFrame(self):
        self.itsCurrentFrame = min([10, self.itsCurrentFrame + 1])

    def scoreForFrame(self, theFrame):
        return self.itsScorer.scoreForFrame(theFrame)

    itsCurrentFrame = 0
    firstThrowInFrame = True
    itsScorer = None

class Scorer:
    ball = 0
    itsThrows = [0] * 21
    itsCurrentThrow = 0

    def addThrow(self, pins):
        self.itsThrows[self.itsCurrentThrow] = pins
        self.itsCurrentThrow += 1

    def scoreForFrame(self, theFrame):
        ball = 0
        score = 0
        for currentFrame in range(0, theFrame):
            if(self.strike()):
                score += 10 + self.nextTwoBalls()
            elif(self.spare()):
                score += 10 + self.nextBall()
            else:
                score += self.twoBallsInFrame()

        return score

    def strike(self):
        if(self.itsThrows[self.ball] == 10):
            self.ball += 1
            return True

        return False

    def spare(self):
        if(self.itsThrows[self.ball] + self.itsThrows[self.ball+1] == 10):
            self.ball += 1
            return True

        return False

    def nextTwoBalls(self):
        return self.itsThrows[self.ball] + self.itsThrows[self.ball + 1]

    def nextBall(self):
        return self.itsThrows[self.ball]

    def twoBallsInFrame(self):
        score = self.itsThrows[self.ball]
        self.ball += 1
        score += self.itsThrows[self.ball]
        self.ball +=1
        return score

    #Tests (sort of)
def bowlPerfectGame():
    game = Game()
    for i in range(0, 12):
        game.add(10)
    
    print (game.scoreForFrame(10))

def bowl299Game():
    game = Game()
    for i in range(0, 11):
        game.add(10)

    game.add(9)
    print (game.scoreForFrame(10))

def bowl279Game():
    game = Game()
    game.add(9)
    game.add(0)
    for i in range(0,11):
        game.add(10)

    print (game.scoreForFrame(10))

def bowl90Game():
    game = Game()
    for i in range(0, 10):
        game.add(9)
        game.add(0)

    print(game.scoreForFrame(10))

bowlPerfectGame()
bowl299Game()
bowl279Game()
bowl90Game()
