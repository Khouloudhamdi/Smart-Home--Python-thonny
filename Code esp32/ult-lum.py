from machine import Pin,ADC
from BlynkLib import Blynk
from time import sleep
from hcsr04 import HCSR04
import network
from hcsr04 import HCSR04


# Entrez le SSID et le mot de passe de votre réseau Wi-Fi
ssid = 'iot'
password = '11111111'
# Initialisez l'interface Wi-Fi
wifi = network.WLAN(network.STA_IF)
# Activez l'interface Wi-Fi
wifi.active(True)
# Connectez-vous au réseau Wi-Fi
wifi.connect(ssid, password)
# Attendez que la connexion soit établie
while not wifi.isconnected():
    pass
# Affichez les informations sur la connexion Wi-Fi
print('Connexion Wi-Fi établie')
print('Adresse IP :', wifi.ifconfig()[0])
# Entrez les informations d'authentification de votre compte Blynk
#BLYNK_AUTH = '7Tndhg6ajFQnJnqunmc-VQYvgchqhrr3'
BLYNK_AUTH = '1NVysGyM_jcT8r3z81XuyVhQiSfQL6Ir'
# Initialisez l'objet Blynk
blynk = Blynk(BLYNK_AUTH)
#-----------Ultrason-------------
ultrason = HCSR04(trigger_pin=12,echo_pin=14,echo_timeout_us=1000000)
#-----------ampoule------------
ampoule=Pin(13,Pin.OUT)
photo=ADC(Pin(34))
while True:
    distance = ultrason .distance_cm()
    sleep(1)
    lum=photo.read()
    print(distance,'cm')
    print(lum)
    blynk.virtual_write(5,distance)
    blynk.virtual_write(6,lum)
    if lum<3000 and distance <15:
        ampoule.value(0)
    else:
        ampoule.value(1)
        sleep(1)
        
    
 
