import obd,time
import json, os
from log import Log
from Logger import Logger

class car:
    def __init__(self, logger):
        self.connection = obd.Async()
        self.log = Log()
        self.logger = logger
        self.counter = 0
   
    def getSpeed(self,r):
	self.log.add("SPEED", str(r.value))
        self.count()

    def getFuelLevel(self,r):
	print(r.value)
        self.log.add("FUEL_LEVEL", str(r.value))
        self.count()

    def getThrottlePosition(self,r):
	self.log.add("THROTTLE_POSITION", str(r.value))
        self.count()

    def getCoolantTemp(self,r):
        self.log.add("COOLANT_TEMP", str(r.value))
        self.count()

    def getOilPressure(self,r):
        self.log.add("RPM", str(r.value))
        self.count()

    def getLoad(self,r):
	self.log.add("ENGINE_LOAD",str(r.value))
	self.count()

    def getFuelRate(self,r):
	self.log.add("FUEL_RATE", str(r.value))
	self.count()


    def count(self):
        self.counter += 1
        if self.counter == 7 : #number of callbacks 
            self.logger.write(self.log.getLog())
	    self.counter = 0

 
    def setupCallbacks(self):
        self.connection.watch(obd.commands.SPEED, callback=self.getSpeed)
        self.connection.watch(obd.commands.FUEL_LEVEL, callback=self.getFuelLevel)
        self.connection.watch(obd.commands.THROTTLE_POS, callback=self.getThrottlePosition)
        self.connection.watch(obd.commands.COOLANT_TEMP, callback=self.getCoolantTemp)
        self.connection.watch(obd.commands.RPM, callback=self.getOilPressure) # change to oil pressure
	self.connection.watch(obd.commands.ENGINE_LOAD, callback=self.getLoad)
	self.connection.watch(obd.commands.FUEL_RATE, callback=self.getFuelRate)

    def startLogging(self):
	self.connection.start()

    def stopLogging(self):
	self.connection.stop()

    def getStatus(self):
        return self.connection.status()



Logger = Logger()
tahoe = car(Logger)
tahoe.setupCallbacks()
while tahoe.getStatus() == OBDStatus.CAR_CONNECTED:
    tahoe.startLogging()
tahoe.stopLogging() 
