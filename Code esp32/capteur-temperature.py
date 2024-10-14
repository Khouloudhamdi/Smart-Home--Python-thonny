from machine import Pin
from dht import DHT11
from time import sleep
dh=DHT11(Pin(23))
chauffage=Pin(1,Pin.OUT)


   
while True:
    dh.measure()
    T=dh.temperature()
    H=dh.humidity()
    print("temperature:",T,"humidite:=",H)
#     blynk.virtual_write(1, T)
#     blynk.virtual_write(2, H)
#     if T>23:
#         ventilo2.value(1)
#         print("ouverture de climatiseur")
#     else:
#         ventilo2.value(0)
#     if T<5:
#         chauffage.value(1)
#         print("ouverture de chauffage")
#     else:
#         chauffage.value(0)
    sleep(1)
        
    