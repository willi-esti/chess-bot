#from pyautogui import *
import pyautogui, time



x = None
while True:
	x = pyautogui.locateCenterOnScreen('wr.png', confidence=0.8)
	if x != None:
		print(x[0])
		pyautogui.moveTo(x[0], x[1], duration=0.2)
	else:
		print('Ko')
	time.sleep(1)





