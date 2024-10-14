from machine import Pin
from time import sleep

led = Pin(32, Pin.OUT) # Broche de la LED
pir = Pin(4, Pin.IN) # Broche du capteur PIR

while True:
    pirval=pir.value()
    if pirval==1:
        print('Mouvement détecté :=',pirval)
        led.value(1) # Allume la LED
    else:
        led.value(0) # Eteint la LED
        print('aucune Mouvement:=',pirval)
        sleep(1)