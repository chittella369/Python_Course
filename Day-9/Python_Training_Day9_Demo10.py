'''
Created on Mar 14, 2017

@author: junaid.latif.shaikh
'''
from tkinter import *
import sys;

def hello(event):
    print("Single Click, Button-l") 
    
def quit(event):                           
    print("Double Click, so let's stop") 
    sys.exit() 


widget = Button(None, text='Mouse Clicks')

widget.pack()

""" The left mouse button is defined by the event <Button-1> """
widget.bind('<Button-1>', hello)

"""Similar to the Button event, see above, but the button is double clicked instead of a single click."""

widget.bind('<Double-1>', quit) 

widget.mainloop()