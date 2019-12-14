import tkinter
from tkinter import *


root=tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("My Calculator")

lb=Label(
    root,
    text="Label",
    anchor=SE,
    font=("Verdana",24),
)

lb.pack(expand=True,fill="both",)

row1=Frame(root)
row1.pack(expand=TRUE,fill="both",)
row2=Frame(root)
row2.pack(expand=TRUE,fill="both",)
row3=Frame(root)
row3.pack(expand=TRUE,fill="both",)
row4=Frame(root)
row4.pack(expand=TRUE,fill="both",)

r1b1=Button(
    row1,
    text= "7",
    font= ("Verdana",22),
    relief=GROOVE,
    border=0,
)

r1b1.pack(side=LEFT,expand=True,fill="both",)

r1b2=Button(
    row1,
    text= "8",
    font= ("Verdana",22),
    relief=GROOVE,
    border=0,
)

r1b2.pack(side=LEFT,expand=True,fill="both",)

r1b3=Button(
    row1,
    text= "9",
    font= ("Verdana",22),
    relief=GROOVE,
    border=0,
)

r1b3.pack(side=LEFT,expand=True,fill="both",)

r1b4=Button(
    row1,
    text= "+",
    font= ("Verdana",22),
    relief=GROOVE,
    border=0,
)

r1b4.pack(side=LEFT,expand=True,fill="both",)

r2b1=Button(
    row2,
    text= "4",
    font= ("Verdana",22),
    relief=GROOVE,
    border=0,
)

r2b1.pack(side=LEFT,expand=True,fill="both",)

r2b2=Button(
    row2,
    text= "5",
    font= ("Verdana",22),
    relief=GROOVE,
    border=0,
)

r2b2.pack(side=LEFT,expand=True,fill="both",)

r2b3=Button(
    row2,
    text= "6",
    font= ("Verdana",22),
    relief=GROOVE,
    border=0,
)

r2b3.pack(side=LEFT,expand=True,fill="both",)

r2b4=Button(
    row2,
    text= "-",
    font= ("Verdana",22),relief=GROOVE,
    border=0,
)

r2b4.pack(side=LEFT,expand=True,fill="both",)






r3b1=Button(
    row3,
    text= "1",
    font= ("Verdana",22),relief=GROOVE,
    border=0,
)

r3b1.pack(side=LEFT,expand=True,fill="both",)

r3b2=Button(
    row3,
    text= "2",
    font= ("Verdana",22),relief=GROOVE,
    border=0,
)

r3b2.pack(side=LEFT,expand=True,fill="both",)

r3b3=Button(
    row3,
    text= "3",
    font= ("Verdana",22),relief=GROOVE,
    border=0,
)

r3b3.pack(side=LEFT,expand=True,fill="both",)

r3b4=Button(
    row3,
    text= "*",
    font= ("Verdana",22),relief=GROOVE,
    border=0,
)

r3b4.pack(side=LEFT,expand=True,fill="both",)









r4b1=Button(
    row4,
    text= ".",
    font= ("Verdana",22),relief=GROOVE,
    border=0,
)

r4b1.pack(side=LEFT,expand=True,fill="both",)

r4b2=Button(
    row4,
    text= "0",
    font= ("Verdana",22),relief=GROOVE,
    border=0,
)

r4b2.pack(side=LEFT,expand=True,fill="both",)

r4b3=Button(
    row4,
    text= "%",
    font= ("Verdana",22),relief=GROOVE,
    border=0,
)

r4b3.pack(side=LEFT,expand=True,fill="both",)

r4b4=Button(
    row4,
    text= "/",
    font= ("Verdana",22),relief=GROOVE,
    border=0,
)

r4b4.pack(side=LEFT,expand=True,fill="both",)

root.mainloop()