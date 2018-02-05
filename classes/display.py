# Credits to https://raspberrytips.nl/lcd-scherm-20x4-i2c-raspberry-pi/

# Constants
LCD_WIDTH = 20   # Maximum characters per line

LCD_CHR = 1 # Mode - Sending data
LCD_CMD = 0 # Mode - Sending command

LCD_LINES = [0x80, 0xC0, 0x94, 0xD4] # LCD RAM addresses for line 1 to 4

LCD_BACKLIGHT_ON  = 0x08  # On 0X08 / Off 0x00

ENABLE = 0b00000100 # Enable bit

E_PULSE = 0.0005
E_DELAY = 0.0005

#Imports
from smbus2 import SMBus
import time

class Lcd:
    def __init__(self, i2c_addr):
        self.bus = SMBus(1)
        self.i2c_addr = i2c_addr
        if i2c_addr:
            self.lcd_byte(0x33, LCD_CMD)  # 110011 Initialise
            self.lcd_byte(0x32, LCD_CMD)  # 110010 Initialise
            self.lcd_byte(0x06, LCD_CMD)  # 000110 Cursor move direction
            self.lcd_byte(0x0C, LCD_CMD)  # 001100 Display On,Cursor Off, Blink Off
            self.lcd_byte(0x28, LCD_CMD)  # 101000 Data length, number of lines, font size
            self.lcd_byte(0x01, LCD_CMD)  # 000001 Clear display
            time.sleep(E_DELAY)

    def lcd_byte(self, bits, mode):
        bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT_ON
        bits_low = mode | ((bits << 4) & 0xF0) | LCD_BACKLIGHT_ON

        self.bus.write_byte(self.i2c_addr, bits_high)
        self.lcd_toggle_enable(bits_high)

        self.bus.write_byte(self.i2c_addr, bits_low)
        self.lcd_toggle_enable(bits_low)

    def lcd_toggle_enable(self, bits):
        time.sleep(E_DELAY)
        self.bus.write_byte(self.i2c_addr, (bits | ENABLE))
        time.sleep(E_PULSE)
        self.bus.write_byte(self.i2c_addr, (bits & ~ENABLE))
        time.sleep(E_DELAY)

    def lcd_string(self, message, line):
        message = message.ljust(LCD_WIDTH, " ")
        self.lcd_byte(LCD_LINES[line], LCD_CMD)
        for i in range(LCD_WIDTH):
            self.lcd_byte(ord(message[i]), LCD_CHR)



class Display:
    class __Display:
        def __init__(self, i2c_addr):
            self.lcd = Lcd(i2c_addr)
            self.lcd.lcd_string("BeerBoss v1", 1)

        def __del__(self):
            self.print("Deleting myself, bye now")

        def print(self, text):
            print(text)



    instance = None

    def __new__(cls, i2c_addr = None):  # __new__ always a classmethod
        if not Display.instance:
            Display.instance = Display.__Display(i2c_addr)
        return Display.instance
