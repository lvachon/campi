#! /usr/bin/python
from picamera.array import PiRGBArray
from picamera import PiCamera
import os
import numpy as np
import cv2
import time

width=1024
height=768

print("Getting camera")
camera = PiCamera()
camera.resolution = (width, height)
camera.framerate = 1
rawCapture = PiRGBArray(camera, size=(width, height))
camera.analog_gain = 1
camera.digital_gain = 1
camera.shutter_speed = 10000
camera.iso = 400
camera.exposure_mode = 'off'
camera.awb_mode = 'off'
camera.awb_gains = (1,1)
camera.framerate = 1
print("Starting loop")
while(1):
	f = open("./ramdisk/settings","r")
	if(f.mode=='r'):
		g = camera.awb_gains
		pairs = f.read().split(";")
		for pair in pairs:
			pairParts = pair.split(":")
			if(pairParts[0]=='again'):
				camera.analog_gain = pairParts[1]*1.0
			if(pairParts[0]=='dgain'):
				camera.digital_gain = pairParts[1]*1.0
			if(pairParts[0]=='shutter'):
				camera.shutter_speed = pairParts[1]*1.0
			if(pairParts[0]=='iso'):
				camera.iso = pairParts[1]*1.0
			if(pairParts[0]=='awbred'):
				camera.awb_gains = (g[0],pairParts[1]*1.0)
			if(pairParts[0]=='awbblue'):
				camera.awb_gains = (pairParts[1]*1.0, g[1])
	f.close()
	camera.capture('./ramdisk/frame.jpg')
	time.sleep(1000)

#
#	for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
#	print("Frame")
#	cleanImage = frame.array.copy()
#	
#		f = open("./html/ramdisk/autocmd","r")
#		if(f.mode=='r' and f.read()=="GO"):
#			if lMaxY<maxY and cMaxY<maxY and rMaxY<maxY:
#				os.system('cd html;./fwd.sh')
#				print("    No walls")
#			elif lMaxY<maxY and (rMaxY>maxY or cMaxY>maxY):
#				os.system('cd html;./left.sh')
#				print("    Going left")
#			elif rMaxY<maxY and (lMaxY>maxY or cMaxY>maxY):
#				os.system('cd html;./right.sh')
#				print("    Going right")
#			elif cMaxY>maxY or (lMaxY>maxY and rMaxY>maxY):
#				print("    Backing up")
#				os.system('cd html;./bwd.sh;./left.sh;./left.sh;./left.sh')
#		f.close()
#		#time.sleep(0.1)
#		print("    Writing images")
#		cv2.imwrite('./ramdisk/frame.jpg',cleanImage, [int(cv2.IMWRITE_JPEG_QUALITY), 33])
#	rawCapture.truncate(0)
#	laserOn = 1-laserOn

