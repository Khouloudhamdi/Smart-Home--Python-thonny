from machine import Pin,SoftI2C
from dht import DHT11
from time import sleep
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

# LCD
i2c = SoftI2C(scl=Pin(22), sda=Pin(21),freq=100000)
lcd = I2cLcd(i2c, 0x27,2,16)
lcd.clear()
# DHT11
d=DHT11(Pin(23))
#-----------ventilateur 02-------------
ventilo2=Pin(32,Pin.OUT)
#-----------led(chauffage)-------------
chauffage=Pin(1,Pin.OUT)
ventilo2.value(1)
chauffage.value(0)
while True:
    d.measure()
    t = d.temperature()
    h = d.humidity()
    print('DHT11:',t,h)
    temp = 'Temp:{:.0f} C'.format(t)
    lcd.clear()
    lcd.putstr(temp = 'Temp:{:.0f} C'.format(t))
    sleep(1)
    if t>20:
        ventilo2.value(0)
        print("ouverture de climatiseur")
    else:
        ventilo2.value(1)
    if t<10:
        chauffage.value(1)
        print("ouverture de chauffage")
    else:
        chauffage.value(0)
    sleep(1)
    
        
    