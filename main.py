#import os
#print(os.environ["BLINKA_FT232H"])
from pyftdi.ftdi import Ftdi
Ftdi().open_from_url('ftdi://ftdi:232h:1/1')
#Ftdi.show_devices()

import time
import board
import adafruit_bh1750

i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_bh1750.BH1750(i2c)

while True:
    print("%.2f Lux" % sensor.lux)
    time.sleep(1)

