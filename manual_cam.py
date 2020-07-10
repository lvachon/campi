#! /usr/bin/python
from picamera.array import PiRGBArray
from picamera import PiCamera
from fractions import Fraction

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
oline=""
try:
	while(camera.capture_continuous('/home/pi/campi/ramdisk/buffer.jpg')):

		f = open("/home/pi/campi/ramdisk/settings","r")
		if(f.mode=='r'):
			g = camera.awb_gains
			line = f.read()
			if(line!=oline):
				oline=line
				print("new settings")
				pairs = line.split(";")
				for pair in pairs:
					pairParts = pair.split(":")
					#if(pairParts[0]=='again'):
					#	camera.analog_gain = pairParts[1]*1.0
					#if(pairParts[0]=='dgain'):
					#	camera.digital_gain = pairParts[1]*1.0
					if(pairParts[0]=='shutter'):
						camera.framerate = Fraction(1000000,int(pairParts[1]))
						camera.shutter_speed = int(pairParts[1])

					if(pairParts[0]=='iso'):
						iso = int(pairParts[1])
						if(iso>-1 and iso<801):
							camera.iso = int(pairParts[1])
					if(pairParts[0]=='brightness'):
						bright = int(pairParts[1])
						if(bright>-1 and bright<101):
							camera.brightness = int(pairParts[1])
					if(pairParts[0]=='contrast'):
						contrast = int(pairParts[1])
						if(contrast>-101 and contrast<101):
							camera.contrast = int(pairParts[1])
					if(pairParts[0]=='awbred'):
						g = (float(pairParts[1]),g[1])
					if(pairParts[0]=='awbblue'):
						g = (g[0],float(pairParts[1]))
					if(pairParts[0]=='exposure'):
						camera.exposure_mode = pairParts[1]
				camera.awb_gains = g
		f.close()
		print("frame")
		if(camera.framerate>1):
			time.sleep(1)
		os.system('cp /home/pi/campi/ramdisk/buffer.jpg /home/pi/campi/ramdisk/frame.jpg')
		
except:
	print("ERR")
finally:
	camera.close();
