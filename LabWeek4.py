import time
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_pm25.i2c import PM25_I2C
reset_pin = None
import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout = 0.25)
from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)
print("Found PM2.5 sensor, reading data...")
meta_data = ["PM 1.0", "PM 2.5", "PM 10"]
import csv
f = open("data.csv", "w", newline = '')
writer = csv.writer(f)
writer.writerow(meta_data)

while True:
    time.sleep(1)

    try:
        aqdata = pm25.read()
        print(aqdata)
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue
    Itime = time.asctime(time.localtime())
    print(Itime)
    Utime = time.time
    print(Utime)
    print()
    print("Concentration Units (standard)")
    print("---------------------------------------")
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"])
    )
    print("Concentration Units (environmental)")
    print("---------------------------------------")
   )






  