from machine import Pin,ADC
from time import sleep
gaz= Pin(36,Pin.IN)
buzzer= Pin(1, Pin.OUT,value=0)

while True:

    gazz=gaz.value()
    print("gaz:",gazz)
    if gazz==0:
        buzzer.value(1)
    else:
        buzzer.value(0)
    sleep(1)