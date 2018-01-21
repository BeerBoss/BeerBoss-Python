# Imports

class Lcd:
    class __Lcd:
        def __init__(self, i2c_addr):
            self.I2C_addr = i2c_addr

        def __del__(self):
            self.print("Deleting myself, bye now")

        def print(self, text):
            # Test function for now. Including actual code when LCD is delivered and tested
            print(text)

    instance = None

    def __new__(cls, i2c_addr = None):  # __new__ always a classmethod
        if not Lcd.instance:
            Lcd.instance = Lcd.__Lcd(i2c_addr)
        return Lcd.instance
