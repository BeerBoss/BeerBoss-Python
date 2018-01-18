# Imports
from classes.database import Database
from classes.lcd import Lcd
from classes.relay import Relay
from classes.sensor import Sensor
import threading
import settings
import time

class Logic(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.database = Database(settings.db_host, settings.db_user, settings.db_user_password, settings.db_database)
        self.lcd = Lcd(settings.lcd_i2c_addr)
        self.cooler = Relay(settings.cooler_relayPin)
        self.heater = Relay(settings.heater_relayPin)
        self.sensorFridge = Sensor(settings.sensorFridgePin)
        self.sensorBarrel = Sensor(settings.sensorBarrelPin)
        self.start()

    def run(self):
        while(1):
            self.lcd.print(self.cooler.relayState)
            self.database.submitData(self.sensorFridge.currentTemp, self.sensorBarrel.currentTemp, self.cooler.relayState.value, self.heater.relayState.value)
            time.sleep(60)  # Wait a minute


if __name__ == "__main__":
    logic = Logic()
