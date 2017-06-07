import Tkinter as tk
import time
import pyautogui
import ctypes
import random
import time
import math
class Mouse:
	def __init__(self):
		self.root=tk.Tk()

	def currentPos(self):
		return (self.root.winfo_pointerx(),self.root.winfo_pointery())

def move_mouse(pos):
	root=tk.Tk()
	x_pos, y_pos = pos
	screen_size = (root.winfo_screenwidth(),root.winfo_screenheight())
	x = 65536L * x_pos / screen_size[0] + 1
	y = 65536L * y_pos / screen_size[1] + 1
	return pyautogui.moveTo(x_pos, y_pos)

def random_movement(top_left_corner, bottom_right_corner, min_speed=100, max_speed=200):
	'''speed is in pixels per second'''
	shaft_clicked=False
	feather_clicked=False
	x_bound = top_left_corner[0], bottom_right_corner[0]
	y_bound = top_left_corner[1], bottom_right_corner[1]

	pos = (random.randrange(*x_bound),
	random.randrange(*y_bound))

	speed = min_speed + random.random()*(max_speed-min_speed)
	direction = 2*math.pi*random.random()

	def get_new_val(min_val, max_val, val, delta=0.01):
		new_val = val + random.randrange(-1,2)*(max_val-min_val)*delta
		if new_val<min_val or new_val>max_val:
			return get_new_val(min_val, max_val, val, delta)
		return new_val
		
	steps_per_second = 35.0
	counting=0
	while True:
		move_mouse(pos)
		time.sleep(1.0/steps_per_second) 

		speed = get_new_val(min_speed, max_speed, speed)
		direction+=random.randrange(-1,2)*math.pi/5.0*random.random()

		new_pos = (int(round(pos[0]+speed*math.cos(direction)/steps_per_second)),
		int(round(pos[1]+speed*math.sin(direction)/steps_per_second)))

		while new_pos[0] not in xrange(*x_bound) or new_pos[1] not in xrange(*y_bound):
			direction  = 2*math.pi*random.random()
			new_pos = (int(round(pos[0]+speed*math.cos(direction)/steps_per_second)),
			int(round(pos[1]+speed*math.sin(direction)/steps_per_second)))
			if math.fabs(new_pos[0]-top_left_corner[0])<5 or math.fabs(new_pos[0]-bottom_right_corner[0])<5 :
				pyautogui.click()
				counting+=1
				if counting%2==0:
					counting=1
					time.sleep(1.5)  
					pyautogui.moveTo(259, 1353)
					pyautogui.click(button='right')
					pyautogui.moveTo(240, 1407)
					pyautogui.click() 
					time.sleep(13)
					
					pyautogui.click()



		pos=new_pos


def random_movement_go_to(top_left_corner, bottom_right_corner, min_speed=100, max_speed=200):
	'''speed is in pixels per second'''
	shaft_clicked=False
	feather_clicked=False
	x_bound = top_left_corner[0], bottom_right_corner[0]
	y_bound = top_left_corner[1], bottom_right_corner[1]

	pos = (random.randrange(*x_bound),
	random.randrange(*y_bound))

	speed = min_speed + random.random()*(max_speed-min_speed)
	direction = 2*math.pi*random.random()

	def get_new_val(min_val, max_val, val, delta=0.01):
		new_val = val + random.randrange(-1,2)*(max_val-min_val)*delta
		if new_val<min_val or new_val>max_val:
			return get_new_val(min_val, max_val, val, delta)
		return new_val
		
	steps_per_second = 35.0
	counting=0
	while True:
		move_mouse(pos)
		time.sleep(1.0/steps_per_second) 

		speed = get_new_val(min_speed, max_speed, speed)
		direction+=random.randrange(-1,2)*math.pi/5.0*random.random()

		new_pos = (int(round(pos[0]+speed*math.cos(direction)/steps_per_second)),
		int(round(pos[1]+speed*math.sin(direction)/steps_per_second)))

		while new_pos[0] not in xrange(*x_bound) or new_pos[1] not in xrange(*y_bound):
			direction  = 2*math.pi*random.random()
			new_pos = (int(round(pos[0]+speed*math.cos(direction)/steps_per_second)),
			int(round(pos[1]+speed*math.sin(direction)/steps_per_second)))
			if math.fabs(new_pos[0] - 259)<5 and math.fabs(new_pos[1]-1353)<5:
				pyautogui.click(button='right')



		pos=new_pos









	
mo=Mouse()
AMOUNT = 5000
totalGoes = (AMOUNT/150) +1
count=0

# while count<=totalGoes:
# 	lbox=(2376,1156)
# 	rbox=(2418,1159)
# 	random_movement(lbox,rbox)
# 	time.sleep(1.5)  
# 	pyautogui.moveTo(259, 1353)
# 	pyautogui.click(button='right')
# 	pyautogui.moveTo(240, 1407)
# 	pyautogui.click() 
# 	time.sleep(13)

lbox=(2376,1156)
rbox=(2418,1159)
random_movement(lbox,rbox)




