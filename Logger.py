import arrow, os, json

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
