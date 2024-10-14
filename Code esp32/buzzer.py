from machine import Pin
from time import sleep

buzzer= Pin(23, Pin.OUT)

while True:
  # buzzer ON
  buzzer.value(1)
  sleep(1)
