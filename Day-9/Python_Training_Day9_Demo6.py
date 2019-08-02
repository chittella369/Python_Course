'''
Created on Mar 14, 2017

@author: junaid.latif.shaikh
'''
from tkinter import *

from tkinter.messagebox import showerror, showinfo, askyesno, showwarning,\
    askokcancel

showerror("Answer","Sorry, no data avaiable")


showinfo('No','Qiut has been cancelled')


askyesno('Verify','DO you want to quit')

showwarning('Yes', 'Not yet implemented')

askokcancel('Confirm',"DO you want to Stop")

mainloop()


"""
askokcancel(title=None, message=None, **options)
Ask if operation should proceed; return true if the answer is ok
askquestion(title=None, message=None, **options)
Ask a question
askretrycancel(title=None, message=None, **options)
Ask if operation should be retried; return true if the answer is yes
askyesno(title=None, message=None, **options)
Ask a question; return true if the answer is yes
askyesnocancel(title=None, message=None, **options)
Ask a question; return true if the answer is yes, None if cancelled.
showerror(title=None, message=None, **options)
Show an error message
showinfo(title=None, message=None, **options)
Show an info message
showwarning(title=None, message=None, **options)
Show a warning message



"""