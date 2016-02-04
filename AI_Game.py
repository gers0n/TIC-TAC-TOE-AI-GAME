import os, random
from pprint import pprint
from player import Player
from game import Game


class AIPlayer(Player):
    # def __init__(s, name = None, debugMode = True):
    #     super(Player, s).__init__()
    def __autoPlay(self, emptyStep = [], fullSteps = []):
        nextPlay = random.choice(emptyStep)
        return ",".join( nextPlay )

    def autoPlayTTT(self):

        
        if self.currentGame:
            _map = self.currentGame.map
            empty = []
            played = []
            for i in range(len(_map)):
                y = _map[i]

                for i2 in range(len( y )):
                    x  = _map[i][i2]
                    if x == 0:
                        empty.append([str(i+1), str(i2+1) ])
                    else:
                        played.append([str(i+1), str(i2+1)])
            if self.DEBUG:
                print "\nAIPlayer get TTT Moves\n"
                print "==================="
                print "=========PC========"
                print "==================="
                print "Empty positions:", empty
                print "Played positions:", played
                print "==================="
            move = self.__autoPlay( empty, played)
            print move
            return move
        return raw_input("x,y: ")


class HumanPlayer(Player):

    def _play(selfs):
        return raw_input()

os.system("cls")


Me = HumanPlayer("Fhillip") #Player 1
AIP = AIPlayer("AI Machine") #Player 2
g = Game()

Me.registerGameWithCB(g, Me._play );

AIP.registerGameWithCB(g, AIP.autoPlayTTT )

# raw_input()

g.addPlayer(Me)
g.addPlayer(AIP)

# AIP._game = g

# print "player list"
# pprint(g.     )
print "\n=================="
print "Starting"
g.start()
# raw_input()
