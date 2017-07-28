class Log:
    def __init__(self):
        self.data = {} 

    def add(self,id,val):
        self.data.update({id : val})

    def display(self):
        print(self.data)

    def getLog(self):
        return self.data

#_log = Log()
#_log.add("RPM",3000)
#_log.add("FUEL_LEVEL", 30.66)
#_log.add("OIL_PRESSURE", 40)
#print(_log.getLog()
