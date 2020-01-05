import tkinter
from tkinter import *

val = ""
result=0
op=""

def r3b1_clicked():
    global val
    val=val+"1"
    dt.set(val)

def r3b2_clicked():
    global val
    val=val+"2"
    dt.set(val)

def r3b3_clicked():
    global val
    val=val+"3"
    dt.set(val)

def r2b1_clicked():
    global val
    val=val+"4"
    dt.set(val)

def r2b2_clicked():
    global val
    val=val+"5"
    dt.set(val)

def r2b3_clicked():
    global val
    val=val+"6"
    dt.set(val)

def r1b1_clicked():
    global val
    val=val+"7"
    dt.set(val)

def r1b2_clicked():
    global val
    val=val+"8"
    dt.set(val)

def r1b3_clicked():
    global val
    val=val+"9"
    dt.set(val)

def r4b2_clicked():
    global val
    val=val+"0"
    dt.set(val)

def r1b4_clicked():
    global val
    global op
    global result
    result=int(val)
    val=val+"+"
    op="+"
    dt.set(val)

def r2b4_clicked():
    global val
    global op
    global result
    result=int(val)
    val=val+"-"
    op="-"
    dt.set(val)

def r3b4_clicked():
    global val
    global op
    global result
    result=int(val)
    val=val+"*"
    op="*"
    dt.set(val)

def r4b4_clicked():
    global val
    global op
    global result
    result=int(val)
    val=val+"/"
    op="/"
    dt.set(val)

def r4b1_clicked():
    global val
    global op
    global result
    result=0
    val=""
    op=""
    dt.set(val)

def r4b3_clicked():
    global val
    global op
    global result
    temp=val
    if op=="+":
        result+=int(temp.split("+")[1])
    elif op=="-":
        result-=int(temp.split("-")[1])
    elif op=="*":
        result*=int(temp.split("*")[1])
    elif op=="/":
        x=int(temp.split("/")[1])
        if x==0:
            result="Zero error"
        else:
            result=result//x
    val=str(result)
    dt.set(val)
    

root=tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("My Calculator")

dt=StringVar()

lb=Label(
    root,
    text="Label",
    anchor=SE,
    font=("Verdana",24),
    textvariable= dt,
    background="#FFF",
    fg="#000",
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
    command=r1b1_clicked,
)

r1b1.pack(side=LEFT,expand=True,fill="both",)

r1b2=Button(
    row1,
    text= "8",
    font= ("Verdana",22),
    relief=GROOVE,
    border=0,
    command=r1b2_clicked,
)

r1b2.pack(side=LEFT,expand=True,fill="both",)

r1b3=Button(
    row1,
    text= "9",
    font= ("Verdana",22),
    relief=GROOVE,
    border=0,
    command=r1b3_clicked,
)

r1b3.pack(side=LEFT,expand=True,fill="both",)

r1b4=Button(
    row1,
    text= "+",
    font= ("Verdana",22),
    relief=GROOVE,
    border=0,
    command=r1b4_clicked,
)

r1b4.pack(side=LEFT,expand=True,fill="both",)

r2b1=Button(
    row2,
    text= "4",
    font= ("Verdana",22),
    relief=GROOVE,
    border=0,
    command=r2b1_clicked,
)

r2b1.pack(side=LEFT,expand=True,fill="both",)

r2b2=Button(
    row2,
    text= "5",
    font= ("Verdana",22),
    relief=GROOVE,
    border=0,
    command=r2b2_clicked,
)

r2b2.pack(side=LEFT,expand=True,fill="both",)

r2b3=Button(
    row2,
    text= "6",
    font= ("Verdana",22),
    relief=GROOVE,
    border=0,
    command=r2b3_clicked,
)

r2b3.pack(side=LEFT,expand=True,fill="both",)

r2b4=Button(
    row2,
    text= "-",
    font= ("Verdana",22),relief=GROOVE,
    border=0,
    command=r2b4_clicked,
)

r2b4.pack(side=LEFT,expand=True,fill="both",)

r3b1=Button(
    row3,
    text= "1",
    font= ("Verdana",22),relief=GROOVE,
    border=0,
    command=r3b1_clicked,
)

r3b1.pack(side=LEFT,expand=True,fill="both",)

r3b2=Button(
    row3,
    text= "2",
    font= ("Verdana",22),relief=GROOVE,
    border=0,
    command=r3b2_clicked,
)

r3b2.pack(side=LEFT,expand=True,fill="both",)

r3b3=Button(
    row3,
    text= "3",
    font= ("Verdana",22),relief=GROOVE,
    border=0,
    command=r3b3_clicked,
)

r3b3.pack(side=LEFT,expand=True,fill="both",)

r3b4=Button(
    row3,
    text= "*",
    font= ("Verdana",22),relief=GROOVE,
    border=0,
    command=r3b4_clicked,
)

r3b4.pack(side=LEFT,expand=True,fill="both",)


r4b1=Button(
    row4,
    text= "C",
    font= ("Verdana",22),relief=GROOVE,
    border=0,
    command=r4b1_clicked,
)

r4b1.pack(side=LEFT,expand=True,fill="both",)

r4b2=Button(
    row4,
    text= "0",
    font= ("Verdana",22),relief=GROOVE,
    border=0,
    command=r4b2_clicked,
)

r4b2.pack(side=LEFT,expand=True,fill="both",)

r4b3=Button(
    row4,
    text= "=",
    font= ("Verdana",22),relief=GROOVE,
    border=0,
    command=r4b3_clicked,
)

r4b3.pack(side=LEFT,expand=True,fill="both",)

r4b4=Button(
    row4,
    text= "/",
    font= ("Verdana",22),relief=GROOVE,
    border=0,
    command=r4b4_clicked,
)

r4b4.pack(side=LEFT,expand=True,fill="both",)

root.mainloop()