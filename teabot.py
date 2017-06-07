import cv2
import numpy as np
import pyscreenshot as ImageGrab
import time
import pyautogui
from pprint import pprint 
import numpy
import sys
import thread
import Tkinter as tk

clicker=tk.Tk()

numberofGoes=10000
counter=1
time.sleep(1)
(bankx,banky)=(clicker.winfo_pointerx(),clicker.winfo_pointery())
try:
	while counter<numberofGoes:
	
		if counter%10==0:
			img_rgb = numpy.array(ImageGrab.grab().convert('RGB'))
			img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
			template = cv2.imread('tea.png',0)
			w1, h1 = template.shape[::-1]

			res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
			threshold = 0.8
			loc = np.where( res >= threshold)
			# for pt in zip(*loc[::-1]):
			#     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
			#     counter=counter+1
			# print counter
			
			# cv2.imwrite('res.png',img_rgb)
			try:
				a=zip(*loc[::-1])
				pts=a[0]
				(bankx,banky) =((2.0*pts[0] +w1)/4.0,(2.0*pts[1] +h1)/4.0)
				print 'not fucked'
			except:
				print 'fucked'
				pass
		
		
		pyautogui.moveTo(bankx, banky)
		pyautogui.click()
		time.sleep(1.5)	
		pyautogui.moveTo(2373, 1160)
		pyautogui.click(button='right')
		time.sleep(.5)
		pyautogui.moveTo(2351, 1221)
		pyautogui.click()

		pyautogui.click()
		time.sleep(3)
		
		
		'''
		time.sleep(1)
		pyautogui.moveTo(2373, 1163)
		pyautogui.click(button='right')
		time.sleep(1)
		pyautogui.moveTo(2362, 1238)
		pyautogui.click()
		time.sleep(1)
		'''
		counter=counter+1
except KeyboardInterrupt:
	sys.exit()