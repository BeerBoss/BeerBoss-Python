# Imports
from classes.display import Display
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
        self.display = Display(settings.lcd_i2c_addr)
        self.cooler = Relay(settings.cooler_relayPin)
        self.heater = Relay(settings.heater_relayPin)
        self.sensorFridge = Sensor(settings.sensorFridgeAddress)
        self.sensorBarrel = Sensor(settings.sensorBarrelAddress)
        self.web = Web(settings.webAddress, settings.email, settings.password)
        self.action = Action.NOTHING
        self.processingData = []

    def __del__(self):
        del self.cooler
        del self.heater
        self.sensorFridge.stopRecording()
        self.sensorBarrel.stopRecording()
        del self.web
        del self.display

    def submitData(self):
        self.web.submitData(self.sensorFridge.currentTemp, self.sensorBarrel.currentTemp, self.cooler.relayState.value, self.heater.relayState.value)

    def decideAction(self):
        desiredTemp = self.web.getDesiredTemp()
        barrelTemp = self.sensorBarrel.currentTemp
        fridgeTemp = self.sensorFridge.currentTemp

        if barrelTemp and fridgeTemp and desiredTemp:
            if barrelTemp < desiredTemp:
                self.action = Action.HEAT
            elif barrelTemp > desiredTemp:
                self.action = Action.COOL

    def executeAction(self):
        self.cooler.setstate(self.action.value[0])
        self.heater.setstate(self.action.value[1])



if __name__ == "__main__":
    logic = Logic()
    try:
        while 1:
            logic.submitData()
            logic.decideAction()
            logic.executeAction()
            print(logic.action.value)
            time.sleep(5)
    except KeyboardInterrupt:
        del logic
