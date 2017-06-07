#opencv install link for mac http://www.pyimagesearch.com/2015/06/15/install-opencv-3-0-and-python-2-7-on-osx/
#brew reinstall opencv3 --with-python3
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


#ImageGrab.grab_to_file('current.png')
#print "done with image"
#cv2.imread('current.png')
# def kill():
# 	while True:
# 		print "dongs"
# 		if cv2.waitKey(33) == ord('a'):
# 			sys.exit()

# def die():
# 	sys.exit()
# def handle_events(args):
# 	if args.current_key=='a':
# 		hk.stop()
# 		sys.exit()
'''
img_rgb = numpy.array(ImageGrab.grab().convert('RGB'))
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('tarr.png',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.90
loc = np.where( res >= threshold)
counter=0
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    counter=counter+1
print counter
cv2.imwrite('res.png',img_rgb)

'''
herbNum=23678

clicker=tk.Tk()
(bankx,banky)=(clicker.winfo_pointerx(),clicker.winfo_pointery())
numberofGoes=herbNum/28 +1 
counter=1
print numberofGoes
'''
img_rgb = numpy.array(ImageGrab.grab().convert('RGB'))
print "grabed"
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('tarr.png',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.90
loc = np.where( res >= threshold)
'''
#np.savetxt('inv.txt', zip(*loc[::-1]))
template = cv2.imread('tarr.png',0)
w, h = template.shape[::-1]
ptarr=np.loadtxt('inv.txt')


pyautogui.moveTo(bankx, banky)
pyautogui.click()
time.sleep(2)
print "read"
try:
	while counter<numberofGoes:
		a=None
		print counter
		

		pyautogui.moveTo(982, 365)	
		#pyautogui.click()
		time.sleep(.5)
		pyautogui.click(button='right')
		pyautogui.moveTo(987, 470)
		pyautogui.click()
		pyautogui.moveTo(1381, 285)
		pyautogui.click()
		time.sleep(1)
		
		'''
		if counter%5==0:
			img_rgb = numpy.array(ImageGrab.grab().convert('RGB'))
			print "grabedsant"
			img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
			template = cv2.imread('santa.png',0)
			w, h = template.shape[::-1]

			res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF)
			threshold = 0.95
			loclol = np.where( res >= threshold)
			print loclol
			ptl=None
			for ptk in zip(*loclol[::-1]):
				ptl=ptk
				break
			(bankx,banky) = ((2.0*ptl[0] +w)/4.0,(2.0*ptl[1] +h)/4.0)
		'''
		#x=None
		#y=None
		for pt in ptarr:
			
			pyautogui.moveTo((2.0*pt[0] +w)/4.0,(2.0*pt[1] +h)/4.0)
			#time.sleep(.01)
			pyautogui.click()
			#cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
			#x=(2.0*pt[0] +w)/4.0
			#y=(2.0*pt[1] +h)/4.0
		#cv2.imwrite('res.png',img_rgb)
		if counter%10==0:
			img_rgb = numpy.array(ImageGrab.grab().convert('RGB'))
			img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
			template = cv2.imread('herblol.png',0)
			w1, h1 = template.shape[::-1]

			res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
			threshold = 0.7
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
				print 'gg'
			except:
				print 'bc'
				pass
		
		
		pyautogui.moveTo(bankx, banky)
		pyautogui.click()	
		time.sleep(1.5)
		pyautogui.moveTo(2414, 1162)
		pyautogui.click(button='right')
		time.sleep(1)
		pyautogui.moveTo(2402, 1266)
		pyautogui.click()
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






	#time.sleep(.5)