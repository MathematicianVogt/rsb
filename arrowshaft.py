import Tkinter as tk
import time
import pyautogui
class Mouse:
	def __init__(self):
		self.root=tk.Tk()

	def currentPos(self):
		return (self.root.winfo_pointerx(),self.root.winfo_pointery())


mo=Mouse()
AMOUNT = 5000
totalGoes = (AMOUNT/150) +1
count=0

while count<=totalGoes:
	pyautogui.moveTo(2376, 1156)
	pyautogui.click()
	pyautogui.moveTo(2418, 1159)
	pyautogui.click()
	time.sleep(1.5)  
	pyautogui.moveTo(259, 1353)
	pyautogui.click(button='right')
	pyautogui.moveTo(240, 1407)
	pyautogui.click() 
	time.sleep(13)


	
