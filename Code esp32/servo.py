from machine import Pin,PWM 
from time import sleep
# servo=PWM(Pin(4),freq=50)
# servo.duty(75)
led = Pin(02, Pin.OUT)
led.on()
sleep(1)
# servo.duty(75)
#  
# while True:
#     servo.duty(125)
#     sleep(1)
#     servo.duty(75)
#     sleep(1)
#     
