# Python GUI calculator
from tkinter import *
from tkinter import messagebox as tmsg
# functions
# Back-end Code


num = ""
operator = ""


def zero():
    global num
    num += "0"
    equation.set(num)


def one():
    global num
    num += "1"
    equation.set(num)


def two():
    global num
    num += "2"
    equation.set(num)


def three():
    global num
    num += "3"
    equation.set(num)


def four():
    global num
    num += "4"
    equation.set(num)


def five():
    global num
    num += "5"
    equation.set(num)


def six():
    global num
    num += "6"
    equation.set(num)


def seven():
    global num
    num += "7"
    equation.set(num)


def eight():
    global num
    num += "8"
    equation.set(num)


def nine():
    global num
    num += "9"
    equation.set(num)


def decimal():
    global num
    num += "."
    equation.set(num)


def add():
    print("Hello")


def sub():
    print("Hello")


def mul():
    print("Hello")


def div():
    print("Hello")


def equal():
    print("Hello")


def sqr():
    print("Hello")


def undr():
    print("Hello")


def opr1():
    print("Hello")


def opr2():
    print("Hello")


def c_():
    print("Hello")


def ce_():
    print("Hello")


def del_():
    print("Hello")


def per():
    print("Hello")


def changeOnHover(button, colorOnHover, colorOnLeave):
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))


# Front-end Code

cal = Tk()                                                      # Screen

cal.title("Calculator")                                         # Screen Title

cal.geometry("350x500")                                         # Screen-Size

cal.configure(bg="#101010")                                        # Screen Background Color

cal.maxsize(350, 500)                                           # Screen Max Size

cal.minsize(350, 500)                                           # Screen Min Size

cal.wm_iconbitmap("calc.ico")                                # Calculator icon

equation = StringVar()
Label(cal, text="Calculator", font="20px", fg="yellow", bg="black").place(x=120, y=15)
Entry(cal, width=19, font="Calibri 25", textvariable=equation, justify=RIGHT,
      bg="#101010", fg="white").place(x=11, y=100)

photo = PhotoImage(file="clear.png")
Label(cal, text="- By Paras Upadhyay", font="Calibri 8 bold italic", bg="#101010", fg="white").place(x=247, y=480)
# Buttons

btn1 = Button(cal, image=photo, height=42, width=72, command=del_, bg="#282828", fg="white", bd=5)
btn1.place(x=260, y=155)
changeOnHover(btn1, "#383838", "#282828")

btn2 = Button(cal, text="C", font="Times 19", height=1, width=5, command=c_, fg="#ffffff", bg="#282828", bd=3)
btn2.place(x=177, y=155)
changeOnHover(btn2, "#383838", "#282828")

btn3 = Button(cal, text="CE", font="Times 19", height=1, width=5, command=ce_, fg="#ffffff", bg="#282828", bd=3)
btn3.place(x=92, y=155)
changeOnHover(btn3, "#383838", "#282828")

btn4 = Button(cal, text=chr(37), font="Times 19", height=1, width=5, command=per, fg="#ffffff", bg="#282828", bd=3)
btn4.place(x=10, y=155)
changeOnHover(btn4, "#383838", "#282828")

btn5 = Button(cal, text=chr(247), font="Times 19", height=1, width=5, command=div, fg="#ffffff", bg="#282828", bd=3)
btn5.place(x=260, y=210)
changeOnHover(btn5, "#383838", "#282828")

btn6 = Button(cal, text="\u221A", font="Times 19", height=1, width=5, command=undr, fg="#ffffff", bg="#282828", bd=3)
btn6.place(x=177, y=210)
changeOnHover(btn6, "#383838", "#282828")

btn7 = Button(cal, text="x^2", font="Times 19", height=1, width=5, command=sqr, fg="#ffffff", bg="#282828", bd=3)
btn7.place(x=94, y=210)
changeOnHover(btn7, "#383838", "#282828")

btn8 = Button(cal, text="1/x", font="Times 19", height=1, width=5, command=opr2, fg="#ffffff", bg="#282828", bd=3)
btn8.place(x=11, y=210)
changeOnHover(btn8, "#383838", "#282828")

btn9 = Button(cal, text="x", font="Times 19",  height=1, width=5, command=mul, fg="#ffffff", bg="#282828", bd=3)
btn9.place(x=260, y=265)
changeOnHover(btn9, "#383838", "#282828")

btn10 = Button(cal, text="9", font="Times 19", height=1, width=5, command=nine, bg="#383838", fg="#ffffff", bd=3)
btn10.place(x=177, y=265)
changeOnHover(btn10, "#282828", "#383838")

btn11 = Button(cal, text="8", font="Times 19", height=1, width=5, command=eight, bg="#383838", fg="#ffffff", bd=3)
btn11.place(x=94, y=265)
changeOnHover(btn11, "#282828", "#383838")

btn24 = Button(cal, text="7", font="Times 19", height=1, width=5, command=seven, bg="#383838", fg="#ffffff", bd=3)
btn24.place(x=11, y=265)
changeOnHover(btn24, "#282828", "#383838")

btn12 = Button(cal, text="-", font="Times 19", height=1, width=5, command=sub, fg="#ffffff", bg="#282828", bd=3)
btn12.place(x=260, y=320)
changeOnHover(btn12, "#383838", "#282828")

btn13 = Button(cal, text="6", font="Times 19", height=1, width=5, command=six, bg="#383838", fg="#ffffff", bd=3)
btn13.place(x=177, y=320)
changeOnHover(btn13, "#282828", "#383838")

btn14 = Button(cal, text="5", font="Times 19", height=1, width=5, command=five, bg="#383838", fg="#ffffff", bd=3)
btn14.place(x=94, y=320)
changeOnHover(btn14, "#282828", "#383838")

btn15 = Button(cal, text="4", font="Times 19", height=1, width=5, command=four, bg="#383838", fg="#ffffff", bd=3)
btn15.place(x=11, y=320)
changeOnHover(btn15, "#282828", "#383838")

btn16 = Button(cal, text="+", font="Times 19", height=1, width=5, command=add, fg="#ffffff", bg="#282828", bd=3)
btn16.place(x=260, y=375)
changeOnHover(btn16, "#383838", "#282828")

btn17 = Button(cal, text="3", font="Times 19", height=1, width=5, command=three, bg="#383838", fg="#ffffff", bd=3)
btn17.place(x=177, y=375)
changeOnHover(btn17, "#282828", "#383838")

btn18 = Button(cal, text="2", font="Times 19", height=1, width=5, command=two, bg="#383838", fg="#ffffff", bd=3)
btn18.place(x=94, y=375)
changeOnHover(btn18, "#282828", "#383838")

btn19 = Button(cal, text="1", font="Times 19", height=1, width=5, command=one, bg="#383838", fg="#ffffff", bd=3)
btn19.place(x=11, y=375)
changeOnHover(btn19, "#282828", "#383838")

btn20 = Button(cal, text="=", font="Times 19", height=1, width=5, command=equal, fg="#000", bg="#ff8257", bd=3)
btn20.place(x=260, y=430)
changeOnHover(btn20, "#ff9057", "#ff8257")

btn21 = Button(cal, text=".", font="Times 19", height=1, width=5, command=decimal, fg="#ffffff", bg="#282828", bd=3)
btn21.place(x=177, y=430)
changeOnHover(btn21, "#383838", "#282828")

btn22 = Button(cal, text="0", font="Times 19", height=1, width=5, command=zero, fg="#ffffff", bg="#282828", bd=3)
btn22.place(x=92, y=430)
changeOnHover(btn22, "#383838", "#282828")

btn23 = Button(cal, text="+/-", font="Times 19", height=1, width=5, command=opr1, fg="#ffffff", bg="#282828", bd=3)
btn23.place(x=10, y=430)
changeOnHover(btn23, "#383838", "#282828")

cal.mainloop()
