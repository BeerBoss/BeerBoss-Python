# Imports
from .enum import RelayState


class Relay:
    def __init__(self, relaypin):
        self.relayPin = relaypin
        self.relayState = RelayState.OFF

    def turnoff(self):
        # Logic to turn off using GPIO
        self.relayState = RelayState.OFF

    def turnon(self):
        # Logic to turn on using GPIO
        self.relayState = RelayState.ON
