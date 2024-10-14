from machine import Pin
from dht import DHT11
from time import sleep
dh=DHT11(Pin(23))
while True:
    dh.measure()
    T=dh.temperature()
    H=dh.humidity()
    print("temperature:",T,"humidite:=",H)
    sleep(1)
        
    