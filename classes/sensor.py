# Imports
import threading
import time
import random
class Sensor(threading.Thread):
    def __init__(self, busaddr):
        threading.Thread.__init__(self)
        self.sensor = busaddr
        self.currentTemp = None
        self.previousTemp = None
        self.start()  # Start the thread

    def run(self):
        while 1:
            self.generatedata()
            time.sleep(1)              # Let the thread sleep for 1 second

    def generatedata(self):
        # Generates random data until sensors are hooked up
        self.previousTemp = self.currentTemp
        self.currentTemp = random.uniform(1, 28)

    def getdata(self):
        data = {'current': self.currentTemp, 'previous': self.previousTemp}
        return data
