'''
Created on Mar 15, 2017

@author: junaid.latif.shaikh
'''


import pyautogui

pyautogui.typewrite('\n Hello world!')                 # prints out "Hello world!" instantly
pyautogui.typewrite('\n Hello world!', interval=0.150)  # prints out "Hello world!" with a quarter second delay after each character




"""The primary keyboard function is typewrite(). This function will type the characters in the string is passed. To add a delay interval in between pressing each character key, pass an int or float for the interval keyword argument."""