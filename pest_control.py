import cv2
import numpy as np
from matplotlib import pyplot as plt
import pyscreenshot as ImageGrab
import Tkinter
import time
import pyautogui
from pprint import pprint 
import numpy
import sys
import thread

img_rgb = numpy.array(ImageGrab.grab().convert('RGB'))
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('grimmy_guam.png',0)
w, h = template.shape[::-1]

plank = cv2.imread('plank.jpg',0)
creat=cv2.imread('creat.jpg',0)
start_loc=cv2.imread('start.jpg',0)
we_here=cv2.imread('wehere.jpg',0)


counter=0
while True:
	#time.sleep(2)
	img_rgb = numpy.array(ImageGrab.grab().convert('RGB'))
	img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
	w, h = creat.shape[::-1]
	res = cv2.matchTemplate(img_gray,creat,cv2.TM_CCOEFF_NORMED)
	threshold = 0.5
	loc = np.where( res >= threshold)
	counter=counter+1
	print counter
	for pt in zip(*loc[::-1]):
		
		pyautogui.moveTo((2.0*pt[0] +w)/4.0,(2.0*pt[1] +h)/4.0)
		time.sleep(.5)
		pyautogui.click()
		

