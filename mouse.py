import pyautogui
import os
import win32api
import time

import main2
import time
mouse_length=0
mouse2_length=0
def mouse():
	
	state_left = win32api.GetKeyState(0x01)
	global mosue_length
	global mouse2_length

	i=1
	mouse=[]
	mouse2=[]
	while i<11:
		a = win32api.GetKeyState(0x01)
		if a != state_left:
			state_left = a
			if a < 0:
				if i!=0 and i%3==0:
					main2.average=1
				if i!=10:
					mouse.append(pyautogui.position())
					#mouse2.append(pyautogui.position())
					mouse_length=len(mouse)
					#mouse2_length=len(mouse2)
				else:
					main2.stop_con=0
				time.sleep(0.01)
				#if(mouse_length>main2.eye_coordinates_left_length):					
					#mouse.pop()
				#if(mouse2_length>main2.eye_coordinates_right_length):
					#mouse2.pop()


				i+=1
	return mouse







