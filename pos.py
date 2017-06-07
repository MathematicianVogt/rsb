import Tkinter as tk
import time
import pyautogui
class Mouse:
	def __init__(self):
		self.root=tk.Tk()
		print "luls"

	def currentPos(self):
		return (self.root.winfo_pointerx(),self.root.winfo_pointery())


mo=Mouse()
AMOUNT = 1000
totalGoes = (AMOUNT/150) +1
count=0

while True:
	print mo.currentPos()
	time.sleep(1)