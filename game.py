import os
from pprint import pprint
from player import Player

class Game:
    playerList = []
    __GAMENAME = "Tic Tac Toe"
    
    @property 
    def _GAMENAME(self):
        return self.__GAMENAME

    class __Status:
        player = None
        someWinner = False

    def addPlayer(self, player=None):
        if len(self.playerList) <= 2 and player:
            self.playerList.append(player)
            print 'Added player - ', player
    
    def __init__(self):
        self.status = self.__Status()
        self.useAI = False
        self.turn = None
        self.renderMap()
        self.DEBUG = False

    def asignPlayers(self):
        self.turn = self.playerList[0]

    def console(self):
        def __consoleHelp():
            print '\nHelp'
            pprint(switch.keys())
            print '\n'
            
        codeSTR, switch = "</>", {
            "exit":exit,
            "setFullMap":self.setFullMap,
            "help": __consoleHelp
            }
        
        while True:
            command = raw_input("%s: "%codeSTR).split(" ")
            
            if command[0] == "exit":
                return;

            if len(command) > 1:
                if command[1] != " ":
                    print "Running %s"%switch[ command[0] ]
                    args = command[1].split(",")
                    switch[ command[0] ]( *args )
            if len(command) <= 1:
                print "Running %s no params"%switch[ command[0] ]
                switch[ command[0] ]()


    def start(self):
        if not len(self.playerList) == 2:
            if self.DEBUG:
                print len(self.playerList)
                print self.playerList
            print 'not enough players to play'
            return
        self.asignPlayers()

        ## render an UI map
        self.renderUIMap()
        for i in range(len(self.playerList)):
            print "Player #%i is %s\n"%(i+1, self.playerList[i])
        # run the game
        while self.status.someWinner == False:
            self.makeAMove()
            self.verifyGameStatus()

    def run(self):
        self.start()
        
    def renderMap(self):
        self.map = [
            [0,0,0], # [11,12,13],
            [0,0,0], # [21,22,23],
            [0,0,0], # [31,32,33],
        ]
        
    def renderUIMap(self):
        print "\n"
        for colm in self.map:
            print colm
        print "\n"

    def changeTurn(self, actualTurn = None):
        if (not actualTurn) or actualTurn == self.playerList[1]:
            self.turn = self.playerList[0]
        else:
            self.turn = self.playerList[1]
        if self.DEBUG: print "turn asigned", self.turn

    def makeAMove(self):
        toAsign = 1 if self.turn == self.playerList[0] else 2

        print "\n"+ str(self.turn.name)+" Atack at position (x,y) (help if needed): "
        # print self._GAMENAME

        action = self.turn.play(self._GAMENAME)

        if action == "superConsole":
            self.console()

        elif not action == "help":
            pos = {
                "x": int(action.split(",")[0])-1,
                "y": int(action.split(",")[1])-1
                }

            if self.map[pos["x"]][pos["y"]] == 0:
                self.map[pos["x"]][pos["y"]] = toAsign
                if self.DEBUG: 
                    print self.turn,"\n"
                    print "End %s turn"%self.turn,"\n"
                self.renderUIMap()
                self.changeTurn(self.turn)

            else:
                print "Wrong position\n"
        print "================================"
            
    def verifyGameStatus(self):
        self.verifyMapIsNotFull()
        self.verifyIfAnyWinner()
        
    def verifyMapIsNotFull(self):
        if self.map[0][0] and self.map[0][1] and self.map[0][2] and self.map[1][0] and self.map[1][1] and self.map[1][2] and self.map[2][0] and self.map[2][1] and self.map[2][2]:
            print "Map is full\nIf wanna play again run: GameInstance.run()\n"
            self.setWinner()
            
    def setFullMap(self, superAdminAccess = "Something"):
        def __runFullyMap(superAdminAccess):
            self.map = [
                [4,4,4],
                [4,4,4],
                [4,4,4],
            ]
            self.setWinner()
            self.renderMap()

        if superAdminAccess:
            return __runFullyMap(superAdminAccess)
    
    def verifyIfAnyWinner(self):
        pass

    def setWinner(self, player =None):
        self.status.player = player
        self.status.someWinner = True
