'''
Created on Mar 15, 2017

@author: junaid.latif.shaikh
'''
import pyautogui

pyautogui.keyDown('ctrl')
pyautogui.keyDown('shift')
pyautogui.keyDown('esc')
pyautogui.keyUp('esc')
pyautogui.keyUp('shift')
pyautogui.keyUp('ctrl')