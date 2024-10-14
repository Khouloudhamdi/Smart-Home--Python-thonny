from machine import UART
import os

# Initialize the UART connection to the ESP32-CAM
uart = UART(2, baudrate=115200, rx=16, tx=17, timeout=10)
os.dupterm(uart)

# Take a photo and save it to the local file system
def take_photo():
  uart.write(b'\r\n')
  uart.write(b'import sensor\r\n')
  uart.write(b'sensor.reset()\r\n')
  uart.write(b'import time\r\n')
  uart.write(b'import image\r\n')
  uart.write(b'clock = time.clock()\r\n')
  uart.write(b'sensor.set_pixformat(sensor.RGB565)\r\n')
  uart.write(b'sensor.set_framesize(sensor.QVGA)\r\n')
  uart.write(b'sensor.run(1)\r\n')
  uart.write(b'clock.tick()\r\n')
  uart.write(b'img = sensor.snapshot()\r\n')
  uart.write(b'img.save("image.jpg")\r\n')

# Call the function to take a photo
take_photo()
