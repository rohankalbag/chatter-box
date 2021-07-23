import pyautogui,time
import random
import csv

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

def emojipyramid(n,emoji_name):
      '''n is the no of rows of the emoji pyramid that you want, and emoji_name is the string version of emoji 
         for example for smile with pain (:pain)'''
      time.sleep(3)
      for i in range(0,n):
            for j in range(0,i+1):
                  pyautogui.typewrite(emoji_name)
                  time.sleep(0.1)
                  pyautogui.press("enter")
            time.sleep(1)
            pyautogui.press("enter")

def randomisespam(n):
      #n is the no of times you want to spam
      ''' Save the name of your contact (first few letters also works) and message value pairs in a csv file called data.csv stored in same directory
          for example
          name1, message1,
          name2, message2,
          '''
      f = open("data.csv",'r')
      data = csv.reader(f)
      people, messages = [],[]
      for line in data:
            people += [line[0]]
            messages += [line[1]]
      for i in range(n):
            j = random.randint(0,len(people)-1)
            k = random.randint(0,len(messages)-1)
            tag(1, people[j], messages[k])