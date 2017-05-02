from tkinter import *
from tkinter import ttk

root = Tk()

# frame = Frame(root)

Label(root, text="First Name").grid(row=0, sticky=W,padx=4)
Entry(root,width = 20).grid(row=0,column=1,sticky=E,pady=4)

Label(root, text="Last Name").grid(row=1, sticky=W,padx= 4)
Entry(root).grid(row=1,column=1,sticky=E,pady=4)

button = Button(root,text = "Submit").grid(row=3)
# frame.pack()
root.mainloop()