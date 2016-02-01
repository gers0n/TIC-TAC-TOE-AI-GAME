import os
from pprint import pprint

class Game:
    __str__ = "Tic Tac Toe"
    playerList = []
    
    class __Winner: 
        player= None
        someWinner= False

    def addPlayer(s, player):
        if len(playerList) < 2:
            s.playerList.append(player)
            
    def reinit(s):
        print "has to asign your player Name"
        p1 = raw_input("Player1 Name: ")
        p2 = raw_input("player2 Name (PC for AI): ") 
        return s.__init__(p1, p2 or "PC")
    
    def __init__(s, player1 = None, player2 = None):
        if not player1:
            return s.reinit()
            
        s.winner = s.__Winner()
        s.useAI = False

        #set game to players
        if player1:
              s.addPlayer(player1)
        if player2:
              s.addPlayer(player2)
              
        for player in s.playerLIst:
            player.knownGameSTR[ s.__str__ ] = s
            
        s.player = player1
        s.player2 = player2
          
        s.renderMap()
        s.changeTurn()
    
        
    def console(s):
        def __consoleHelp():
            print '\nHelp'
            pprint(switch.keys())
            print '\n'
            
        codeSTR, switch = "</>", {
            "exit":exit,
            "setFullMap":s.setFullMap,
            "help": __consoleHelp
            }
        
        while True:
            command = raw_input("%s: "%codeSTR).split(" ")
            print len(command)
            if command[0] == "exit":
                break;
##            try:
            
            if len(command) > 1:
                if command[1] != " ":
                    args = command[1].split(",")
                    switch[ command[0] ]( *args )
            else:
                switch[ command[0] ]()
##            except:
##                print "Command not reconized"
                
            
    def start(s):
        ## render an UI map
        s.renderUIMap()
        
        # run the game
        while s.winner.someWinner == False:
            s.makeAMove()
            s.verifyGameStatus()

    def run(s):
        s.start()
        
    def renderMap(s):
        s.map = [
            [0,0,0], # [11,12,13],
            [0,0,0], # [21,22,23],
            [0,0,0], # [31,32,33],
        ]
        
    def renderUIMap(s):
        ## os.system("cls")
        for colm in s.map:
            print colm

    def changeTurn(s, actualTurn = None):
        if not actualTurn or actualTurn == s.player2:
            s.turn = s.player
        else:
            s.turn = s.player2
        print s.turn
        
    def makeAMove(s):
        toAsign = 1 if s.turn == s.player else 2
        print s.turn.name+" Atack at position (x,y) (help if needed): "
        action = s.turn.play(s.__str__)
        
        if action == "superConsole":
            print "setFullMap exec"
            return s.console()
        try:
            if not action == "help":
                pos = {
                    "x": int(action.split(",")[0])-1,
                    "y": int(action.split(",")[1])-1
                    }
                if s.map[pos["x"] ] [pos["y"]] == 0:
                    s.map[pos["x"] ] [pos["y"]] = toAsign
                    s.changeTurn(s.turn)
                    s.renderUIMap()
                    
                else:
                    print "Wrong position"
                    return s.play()
        except:
            pass
            
    def verifyGameStatus(s):
        s.verifyMapIsNotFull()
        s.verifyIfAnyWinner()
        
    def verifyMapIsNotFull(s):
        if s.map[0][0] and s.map[0][1] and s.map[0][2] and s.map[1][0] and s.map[1][1] and s.map[1][2] and s.map[2][0] and s.map[2][1] and s.map[2][2]:
            print "Map is full\nIf wanna play again run: GameInstance.run()\n"
            s.setWinner()
            
    def setFullMap(s, superAdminAccess = "Something"):
        def __runFullyMap(superAdminAccess):
            s.map = [
                [4,4,4],
                [4,4,4],
                [4,4,4],
                ]
            s.setWinner()
            s.renderMap()
        if superAdminAccess:
            return __runFullyMap(superAdminAccess)
    
    def verifyIfAnyWinner(s):
        pass

    def setWinner(s, player =None):
        s.winner.player = player
        s.winner.someWinner = True

    def AIPlay(s):
        pass

class Player:
    name = ""
    __game = None
    knownGameSTR = {}
    knownGameSTRCBs = {}
    
    def __init__(s, playCallback = None):
        s.play = playCallback
    def __none__(s):
        pass

    def play(s, gameSTR = ""):
        if s.knownGameSTRCBs.get(game.__str__):
            return s.knownGameSTRCBs[game.__str__]()

    def registerGameWithCB(s, game, callback):
        s.knownGameSTRCBs[game.__str__] = callback
        
class AIPlayer(Player):
    name = "PC"
    def _play(s):
        s.getGameMoves()
        return s.play()
        
    def getGameMoves(s):
        print "==================="
        print "=========PC========"
        print "==================="
        _map = s.__game.map
        empty = []
        played = []
        for i in range(len(_map)):
            y = _map[i]
            print y
            for i2 in range(len(_map[i])):
                x  = _map[i][i2]
                if x == 0:
                    empty.append([i, i2])
                else:
                    played.append([i, i2])
        print "Empty positions:", empty
        print "Played positions:", played
                    

class HumanPlayer(Player):
    def __init__(s, name = None):
         s.name = name
         
    def play(s, gameSTR = ""):
        
        return raw_input()

AIP = AIPlayer("AI Machine") #Player 2
Me = HumanPlayer("Fhillip") #Player 1

g = Game()

AIP.registerGameWithCB(g, AIP._play)
Me.registerGameWithCB(g, raw_input)

g.start()
raw_input()
