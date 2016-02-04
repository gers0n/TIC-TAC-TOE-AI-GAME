from pprint import pprint
class Player(object):
    

    def __debugStr(s, method = None, momentSelf = None, extraStr = ""):
        return "\n%s\n self => %s, \n%s"%( method, momentSelf, extraStr)

    def __init__(s, name = None, debugMode = False):
        s.name = name
        s.knownGameSTR = {}
        s.knownGameSTRCBs = {}
        s.__currentGame = None;
        s.DEBUG = debugMode or False

    @property
    def currentGame(s):
        return s.__currentGame

    def play(s, gameSTR = ""):
        if s.knownGameSTRCBs.get(gameSTR):
            s.__setCurerntGame( s.knownGameSTR.get( gameSTR ) )
            if s.DEBUG:
                print "I am %s\nMyGamelistIs :\n%s\n    "%(s, s.knownGameSTRCBs)
                print "\nknownGameSTRCBs in "+gameSTR+" %s"%s.knownGameSTRCBs.get(gameSTR)
                print s.__debugStr("Playing", s, " %s %s" %(s.currentGame, s.knownGameSTRCBs[gameSTR]) )
         
            return s.knownGameSTRCBs[gameSTR]()
    
    def __setCurerntGame(s,  _game = None):
        s.__currentGame = _game

    def registerGameWithCB(s, _game = None, _callback = None):
        if s.DEBUG:
            print s.__debugStr("RegisteringGameWithCB", s, "game => %s \n callback = > %s\n"%(_game, _callback) )
            pprint( s.knownGameSTRCBs )
            print "\n"
        s.knownGameSTR[_game._GAMENAME] = _game
        s.knownGameSTRCBs[s.knownGameSTR[_game._GAMENAME]._GAMENAME] = _callback
        

    # def __str__(s):
    #     return "Player - %s"%s.name
