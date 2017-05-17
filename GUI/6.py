# from tkinter import *
# from tkinter import ttk
#
# root = Tk()
#
# def get_data(event):
#     print("String: ",stringVariable.get())
#     print("Integer: ",intVar.get())
#     print("Double: ",doubleVariable.get())
#     print("Boolean: ",booleanVariable1.get() )
#
#
# def bind_button(event):
#     if (booleanVariable1.get() ):#If any is 0
#         print(booleanVariable1.get() )
#         getdataButton.unbind('<Button-1>')
#     else:
#         print(booleanVariable1.get() )#If both 1
#         getdataButton.bind("<Button-1>",get_data)
#
#
#
# stringVariable = StringVar()
# intVar = IntVar()
# doubleVariable = DoubleVar()
# booleanVariable1 = BooleanVar()
# booleanVariable2 = BooleanVar()
#
# stringVariable.set("String in here")
# intVar.set("Integer in here")
# doubleVariable.set("Double in here")
# booleanVariable1.set(True)
# booleanVariable2.set(True)
#
# stringEntry = Entry(root,textvariable = stringVariable)
# stringEntry.pack(side=LEFT)
#
# intEntry = Entry(root,textvariable = intVar)
# intEntry.pack(side=LEFT)
#
# doubleEntry = Entry(root,textvariable = doubleVariable)
# doubleEntry.pack(side=LEFT)
#
#
# thecheckbutton = Checkbutton(root,file.txt="Switch1",variable=booleanVariable1)
# thecheckbutton.bind("<Button-1>",bind_button)
# thecheckbutton.pack(side=LEFT)
#
# # thecheckbutton2 = Checkbutton(root,file.txt="Switch2",variable=booleanVariable2)
# # thecheckbutton2.bind("<Button-1>",bind_button)
# # thecheckbutton2.pack(side=LEFT)
#
# getdataButton = Button(root,file.txt="Get Data")
# getdataButton.bind("<Button-1>",get_data)
# getdataButton.pack(side=LEFT)
#
#
# root.mainloop()



# from string import *  # Required to call maketrans function.

# intab = "!()-[]{};:'\"\,<>./?@#$%^&*_~"
# outtab ="                            "
# trantab = str.maketrans(intab, outtab)
#
# strr = "this is string !()-[]{};:'\"\,<>./?@#$%^&*_~example....wow!!!";
# print (strr.translate(trantab))
#
# import subprocess as sp
# programName = "notepad.exe"
# fileName = "file.txt"
#
# hello =sp.Popen([programName, fileName])
# print(hello)

#!/usr/bin/python

# import os, sys
#
# # Open a file
# path = "C:\\eula.1028.txt"
# fd = os.open( path, os.O_RDWR|os.O_CREAT )
#
# # Close opened file
# os.close( fd )
#
# # Now create another copy of the above file.
# dst = "/tmp/foo.txt"
# os.link( path, dst)
#
# print ("Created hard link successfully!!")
print('<a href="file:///C:\\eula.1028.txt">example text</a>')
