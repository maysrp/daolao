from cnfont import chinese,pixel,image,anime1,anime2,anime3,flx,anime0
import max7219
from machine import Pin, SPI
import time
spi = SPI(1, baudrate=4000000, polarity=1, phase=0, sck=Pin(4), mosi=Pin(2))
ss = Pin(5, Pin.OUT)
display = max7219.Matrix8x8(spi, ss, 16)


l1="大佬让我过去吧"
l2="祝您身体健康"
l3="财源广进"









# flx(l1,display)
# flx(l2)
# flx(l3)
# time.sleep(2)


anime0("爱一直在",display)
# anime1("下次一定",display)
# anime2("一键三连",display)
# anime3("拒绝白嫖",display)

image("b.json",display)
