from tkinter import *

# if you are working under Python 3, comment the previous line and comment out the following line
#from tkinter import *

root = Tk()

fred = Button(root,  text="QUIT", fg="red",
                         command=quit)
fred .pack(side=RIGHT)
root.mainloop()



