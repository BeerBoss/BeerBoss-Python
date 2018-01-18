# Imports

class Lcd:
    def __init__(self, i2c_addr):
        self.I2C_addr = i2c_addr

    def print(self, text):
        # Test function for now. Including actual code when LCD is delivered and tested
        print(text)
