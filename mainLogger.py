import obd
import arrow
import json, os
from log import Log


class Logger:
    def __init__(self):
        date = arrow.now('US/Central')
        folder =  "/home/ryan/OBDlogs/" + date.format('MM-DD-YYYY')
        if not os.path.isdir(folder):
            os.mkdir(folder, 0755)
        filename = date.format('HH_mm_ss')
        self.toFile = open(folder+filename,'w+')
        begin = {"id":"BEGIN", "time":arrow.now('US/Central').format('HH:mm:ss')}
        self.toFile.write(json.dumps(begin))
    def write(self, data):
        print(data)
        self.toFile.write(json.dumps(data))

    def close():
        lastline = {"id":"END", "time":arrow.now('US/Central').format('HH:mm:ss')}
        self.toFile.write(json.dumps(lastline))
        self.toFile.close()

class car:
    def __init__(self, logger):
        self.connection = obd.Async()
        self.log = Log()
        self.logger = logger
        self.counter = 0
   
    def getSpeed(self,r):
	self.log.add("SPEED", r.value)
        self.count()

    def getFuelLevel(self,r):
        self.log.add("FUEL_LEVEL", r.value)
        self.count()

    def getThrottlePosition(self,r):
	self.log.add("THROTTLE_POSITION", r.value)
        self.count()

    def getCoolantTemp(self,r):
        self.log.add("COOLANT_TEMP", r.value)
        self.count()

    def getOilPressure(self,r):
        self.log.add("OIL_PRESSURE", r.value)
        self.count()

    def count(self):
        self.count += 1
        if self.counter == 5: #number of callbacks 
            self.logger.write(self.log.getlog())

 
    def setupCallbacks(self):
        self.connection.watch(obd.commands.SPEED, callback=self.getSpeed)
        self.connection.watch(obd.commands.FUEL_LEVEL, callback=self.getFuelLevel)
        self.connection.watch(obd.commands.THROTTLE_POS, callback=self.getThrottlePosition)
        self.connection.watch(obd.commands.COOLANT_TEMP, callback=self.getCoolantTemp)
        self.connection.watch(obd.commands.OIL_TEMP, callback=self.getOilPressure) # change to oil pressure



Logger = Logger()
tahoe = car(Logger)

tahoe.setupCallbacks()
