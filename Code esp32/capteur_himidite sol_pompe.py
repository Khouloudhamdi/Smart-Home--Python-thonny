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
#-----------
#-----------capteur humidite sol-------------
humsol=Pin(39,Pin.IN)
# Définir une pompe
pompe1= Pin(03, Pin.OUT)
# Définir le broche de la LED
led = Pin(02, Pin.OUT)
@blynk.on("V0")
def control_led(value):
    if int(value[0]) == 1:
        led.on()
    else:
        led.off()
while True:
    Hsol=humsol.value()
    print("Humidite sol:",Hsol)
    blynk.virtual_write(4, Hsol)
    if Hsol==1:
        print("Arros en cours")
        pompe1.value(0)
    else:
        print("Arros est arrter ")
        pompe1.value(1)
    sleep(1)
