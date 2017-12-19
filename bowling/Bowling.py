#This was my initial attempt. Got stuck and went looking for help.
#Result is in Bowling2.py

class Frame:
    number = 0
    first = None
    second = None
    third = None

    def __init__(self, frameNumber):
        self.number = frameNumber

class Game:
    frames = []

    def __init__(self):
        i = 1
        while i < 11:
            print (i)
            self.frames.append(Frame(i))
            i = i + 1
    
    def calculate(self):
        score = 0
        i = 1
        while i < 11:
            if i < 10:
                if self.frames[i - 1].first != None:
                    score = score + self.frames[i].first

                if self.frames[i - 1].second != None:
                    score = score + self.frames[i].second

            i = i + 1

        print(score)

    def getScore(self, frameNumber, ball):
            print("---Frame " + str(frameNumber) + "---")
            value = int(input("Enter # of pins " + ball + " ball: "))
            if value == 10:
                print("STRIKE!")

            return value

    def play(self):
        i = 1
        while i < 11:
            first = self.getScore(i, "first")
            #print("---Frame " + str(i) + "---")
            #first = int(input("Enter # of pins first ball: "))
            self.frames[i - 1].first = first

            if first < 10:
                second = self.getScore(i, "second")                
                while(second > 10 - first):
                    print("***ERROR: Second ball must be less than or equal to: " + str(10 - first))
                    second = self.getScore(i, "second")               

                if first + second == 10:
                    print("SPARE!")

                self.frames[i - 1].second = second

            if i == 10:
                if first == 10:
                    second = self.getScore(i, "second")                
                    self.frames[i - 1].second = second
                    
                    third = self.getScore(i, "third")
                    self.frames[i - 1].third = third

            i = i + 1

game = Game()
game.play()
