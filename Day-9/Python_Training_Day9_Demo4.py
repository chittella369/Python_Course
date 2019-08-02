'''
Created on Mar 14, 2017

@author: junaid.latif.shaikh
'''
from tkinter import *
root = Tk()

v = IntVar()

Label(root,  text="""Choose Your Gender :""", justify = LEFT, padx = 20).pack()

Radiobutton(root,  text="Female", padx = 20,  variable=v,  value=1).pack(anchor=W)

Radiobutton(root,  text="Male", padx = 20,  variable=v,  value=2).pack(anchor=W)

mainloop()
