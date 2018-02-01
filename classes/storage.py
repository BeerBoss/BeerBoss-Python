import json
import os

class Storage:
    def __init__(self, file):
        self.file = file
        self.data = self.readData()

    def readData(self):
        if os.path.isfile(self.file):
            with open(self.file, 'r') as f:
                return json.load(f)
        else:
            return None

    def writeData(self, data):
        with open(self.file, 'w') as f:
            json.dump(data, f)
