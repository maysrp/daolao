from cnfont import chinese
import max7219
from machine import Pin, SPI
spi = SPI(1, baudrate=400000, polarity=1, phase=0, sck=Pin(4), mosi=Pin(2))
ss = Pin(5, Pin.OUT)
display = max7219.Matrix8x8(spi, ss, 16)
chinese("大佬最美",0,0,display)
