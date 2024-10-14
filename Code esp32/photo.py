from machine import Pin,ADC
from time import sleep
photo=ADC(Pin(36))
while True:
    lum=photo.read()
    print(lum)
    sleep(1)
        
    