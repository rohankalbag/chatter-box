import pyautogui,time

def tag(n,name, message):
      time.sleep(1)
      for i in range(n):
            pyautogui.typewrite("@"+name)
            pyautogui.press("enter")
            pyautogui.typewrite(" "+ message)
            pyautogui.press("enter")

def songspam(filename):
      f = open(filename)
      a = f.readlines()
      time.sleep(5)
      for i in a:
            pyautogui.typewrite(i)
            pyautogui.press("enter")
      f.close()

def deletespam(n):
      time.sleep(5)
      for i in range(n):
            pyautogui.typewrite("ok")
            pyautogui.press("enter")
            time.sleep(0.5)
            pyautogui.moveTo(1769,907,0.1)
            pyautogui.click(1769,907)
            pyautogui.moveTo(1670,858,0.1)
            pyautogui.click(1670,858)
            pyautogui.moveTo(1051,647,0.1)
            pyautogui.click(1051,647)
            time.sleep(0.5)