import Tkinter as tk
import time
import pyautogui

clicker=tk.Tk()
(bankx,banky)=(clicker.winfo_pointerx(),clicker.winfo_pointery())

counter=0
maxc=2000
while(counter<maxc):
	counter=counter+1
	pyautogui.moveTo(bankx, banky)
	pyautogui.click()
	time.sleep(2.5)