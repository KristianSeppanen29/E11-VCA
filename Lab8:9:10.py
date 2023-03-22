# coding=utf-8
 
import RPi.GPIO as GPIO
import datetime
import time
import csv
counts = 0
meta_data = [time, counts]
f = open("radiation_sensor_data", "w", newline = '') 
writer = csv.writer(f)
writer.writerow(meta_data)
data = GPIO.HIGH


 
def my_callback(channel):
     global counts 
     counts+=1
    

  
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)
GPIO.add_event_detect(5, GPIO.FALLING, callback=my_callback)


 

start_time = time.time
big_time = start_time+60
while time.time<=big_time:
    message = raw_input('\nPress any key to exit.\n')
    time.sleep(10)
    currenttime = time.time
    counts = counts
    writer = csv.writer(f)
    writer.writerow([currenttime, counts])
    counts = 0


    
    


#It wants to give out the time and counts detected during that time
    # Set up the system so that it detects falling edges 
    #Set a function that does something when it detects a falling edge. 
    #While loop for an infinite time in that while loop, you want to have a global count variable and you want it to sleep for a minute and then record about the current time and how many counts there are. 
    #You need to set global variable so that for the next run of the loop, the count starts from 0. 
    # Before reseting global variable, write current time and how many counts of time there are.
