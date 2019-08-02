'''
Created on Mar 14, 2017

@author: junaid.latif.shaikh
'''
from tkinter import  *



master = Tk()

lab = Label(master, text="Seelct Language you Know").grid(row=0,stick=W)


var1 = IntVar()
Checkbutton(master, text="Python", variable=var1).grid(row=1, sticky=W)

var2 = IntVar()
Checkbutton(master, text="Java", variable=var2).grid(row=2, sticky=W)

mainloop()


""" Each checkbox needs a different variable name (IntVar()) """
