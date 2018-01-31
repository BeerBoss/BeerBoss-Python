# Imports
import threading
import os
import time
import random
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
from .display import Display

class Sensor(threading.Thread):
    def __init__(self, busaddr):
        threading.Thread.__init__(self)
        self.sensor = 'sys/bus/w1/devices/'+ busaddr + '/w1_slave'
        self.display = Display()
        self.currentTemp = None
        self.previousTemp = None
        self.stopFlag = False
        self.start()  # Start the thread

    def run(self):
        while not self.stopFlag:
            self.read_temp()
            time.sleep(1)              # Let the thread sleep for 1 second
        print("Sensor recording has been stopped!")
        del self

    def temp_raw(self):
        f = open(self.sensor, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def read_temp(self):
        lines = self.temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.temp_raw()
        temp_output = lines[1].find('t=')

        if temp_output != -1:
            temp_string = lines[1].strip()[temp_output + 2:]
            temp_c = float(temp_string) / 1000.0
            self.previousTemp = self.currentTemp
            self.currentTemp = temp_c

    def stopRecording(self):
        self.stopFlag = True
