import cv2
# from keras.models import load_model
import numpy as np
import os
from queue import Queue
import random
import time
#import mean
from statistics import mean

import pyautogui

import win32api


from win32api import GetSystemMetrics

Y_index=-1
X_index=-1
Width = GetSystemMetrics(0)
Height =GetSystemMetrics(1)

tuple_listl=[]

state_right = win32api.GetKeyState(0x02) 

for i in range(3):
	temp=[]
	for j in range(3):
		temp.append((int((Width/3)*j+int(Width/6)) , int(Height/3)*i + int(Height/6) ))
	tuple_listl.append(temp)



def main():
	global state_right

	file_name = cv2.imread("drivingf.jpg")
	window_name = "window"
	interframe_wait_ms = 30

	i=0
	stop=1
	while (stop):
		global tuple_listl

		file_name = cv2.imread("drivingf.jpg")
		window_name = "window"
		interframe_wait_ms = 30
		cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
		cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
	
		x, y, w, h = 900, 5, 350, 350
		file_name = cv2.flip(file_name, 1)
		hsv = cv2.cvtColor(file_name, cv2.COLOR_BGR2HSV)
		mask2 = cv2.inRange(hsv, np.array([2, 50, 60]), np.array([25, 150, 255]))
		res = cv2.bitwise_and(file_name, file_name, mask=mask2)
		gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
		median = cv2.GaussianBlur(gray, (5, 5), 0)

		kernel_square = np.ones((5, 5), np.uint8)
		dilation = cv2.dilate(median, kernel_square, iterations=2)
		opening = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel_square)
		ret, thresh = cv2.threshold(opening, 30, 255, cv2.THRESH_BINARY)
		thresh = thresh[y:y + h, x:x + w]
		global min_index
		if X_index!=-1 or Y_index !=-1:
			cv2.circle(file_name,tuple_listl[Y_index][X_index], 100, (255,255,0), -1)

		cv2.imshow(window_name, file_name)
		if cv2.waitKey(interframe_wait_ms) & 0x7F == ord('q'):
			break
