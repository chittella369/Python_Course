'''
Created on Mar 14, 2017

@author: junaid.latif.shaikh
'''

from tkinter import *


def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()



root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()

