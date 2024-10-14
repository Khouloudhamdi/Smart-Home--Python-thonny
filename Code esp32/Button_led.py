from machine import Pin
from time import sleep
button =Pin(35,Pin.IN) 
led=Pin(13,Pin.OUT) 
while True:
    if button.value()==1:
        print('button:',button.value(),'led on')
        led.on()
    else :
        print('button:',button.value(),'led off')
        led.off()
    sleep(0.005)



