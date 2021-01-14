from font import fonts
import gc
import ujson
import time

def image(file,display):
    with open(file,'r') as f:
        li=ujson.loads(f.read())
    display.fill(0)
    for i in li:
        x=32*(i[1]//8)+i[0]
        y=i[1]%8
        display.pixel(x,y,1)
    display.show()
    
def pixel(x,y,fill,display):
    # print(x,y)
    if x<32 and y<32:
        sx=32*(y//8)+x
        sy=y%8
        display.pixel(sx,sy,fill)

def chinese(ch_str, x_axis, y_axis,display):
    offset_ = 0
    # y_axis = y_axis*8 # 中文高度一行占8个  
    # x_axis = (x_axis*16)  # 中文宽度占16个    
    y_axis = y_axis # 中文高度一行占8个  
    x_axis = x_axis  # 中文宽度占16个

    for k in ch_str:
        code = 0x00  # 将中文转成16进制编码
        data_code = k.encode("utf-8")
        # print(data_code)
        code |= data_code[0] << 16
        code |= data_code[1] << 8
        code |= data_code[2]
        # print(code)
        byte_data = fonts[code]
        for y in range(0, 16):
            a_ = bin(byte_data[y]).replace('0b', '')
            while len(a_) < 8:
                a_ = '0'+a_
            b_ = bin(byte_data[y+16]).replace('0b', '')
            while len(b_) < 8:
                b_ = '0'+b_
            for x in range(0, 8):
                pixel(x_axis+offset_+x, y+y_axis, int(a_[x]),display)   
                pixel(x_axis+offset_+x+8, y+y_axis, int(b_[x]),display)   
        offset_ += 16

        def anime1(text,display):
    a=text[0:1]
    c=text[1:2]
    b=text[2:3]
    d=text[3:4]
    display.fill(0)
    chinese(a,0,0,display)
    time.sleep(0.1)
    display.show()
    display.fill(0)
    chinese(b,16,0,display)
    time.sleep(0.1)
    display.show()
    display.fill(0)
    chinese(c,0,16,display)
    time.sleep(0.1)
    display.show()
    display.fill(0)
    chinese(d,16,16,display)
    time.sleep(0.1)
    display.show()
    display.fill(0)
    chinese(a+b,0,0,display)
    chinese(c+d,0,16,display)
    display.show()
    time.sleep(0.2)
    display.fill(0)
    display.show()
    time.sleep(0.1)
    chinese(a+b,0,0,display)
    chinese(c+d,0,16,display)
    display.show()
    time.sleep(0.3)
    display.fill(0)
    display.show()
    time.sleep(0.1)
    chinese(a+b,0,0,display)
    chinese(c+d,0,16,display)
    display.show()
    time.sleep(1)
    display.fill(0)
    display.show()
    time.sleep(0.5)

def anime2(text,display):
    a=text[0:1]
    c=text[1:2]
    b=text[2:3]
    d=text[3:4]
    display.fill(0)
    chinese(a+b,0,0,display)
    chinese(c+d,0,16,display)
    display.show()
    time.sleep(0.5)
    display.fill(0)
    display.show()
    time.sleep(0.2)
    chinese(a+b,0,0,display)
    chinese(c+d,0,16,display)
    display.show()
    time.sleep(1)
    display.fill(0)
    display.show()
    time.sleep(0.2)
    chinese(a+b,0,0,display)
    chinese(c+d,0,16,display)
    display.show()
    time.sleep(2)

def anime3(text,display):
    a=text[0:1]
    c=text[1:2]
    b=text[2:3]
    d=text[3:4]
    display.fill(0)
    chinese(a,0,0,display)
    time.sleep(0.1)
    display.show()
    chinese(b,16,0,display)
    time.sleep(0.1)
    display.show()
    chinese(c,0,16,display)
    time.sleep(0.1)
    display.show()
    chinese(d,16,16,display)
    time.sleep(0.1)
    display.show()
    display.fill(0)
    display.show()
    time.sleep(0.2)
    chinese(a+b,0,0,display)
    chinese(c+d,0,16,display)
    display.show()
    time.sleep(1)
    display.fill(0)
    display.show()
    time.sleep(0.2)
    chinese(a+b,0,0,display)
    chinese(c+d,0,16,display)
    display.show()
    time.sleep(2)
