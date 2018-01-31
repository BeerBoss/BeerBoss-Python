# Imports
from .enum import RelayState
from .display import Display
import RPi.GPIO as GPIO

class Relay:
    def __init__(self, relaypin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(relaypin, GPIO.OUT)
        self.display = Display()
        self.relayPin = relaypin
        self.relayState = RelayState.OFF

    def __del__(self):
        self.turnoff()
        self.display.print("Relaycontrol for pin {} has been stopped. Pin has been turned off".format(self.relayPin))
        GPIO.cleanup()

    def turnoff(self):
        GPIO.output(self.relayPin, GPIO.HIGH)
        self.relayState = RelayState.OFF

    def turnon(self):
        GPIO.output(self.relayPin, GPIO.LOW)
        self.relayState = RelayState.ON
