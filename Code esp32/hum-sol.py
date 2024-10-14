from machine import Pin,ADC,PWM
from dht import DHT11
from time import sleep
from hcsr04 import HCSR04
humsol=Pin(39,Pin.IN)

while True:
    Hsol=humsol.value()
    print("Humidite sol:",Hsol)
#     if Hsol==1:
#         print("Arros en cours")
#         pompe1.value(1)
#         pompe2.value(0)
#     else:
#         print("Arros est arrter ")
#         pompe1.value(0)
#         pompe2.value(0)
    sleep(1)