#! /usr/bin/python
from picamera.array import PiRGBArray
from picamera import PiCamera
import os
import time

width=1024
height=768

print("Getting camera")
camera = PiCamera()
camera.start_preview();
time.sleep(2);
camera.stop_preview();
camera.resolution = (width, height)
camera.framerate = 1
rawCapture = PiRGBArray(camera, size=(width, height))
#camera.analog_gain = 1
#camera.digital_gain = 1
camera.shutter_speed = 10000
camera.iso = 400
camera.exposure_mode = 'off'
camera.awb_mode = 'off'
#camera.awb_gains = (1,1)
camera.framerate = 1
camera.rotation = 180
print("Starting loop")
while(1):
	f = open("./ramdisk/settings","r")
	if(f.mode=='r'):
		g = camera.awb_gains
		pairs = f.read().split(";")
		for pair in pairs:
			pairParts = pair.split(":")
			#if(pairParts[0]=='again'):
			#	camera.analog_gain = pairParts[1]*1.0
			#if(pairParts[0]=='dgain'):
			#	camera.digital_gain = pairParts[1]*1.0
			if(pairParts[0]=='shutter'):
				camera.framerate = 1000000/int(pairParts[1])
				camera.shutter_speed = int(pairParts[1])

			if(pairParts[0]=='iso'):
				iso = int(pairParts[1])
				if(iso>-1 and iso<801):
					camera.iso = int(pairParts[1])
			if(pairParts[0]=='awbred'):
				g = (float(pairParts[1]),g[1])
			if(pairParts[0]=='awbblue'):
				g = (g[0],float(pairParts[1]))
			if(pairParts[0]=='exposure'):
				camera.exposure_mode = pairParts[1]
		camera.awb_gains = g
	f.close()
	camera.capture('./ramdisk/buffer.jpg')
	os.system('cp ./ramdisk/buffer.jpg ./ramdisk/frame.jpg')
	time.sleep(1)

