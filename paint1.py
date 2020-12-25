import pyautogui, random
import time

time.sleep(3)


pyautogui.click()
ud = 200
r = 50
pyautogui.dragRel(r, 0, duration=0.4)
for i in range(10):
    ud = random.randrange(40, 300)
    pyautogui.dragRel(0, -ud, duration=0.4)
    pyautogui.dragRel(r, 0, duration=0.4)
    pyautogui.dragRel(0, ud, duration=0.4)
    pyautogui.dragRel(r, 0, duration=0.4)
    
     


