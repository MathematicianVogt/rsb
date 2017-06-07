import Tkinter as tk
import time
import pyautogui
import Tkinter as tk
class Mouse:
	def __init__(self):
		self.root=tk.Tk()

	def currentPos(self):
		return (self.root.winfo_pointerx(),self.root.winfo_pointery())


clicker=tk.Tk()
(bankx,banky)=(clicker.winfo_pointerx(),clicker.winfo_pointery())
AMOUNT = 18494
totalGoes = 360
count=0
time.sleep(1)
pyautogui.moveTo(bankx,banky)
pyautogui.click()
time.sleep(2)
while count<=totalGoes:
	count=count+1
	
	pyautogui.moveTo(1130, 797)	
	pyautogui.click()
	time.sleep(2)
	pyautogui.click(button='right')
	pyautogui.moveTo(1100, 895)
	pyautogui.click()
	pyautogui.moveTo(1381, 285)
	pyautogui.click()


	
	
	pyautogui.moveTo(2377, 1157)
	pyautogui.click()
	time.sleep(1)
	pyautogui.moveTo(2414, 1162)
	pyautogui.click()
	time.sleep(1)

	pyautogui.moveTo(326, 1340)
	pyautogui.click(button='right')
	time.sleep(1)

	pyautogui.moveTo(309, 1408)
	pyautogui.click()
	time.sleep(2)
	pyautogui.typewrite('/55', interval=0.1) # type with quarter-second pause in between each key 
	time.sleep(2)
	pyautogui.press('enter')
	time.sleep(50)
	pyautogui.moveTo(bankx,banky)
	pyautogui.click()
	time.sleep(1)
	pyautogui.moveTo(2414, 1162)
	pyautogui.click(button='right')
	pyautogui.moveTo(2402, 1266)
	pyautogui.click()
	time.sleep(1)


	
