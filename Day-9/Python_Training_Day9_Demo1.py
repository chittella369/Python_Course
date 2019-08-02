'''
Created on Mar 14, 2017

@author: junaid.latif.shaikh
'''
from tkinter import *

root = Tk()
message = Message(root,text="This is a basic GUI demo")

#message.config(bg='lightgreen', font=('times', 24, 'italic')
message.config(bg='Red', font=('times',23,'italic'))
               
message.pack()

root.mainloop()