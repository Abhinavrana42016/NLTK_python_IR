from tkinter import *
from tkinter import ttk

root = Tk()

def get_data(event):
    print("String: ",stringVariable.get())
    print("Integer: ",intVar.get())
    print("Double: ",doubleVariable.get())
    print("Boolean: ",booleanVariable1.get() )


def bind_button(event):
    if (booleanVariable1.get() ):#If any is 0
        print(booleanVariable1.get() )
        getdataButton.unbind('<Button-1>')
    else:
        print(booleanVariable1.get() )#If both 1
        getdataButton.bind("<Button-1>",get_data)



stringVariable = StringVar()
intVar = IntVar()
doubleVariable = DoubleVar()
booleanVariable1 = BooleanVar()
booleanVariable2 = BooleanVar()

stringVariable.set("String in here")
intVar.set("Integer in here")
doubleVariable.set("Double in here")
booleanVariable1.set(True)
booleanVariable2.set(True)

stringEntry = Entry(root,textvariable = stringVariable)
stringEntry.pack(side=LEFT)

intEntry = Entry(root,textvariable = intVar)
intEntry.pack(side=LEFT)

doubleEntry = Entry(root,textvariable = doubleVariable)
doubleEntry.pack(side=LEFT)


thecheckbutton = Checkbutton(root,text="Switch1",variable=booleanVariable1)
thecheckbutton.bind("<Button-1>",bind_button)
thecheckbutton.pack(side=LEFT)

# thecheckbutton2 = Checkbutton(root,text="Switch2",variable=booleanVariable2)
# thecheckbutton2.bind("<Button-1>",bind_button)
# thecheckbutton2.pack(side=LEFT)

getdataButton = Button(root,text="Get Data")
getdataButton.bind("<Button-1>",get_data)
getdataButton.pack(side=LEFT)


root.mainloop()