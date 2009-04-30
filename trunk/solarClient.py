#Client code sxrclient.py
import xmlrpclib
import orbitSystem
import planetarium
import Eval
import cPickle
from planetarium import Universe
from orbitSystem import Body
from orbitSystem import System
#import psyco
#psyco.full()
from Eval import Eval

class solarClient(object):
    def __init__(self, xString = 'http://bamdastard.kicks-ass.net:8000', scoreThresh=1):
        try:
            self.server = xmlrpclib.Server(xString)
            self.xfile = self.server.getSystem()
            self.mySystem = cPickle.loads(self.xfile)
            self.Evaluator = Eval(self.mySystem, 1000)
            self.scoreThreshold =scoreThresh;
            self.score = 1000
            while self.score > self.scoreThreshold:
                self.xfile = self.server.getSystem()
                self.mySystem = cPickle.loads(self.xfile)
                self.Evaluator = Eval(self.mySystem, 1000)
                self.score = self.Evaluator.evaluate()
                print self.score
            self.server.insertSystem(self.xfile)
            self.planetWindow = Universe(self.Evaluator)
            run()
        except:
            self.runLocal()
    def runLocal(self):
        print "unable to connect to server"
        sysCount = 1
        self.mySystem = System(sysCount)
        self.Evaluator = Eval(self.mySystem, 1000)
        self.scoreThreshold =1;
        self.score = 1000
        while self.score > self.scoreThreshold:
            self.mySystem = System(sysCount)
            self.Evaluator = Eval(self.mySystem, 1000)
            self.score = self.Evaluator.evaluate()
            print self.score
            sysCount+=1
        self.planetWindow = Universe(self.Evaluator)
        run()
        
#defaultClient = solarClient("badconnectstring", 1)
defaultClient = solarClient("badcstring", 1)