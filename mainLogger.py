import obd
import arrow
import json
import os


class Log:
    def __init__(self):
        date = arrow.now('US/Central')
        folder =  "/home/ryan/OBDlogs/" + date.format('MM-DD-YYYY')
        if not (os.path.isdir(folder)):
            os.mkdir(folder)
        filename = date.format('HH_mm_ss')
        self.toFile = open(folder+filename,'w+')
        begin = {"id":"BEGIN", "time":arrow.now('US/Central').format('HH:mm:ss')}
        self.toFile.write(json.dumps(begin))

    def write(self, data):
	toWrite = {"id": update, "time":arrow.now('US/Central').format('HH:mm:ss'), "Fuel_Level": str(data.fuel_level), "Speed": str(data.speed), "coolant": str(data.coolant)}
        self.toFile.write(json.dumps(toWrite))

    def close():
        lastline = {"id":"END", "time":arrow.now('US/Central').format('HH:mm:ss')}
        self.toFile.write(json.dumps(lastline))
        self.toFile.close()

class car:
    def __init__(self):
        self.connection = obd.OBD()
	Logger.write(self.connection)
    def test():
        cmd = obd.commands["RPM"]
        response = self.connection.query(cmd)
	Logger.write(response)
        return response.value
    def getSpeed():
	return str(self.connection.query(obd.commands.SPEED).value)
    def getFuelLevel():
	return str(self.connection.query(obd.commands.FUEL_LEVEL).value)
    def getThrottlePosition():
	return str(self.connection.query(obd.commands.THROTTLE_POS).value)
    def getCoolantTemp():
	return str(self.connection.query(obd.commands.COOLANT).value)


Logger = Log()
#tahoe = car()
#car.test
#Logger.write(tahoe.test)

connection = obd.OBD()

coolant = obd.commands.COOLANT_TEMP
speed = obd.commands.SPEED
fuel_level = obd.commands.FUEL_LEVEL
throttle_pos = obd.commands.THROTTLE_POS
data = {}

while True:
	Logger.write(' Coolant:') 
	connection.query(coolant).value))
	data.
	Logger.write(' speed:')
	Logger.write(str(connection.query(speed).value))
	Logger.write(' fuel level:')
	Logger.write(str(connection.query(fuel_level).value))
	Logger.write(' Throttle Position')
