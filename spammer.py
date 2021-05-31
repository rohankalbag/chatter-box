import pyautogui,time

def tag(n,name, message):
      '''
      Enter the number of times needed to tag the person, first few letters of the name of the contact saved
      and also the message that you want to mention in the tag.
      '''
      time.sleep(1)
      for i in range(n):
            pyautogui.typewrite("@"+name)
            pyautogui.press("enter")
            pyautogui.typewrite(" "+ message)
            pyautogui.press("enter")

def songspam(filename):
      '''
      store the lyrics in a file and then store this file in the same directory of the .py file filename is a string with the name of the .txt file
      '''
      f = open(filename)
      a = f.readlines()
      time.sleep(5)
      for i in a:
            pyautogui.typewrite(i)
            pyautogui.press("enter")
      f.close()

def deletespam(n,msg):
      ''' A function to enter a message, delete it n times, takes an int and a string, the whatsapp must be in full screen with resolution 1920X1080'''     
      time.sleep(5)
      for i in range(n):
            pyautogui.typewrite(msg)
            pyautogui.press("enter")
            time.sleep(0.5)
            pyautogui.moveTo(1769,907,0.1)
            pyautogui.click(1769,907)
            pyautogui.moveTo(1670,858,0.1)
            pyautogui.click(1670,858)
            pyautogui.moveTo(1051,647,0.1)
            pyautogui.click(1051,647)
            time.sleep(0.5)

def emojipyramid(n):
      time.sleep(5)
      for i in range(1,n+1):
            pyautogui.keyDown('shift')
            pyautogui.keyDown('tab')
            time.sleep(0.1)
            pyautogui.keyUp('shift')
            pyautogui.keyUp('tab')
            pyautogui.press("enter")
            for j in range(1,i+1):
                  pyautogui.keyDown('shift')
                  pyautogui.keyDown('tab')
                  time.sleep(0.1)
                  pyautogui.keyUp('shift')
                  pyautogui.keyUp('tab')
                  time.sleep(0.1)
                  pyautogui.press("down")
                  pyautogui.press('right')
                  time.sleep(0.1)
                  pyautogui.press('enter')
            pyautogui.press("enter")
            time.sleep(0.3)


if __name__ =='__main__': 
    #main block
    print("Hello World")