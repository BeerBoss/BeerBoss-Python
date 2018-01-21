# Imports
from .enum import RelayState
from .lcd import Lcd

class Relay:
    def __init__(self, relaypin):
        self.lcd = Lcd()
        self.relayPin = relaypin
        self.relayState = RelayState.OFF

    def __del__(self):
        self.turnoff()
        self.lcd.print("Relaycontrol for pin {} has been stopped. Pin has been turned off".format(self.relayPin))

    def turnoff(self):
        # Logic to turn off using GPIO
        self.relayState = RelayState.OFF

    def turnon(self):
        # Logic to turn on using GPIO
        self.relayState = RelayState.ON
