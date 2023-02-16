import time
import board
import busio
import argparse
import sys
import adafruit_bme680
print(sys.argv)
i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)
bme680.sea_level_pressure = 1013.25
from digitalio import DigitalInOut, Direction, Pull
from adafruit_pm25.i2c import PM25_I2C
reset_pin = None
import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout = 0.95)
from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)
print("Found PM2.5 sensor, reading data...")
meta_data = ["PM 1.0", "PM 2.5", "PM 10", "temperature", "gas", "relative humidity", "pressure", "altitude"]
import csv
start_time = time.time()
run_time = int(sys.argv[1])
itime = start_time
f = open("data.csv", "w", newline = '')
writer = csv.writer(f)
writer.writerow(meta_data)

while itime < (start_time + run_time):
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
    print("\nTemperature: %0.1f C" % bme680.temperature)
    print("Gas: %d ohm" % bme680.gas)
    print("Humidty: %0.3f %%" % bme680.relative_humidity)
    print("Pressure: %0.3f  hPa" %bme680.pressure)
    print("Altitude = %0.2f meters " % bme680.altitude)
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
    data = (aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"], bme680.temperature,bme680.gas,bme680.pressure,bme680.altitude,bme680.relative_humidity,Utime)
    writer.writerow(data)




