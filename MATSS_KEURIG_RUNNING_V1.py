#!/usr/bin/env python

import RPi.GPIO as GPIO
import datetime
import time 
import os
import sys
import glob
import subprocess


buttonPin = 17  #pin input button is attached to
ledPin = 18  #pin output led is attached to

snapshot_path = '/home/pi/testing/snapshots/' #path to folder containing all of the snapshots
latest_path = '/var/www/html/images/' #path to folder to place the latest snapshots

number_shots = 16  #number of pics to move to webpage folder

GPIO.setmode(GPIO.BCM)

GPIO.setup(buttonPin,GPIO.IN)
GPIO.setup(ledPin,GPIO.OUT)


#button debounce variable
prev_input = 0

while True:

  #reset led 
  GPIO.output(ledPin, GPIO.LOW)

  #take reading
  input = GPIO.input(buttonPin)

  #timestamp filename
  prefix = "capture"
  suffix = datetime.datetime.now().strftime("%m%d%y_%H%M%S")
  filename = "_".join([prefix,suffix]) #e.g. filename = capture_072417_190355.jpg

  #if the last button was lon and this on high, print
  if ((not prev_input) and input):
    #print("Button Pressed")             #debug output statement
    GPIO.output(ledPin, GPIO.HIGH)      #led indicator flash
    #os call to raspistill delay timer of 5 ms, no preview, output file to ./snapshots dir
    os.system('raspistill -t 5 -n -o ' + snapshot_path + filename + '.jpg')

    #file manipulation section

    #write file into webpage image folder
    os.system('cp ' + snapshot_path + filename + '.jpg ' + latest_path)                           

    #create list of file names in web images folder
    file_list = sorted(
      glob.glob(os.path.join(latest_path, '*.jpg')), key=os.path.getctime, reverse=False)

    #delete all but the latest X number of files

    for i in xrange(len(file_list)-number_shots):
        temp_filename = file_list[i]
        os.system('rm ' + temp_filename)


  #update previous input
  prev_input = input

  #slight pause to debounce
  time.sleep(0.05)


