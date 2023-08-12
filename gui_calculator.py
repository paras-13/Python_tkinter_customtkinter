# Python GUI calculator
from tkinter import *
from tkinter import messagebox as tmsg
# functions


def hello():
    tmsg.showinfo(title="info", message="This is a number")


def hello7():
    tmsg.showinfo("info", "You are clicking number 7")


cal = Tk()
cal.title("Calculator")
cal.geometry("350x500")
cal.maxsize(350, 500)
cal.minsize(350, 500)
cal.wm_iconbitmap("Calicon.ico")
Label(cal, text="Calculator", font="20px", fg="yellow", bg="black").place(x=120, y=15)
name = Entry(cal, width=50, font="Arial 24")
name.place(x=0, y=50)

Button(cal, text="x", font="Times 20", height=1, width=5, command=hello).place(x=260, y=150)
Button(cal, text="9", font="Times 20", height=1, width=5, command=hello).place(x=179, y=150)
Button(cal, text="8", font="Times 20", height=1, width=5, command=hello).place(x=92, y=150)
Button(cal, text="7", font="Times 20", height=1, width=5, command=hello7).place(x=5, y=150)

Button(cal, text="-", font="Times 20", height=1, width=5, command=hello).place(x=260, y=205)
Button(cal, text="6", font="Times 20", height=1, width=5, command=hello).place(x=179, y=205)
Button(cal, text="5", font="Times 20", height=1, width=5, command=hello).place(x=92, y=205)
Button(cal, text="4", font="Times 20", height=1, width=5, command=hello).place(x=5, y=205)

Button(cal, text="+", font="Times 20", height=1, width=5, command=hello).place(x=260, y=260)
Button(cal, text="3", font="Times 20", height=1, width=5, command=hello).place(x=179, y=260)
Button(cal, text="2", font="Times 20", height=1, width=5, command=hello).place(x=92, y=260)
Button(cal, text="1", font="Times 20", height=1, width=5, command=hello).place(x=5, y=260)

Button(cal, text="=", font="Times 20", height=1, width=5, command=hello).place(x=260, y=315)
Button(cal, text=".", font="Times 20", height=1, width=5, command=hello).place(x=179, y=315)
Button(cal, text="0", font="Times 20", height=1, width=5, command=hello).place(x=92, y=315)
Button(cal, text="+/-", font="Times 20", height=1, width=5, command=hello).place(x=5, y=315)

cal.mainloop()
