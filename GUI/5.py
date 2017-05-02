from tkinter import *
from tkinter import ttk
def getsum(event):
    val1=int(num1Entry.get())
    val2=int(num2Entry.get())
    sum=val1+val2

    OutPutEntry.delete(0,"end")

    OutPutEntry.insert(0,sum)

root = Tk()

num1Entry = Entry(root)
num1Entry.pack(side=LEFT)

Label(root,text="+").pack(side=LEFT)

num2Entry = Entry(root)
num2Entry.pack(side=LEFT)

buttonequal=Button(root,text ="=")
buttonequal.bind('<Button-1>',getsum)
buttonequal.pack(side=LEFT)
OutPutEntry = Entry(root)
OutPutEntry.pack(side=LEFT)


root.mainloop()