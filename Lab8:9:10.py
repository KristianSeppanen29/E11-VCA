# coding=utf-8
 
import RPi.GPIO as GPIO
import datetime
import time
metadata = "radiation"
f = open("radiation_sensor_data", "w", newline = '') 
writer = csv.writer(f)
writer.writerow(meta_data)
data = GPIO.HIGH

 
def my_callback(channel):
    if GPIO.input(channel) == GPIO.HIGH:
        global counts 
        counts+=1
    

  
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)
GPIO.add_event_detect(5, GPIO.BOTH, callback=my_callback)


 

starttime = time.time
while time.time<=start_time+60:
    message = raw_input('\nPress any key to exit.\n')
    writer.writerow(data)
    global counts
    counts = counts
    time.sleep(10)
f = open("radiation_sensor_data.csv", "w", newline = '')
writer = csv.writer(f)
writer.writerow(currenttime, count)
currenttime = time.time
count = counts


#It wants to give out the time and counts detected during that time

    # Set up the system so that it detects falling edges 
    #Set a function that does something when it detects a falling edge. 
    #While loop for an infinite time in that while loop, you want to have a global count variable and you want it to sleep for a minute and then record about the current time and how many counts there are. 
    #You need to set global variable so that for the next run of the loop, the count starts from 0. 
    # Before reseting global variable, write current time and how many counts of time there are.
