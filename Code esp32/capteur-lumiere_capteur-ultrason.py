from machine import Pin,ADC
from time import sleep
from hcsr04 import HCSR04
ultrason = HCSR04(trigger_pin=12,echo_pin=14,echo_timeout_us=1000000)
led1=Pin(13,Pin.OUT)
photo=ADC(Pin(34))
while True:
    distance = ultrason.distance_cm() 
    lum=photo.read()
    print(distance,'cm','ldr',lum)
    if lum<3000 and distance <15:
        print("led on")
        led1.value(0)
    else:
        print("led off")
        led1.value(1)
    sleep(2)
        
    
 
