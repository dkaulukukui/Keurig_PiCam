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

snapshot_path = 'snapshots/' #path to folder containing all of the snapshots
latest_path = 'recent_snapshots/' #path to folder to place the latest snapshots

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
    print("Button Pressed")             #debug output statement
    GPIO.output(ledPin, GPIO.HIGH)      #led indicator flash
    #os call to raspistill delay timer of 5 ms, no preview, output file to ./snapshots dir
    os.system('raspistill -t 5 -n -o ./snapshots/' + filename + '.jpg')

    #file manipulation section
    
    #create a list of snapshot files 
    file_list = sorted(
      glob.iglob(os.path.join(snapshot_path, '*')), key=os.path.getctime, reverse=True)  #create sorted list of files

    os.system('mv recent_snapshots/* ../trash/')                  #delete old set of recent files (move to trash)

    for i in xrange(4):  #copy 4 most recent files to another dir	
      temp_filename = file_list[i]
      os.system('cp ' + temp_filename + ' recent_snapshots/')                           

    #print file_list


  #update previous input
  prev_input = input

  #slight pause to debounce
  time.sleep(0.05)


