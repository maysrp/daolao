from cnfont import chinese,pixel
import max7219
from machine import Pin, SPI
import time
spi = SPI(1, baudrate=4000000, polarity=1, phase=0, sck=Pin(4), mosi=Pin(2))
ss = Pin(5, Pin.OUT)
display = max7219.Matrix8x8(spi, ss, 16)


l1="大佬让我过去吧"
l2="祝您身体健康"
l3="财源广进"
def flx(lx,r="r"):
    if r=="l":
        r="<"
    else:
        r=">"
    for i in range(len(lx)-1):
        display.fill(0)
        chinese(lx[i:i+2],0,0,display)
        display.text(r+r+r+" ",96,0,1)
        display.text('----',64,0,1)
        display.show()
        time.sleep(0.1)
        if i<len(lx)-2:
            display.fill(0)
            chinese(lx[i:i+3],-4,0,display)
            display.text(" "+r+r+r,96,0,1)
            display.text('----',64,0,1)
            display.show()
            time.sleep(0.1)
            display.fill(0)
            chinese(lx[i:i+3],-8,0,display)
            display.text(r+" "+r+r,96,0,1)
            display.text('----',64,0,1)
            display.show()
            time.sleep(0.1)
            display.fill(0)
            chinese(lx[i:i+3],-12,0,display)
            display.text(r+r+" "+r,96,0,1)
            display.text('----',64,0,1)
            display.show()
            time.sleep(0.1)





def xx():
    display.fill(0)
    chinese("谢",0,0,display)
    time.sleep(0.1)
    display.show()
    display.fill(0)
    chinese("谢",16,0,display)
    time.sleep(0.1)
    display.show()
    display.fill(0)
    chinese("大",0,16,display)
    time.sleep(0.1)
    display.show()
    display.fill(0)
    chinese("佬",16,16,display)
    time.sleep(0.1)
    display.show()
    display.fill(0)
    chinese("谢谢",0,0,display)
    chinese("大佬",0,16,display)
    display.show()
    time.sleep(0.2)
    display.fill(0)
    display.show()
    time.sleep(0.1)
    chinese("谢谢",0,0,display)
    chinese("大佬",0,16,display)
    display.show()
    time.sleep(0.3)
    display.fill(0)
    display.show()
    time.sleep(0.1)
    chinese("谢谢",0,0,display)
    chinese("大佬",0,16,display)
    display.show()
    time.sleep(1)
    display.fill(0)
    display.show()
    time.sleep(0.5)

def zm():
    display.fill(0)
    chinese("大佬",0,0,display)
    chinese("最美",0,16,display)
    display.show()
    time.sleep(0.5)
    display.fill(0)
    display.show()
    time.sleep(0.2)
    chinese("大佬",0,0,display)
    chinese("最美",0,16,display)
    display.show()
    time.sleep(1)
    display.fill(0)
    display.show()
    time.sleep(0.2)
    chinese("大佬",0,0,display)
    chinese("最美",0,16,display)
    display.show()
    time.sleep(2)



flx(l1)
flx(l2)
flx(l3)
time.sleep(2)
xx()
zm()
