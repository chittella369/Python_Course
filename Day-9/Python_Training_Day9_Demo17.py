'''
Created on Mar 14, 2017

@author: junaid.latif.shaikh
'''
from tkinter import *

def motion(event):
  print("Mouse position: (%s %s)" % (event.x, event.y))
  return

master = Tk()

msg = Message(master, text =" whatever_you_do")

msg.config(bg='lightgreen', font=('times', 24, 'italic'))

msg.bind('<Motion>',motion)

msg.pack()

mainloop()


""" Every time we move the mouse in the Message widget, the position of the mouse pointer will be printed.
 When we leave this widget, the function motion() is not called anymore. """