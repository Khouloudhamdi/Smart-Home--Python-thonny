from machine import Pin,ADC,PWM
from time import sleep
from BlynkLib import Blynk
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
#-----------capteur gaz-------------
gaz= Pin(36,Pin.IN)
#-----------ventilateur 01-------------
ventilo1=Pin(33,Pin.OUT)
ventilo1.value(01)
#-----------SERVO-Moteur---------
servo=PWM(Pin(15),freq=50)
servo.duty(25)
@blynk.on("V7")
def control_porte(value):
    if int(value[0]) == 1:
        servo.duty(75) 
    else:
        servo.duty(25)

while True:
    control_porte
# capteur de gaz_ventilo-moteur_buzzer
    gaz_value =gaz.value()
    print('Valeur du capteur MQ-2 :', gaz_value)
    blynk.virtual_write(3, gaz_value)
    if gaz_value==0:         #détection de gaz
        print('presence de gaz')
        ventilo1.value(0)
        servo.duty(75)
        sleep(1)
    else:
        print('absence de gaz')
        ventilo1.value(1)
        servo.duty(25)
    sleep(1)
    
    
    
    