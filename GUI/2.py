from tkinter import *
from tkinter import ttk

root = Tk()

frame = Frame(root)

Label(frame,text = "LABEL").pack()

Button(frame, text="Button1").pack(side = LEFT, fill = Y)
Button(frame, text="Button2").pack(side = RIGHT, fill = X)
Button(frame, text="Button3").pack(side = LEFT, fill = X)
Button(frame, text="Button4").pack(side = RIGHT, fill = Y)


frame.pack()

root.mainloop()
