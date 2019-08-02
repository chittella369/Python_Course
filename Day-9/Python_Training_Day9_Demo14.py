'''
Created on Mar 15, 2017

@author: junaid.latif.shaikh
'''
import pyautogui

for i in range(10):
      pyautogui.moveRel(100, 0, duration=0.25)
      pyautogui.moveRel(0, 100, duration=0.25)
      pyautogui.moveRel(-100, 0, duration=0.25)
      pyautogui.moveRel(0, -100, duration=0.25)
      
      
      
      
""" The pyautogui.moveRel() function moves the mouse cursor relative to its current position. The following example moves the mouse in the same square pattern, except it begins the square from wherever the mouse happens to be on the screen when the code starts running:"""