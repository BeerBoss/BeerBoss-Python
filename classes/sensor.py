# Imports
import threading
import time
import random
from .lcd import Lcd

class Sensor(threading.Thread):
    def __init__(self, busaddr):
        threading.Thread.__init__(self)
        self.sensor = busaddr
        self.lcd = Lcd()
        self.currentTemp = None
        self.previousTemp = None
        self.stopFlag = False
        self.start()  # Start the thread

    def run(self):
        while not self.stopFlag:
            self.generatedata()
            time.sleep(1)              # Let the thread sleep for 1 second
        print("Sensor recording has been stopped!")
        del self

    def stopRecording(self):
        self.stopFlag = True

    def generatedata(self):
        # Generates random data until sensors are hooked up
        self.previousTemp = self.currentTemp
        self.currentTemp = random.uniform(1, 28)
