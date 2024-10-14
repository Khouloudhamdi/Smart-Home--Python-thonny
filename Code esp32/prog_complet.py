from BlynkLib import Blynk
from machine import Pin,ADC,PWM
from dht import DHT11
from time import sleep
import network
from hcsr04 import HCSR04


# Entrez le SSID et le mot de passe de votre réseau Wi-Fi
ssid = 'hamdi'
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

# Définir le broche de la LED
led = Pin(2, Pin.OUT)
#-----------capteur DHT11-------------
dh=DHT11(Pin(23))
#-----------capteur gaz MQ2-------------
gaz= ADC(Pin(36))
#-----------capteur humidite sol-------------
humsol=Pin(39,Pin.IN)
#-----------Ultrason-------------
ultrason = HCSR04(trigger_pin=12,echo_pin=14,echo_timeout_us=1000000)
#-----------capteur de lumiere-------------
photo=ADC(Pin(34))
#-----------SERVO-Moteur---------
servo=PWM(Pin(15),freq=50)
servo.duty(25)

@blynk.on("V0")
def control_led(value):
    if int(value[0]) == 1:
        led.on()
    else:
        led.off()
@blynk.on("V7")
def control_porte(value):
    if int(value[0]) == 1:
        servo.duty(75) 
    else:
        servo.duty(25)  
@blynk.on("V1")
def read_dht_data():
    dh.measure()
    T=dh.temperature()
    H=dh.humidity()
    print("temperature:",T,"humidite:=",H)
    blynk.virtual_write(2, H)
def read_Gaz():
    gaz_value = gaz.read()
    print('Valeur du capteur MQ-2 :', gaz_value)
    blynk.virtual_write(3, gaz_value)
def read_humsol():
    Hsol=humsol.value()
    print("Humidite sol:",Hsol)
    blynk.virtual_write(4, Hsol)
    if Hsol==1:
        print("Arros en cours")
        #pompe1.value(0)
        blynk.virtual_write(8, 0)
    else:
        print("Arros est arrter ")
        #pompe1.value(1)
        blynk.virtual_write(8, 1)



def read_ultrason_LDR():
    distance = ultrason.distance_cm()
    lum=photo.read()
    print("Distance = ",distance,'cm',"lumiere = ",lum)
    blynk.virtual_write(5,distance)
    blynk.virtual_write(6,lum)
while True:
    blynk.run()
    read_dht_data()
    read_Gaz()
    read_humsol()
    read_ultrason_LDR()
    control_porte
    sleep(5)