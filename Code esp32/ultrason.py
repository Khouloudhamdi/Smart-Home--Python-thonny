from hcsr04 import HCSR04
from machine import Pin
from time import sleep

ultrason = HCSR04(trigger_pin=5,echo_pin=18,echo_timeout_us=1000000)

while True:
    distance = ultrason.distance_cm() 
    print(distance,'cm')
    sleep(1)
 
