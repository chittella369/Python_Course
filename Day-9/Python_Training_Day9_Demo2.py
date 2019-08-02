'''
Created on Mar 14, 2017

@author: junaid.latif.shaikh
'''
from tkinter import *

root = Tk()

w = Label(root, text="Enter your details in below text field")
w.pack()



T = Text(root, height=2, width=30)
T.pack()


T.insert(END, "Just a text Widget\nin two lines\n")


mainloop()
