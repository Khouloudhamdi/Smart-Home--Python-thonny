from BlynkLib import Blynk
from machine import Pin,ADC
from time import sleep
import network
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
#-----------capteur DHT11-------------
d=DHT11(Pin(23))
#-----------ventilateur 02-------------
ventilo2=Pin(32,Pin.OUT)
ventilo2.value(1)
#-----------led(chauffage)-------------
chauffage=Pin(01,Pin.OUT)
chauffage.value(0)
while True:
    dh.measure()
    T=dh.temperature()
    H=dh.humidity()
    print("temperature:",T,"humidite:=",H)
    blynk.virtual_write(1, T)
    blynk.virtual_write(2, H)
    if T>23:
        ventilo2.value(0)
        print("ouverture de climatiseur")
    else:
        ventilo2.value(1)
    if T<23:
        chauffage.value(1)
        print("ouverture de chauffage")
    else:
        chauffage.value(0)
    sleep(1)