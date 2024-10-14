import Stepper
from machine import Pin, ADC
from time import sleep
# m1
In1 = Pin(32,Pin.OUT)
In2 = Pin(33,Pin.OUT)
In3 = Pin(25,Pin.OUT)
In4 = Pin(26,Pin.OUT)
# m2
In11 = Pin(23,Pin.OUT)
In22 = Pin(1,Pin.OUT)
In33 = Pin(3,Pin.OUT)
In44 = Pin(19,Pin.OUT)
m1 = Stepper.create(In1,In2,In3,In4)
m2 = Stepper.create(In11,In22,In33,In44)
while True:
    m2.angle(360)# faire tourner le moteur pas a pas dans le sens de de l'aiguille
    m1.step(360,-1) # faire tourner le moteur pas a pas dans le sens inverse de l'aiguille
    sleep(1)
