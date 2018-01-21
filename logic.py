# Imports
from classes.lcd import Lcd
from classes.relay import Relay
from classes.sensor import Sensor
from classes.web import Web
from classes.enum import Action
import threading
import settings
import time

class Logic(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.lcd = Lcd(settings.lcd_i2c_addr)
        self.cooler = Relay(settings.cooler_relayPin)
        self.heater = Relay(settings.heater_relayPin)
        self.sensorFridge = Sensor(settings.sensorFridgePin)
        self.sensorBarrel = Sensor(settings.sensorBarrelPin)
        self.web = Web(settings.webAddress, settings.email, settings.password)
        self.action = Action.NOTHING
        self.processingData = []

    def __del__(self):
        del self.cooler
        del self.heater
        self.sensorFridge.stopRecording()
        self.sensorBarrel.stopRecording()
        del self.web
        del self.lcd

    def submitData(self):
        self.web.submitData(self.sensorFridge.currentTemp, self.sensorBarrel.currentTemp, self.cooler.relayState.value, self.heater.relayState.value)


if __name__ == "__main__":
    logic = Logic()
    try:
        while(1):
            logic.submitData()
            time.sleep(1)
    except KeyboardInterrupt:
        del logic
