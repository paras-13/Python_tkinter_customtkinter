# Python GUI calculator
from tkinter import *
from tkinter import messagebox as tmsg
# functions
# Back-end Code


def zero():
    print("Hello")


def one():
    print("Hi")


def two():
    print("Hello")


def three():
    print("Hello")


def four():
    print("Hello")


def five():
    print("Hello")


def six():
    print("Hello")


def seven():
    print("Hello")


def eight():
    print("Hello")


def nine():
    print("Hello")


def decimal():
    print("Hello")


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


Label(cal, text="Calculator", font="20px", fg="yellow", bg="black").place(x=120, y=15)
name = Entry(cal, width=19, font="Arial 24", justify=RIGHT)
name.place(x=0, y=115)
photo = PhotoImage(file="clear.png")

# Buttons

btn1 = Button(cal, image=photo, height=42, width=72, command=del_, bg="#282828", bd=5)
btn1.place(x=260, y=165)
changeOnHover(btn1, "#383838", "#282828")

btn2 = Button(cal, text="C", font="Times 19", height=1, width=5, command=c_, fg="#ffffff", bg="#282828", bd=3)
btn2.place(x=177, y=165)
changeOnHover(btn2, "#383838", "#282828")

btn3 = Button(cal, text="CE", font="Times 19", height=1, width=5, command=ce_, fg="#ffffff", bg="#282828", bd=3)
btn3.place(x=92, y=165)
changeOnHover(btn3, "#383838", "#282828")

btn4 = Button(cal, text=chr(37), font="Times 19", height=1, width=5, command=per, fg="#ffffff", bg="#282828", bd=3)
btn4.place(x=10, y=165)
changeOnHover(btn4, "#383838", "#282828")

btn5 = Button(cal, text=chr(247), font="Times 19", height=1, width=5, command=div, fg="#ffffff", bg="#282828", bd=3)
btn5.place(x=260, y=220)
changeOnHover(btn5, "#383838", "#282828")

btn6 = Button(cal, text="\u221A", font="Times 19", height=1, width=5, command=undr, fg="#ffffff", bg="#282828", bd=3)
btn6.place(x=177, y=220)
changeOnHover(btn6, "#383838", "#282828")

btn7 = Button(cal, text="x^2", font="Times 19", height=1, width=5, command=sqr, fg="#ffffff", bg="#282828", bd=3)
btn7.place(x=94, y=220)
changeOnHover(btn7, "#383838", "#282828")

btn8 = Button(cal, text="1/x", font="Times 19", height=1, width=5, command=opr2, fg="#ffffff", bg="#282828", bd=3)
btn8.place(x=11, y=220)
changeOnHover(btn8, "#383838", "#282828")

btn9 = Button(cal, text="x", font="Times 19",  height=1, width=5, command=mul, fg="#ffffff", bg="#282828", bd=3)
btn9.place(x=260, y=275)
changeOnHover(btn9, "#383838", "#282828")

btn10 = Button(cal, text="9", font="Times 19", height=1, width=5, command=nine, bg="#383838", fg="#ffffff", bd=3)
btn10.place(x=177, y=275)
changeOnHover(btn10, "#282828", "#383838")

btn11 = Button(cal, text="8", font="Times 19", height=1, width=5, command=eight, bg="#383838", fg="#ffffff", bd=3)
btn11.place(x=94, y=275)
changeOnHover(btn11, "#282828", "#383838")

btn24 = Button(cal, text="7", font="Times 19", height=1, width=5, command=seven, bg="#383838", fg="#ffffff", bd=3)
btn24.place(x=11, y=275)
changeOnHover(btn24, "#282828", "#383838")

btn12 = Button(cal, text="-", font="Times 19", height=1, width=5, command=sub, fg="#ffffff", bg="#282828", bd=3)
btn12.place(x=260, y=330)
changeOnHover(btn12, "#383838", "#282828")

btn13 = Button(cal, text="6", font="Times 19", height=1, width=5, command=six, bg="#383838", fg="#ffffff", bd=3)
btn13.place(x=177, y=330)
changeOnHover(btn13, "#282828", "#383838")

btn14 = Button(cal, text="5", font="Times 19", height=1, width=5, command=five, bg="#383838", fg="#ffffff", bd=3)
btn14.place(x=94, y=330)
changeOnHover(btn14, "#282828", "#383838")

btn15 = Button(cal, text="4", font="Times 19", height=1, width=5, command=four, bg="#383838", fg="#ffffff", bd=3)
btn15.place(x=11, y=330)
changeOnHover(btn15, "#282828", "#383838")

btn16 = Button(cal, text="+", font="Times 19", height=1, width=5, command=add, fg="#ffffff", bg="#282828", bd=3)
btn16.place(x=260, y=385)
changeOnHover(btn16, "#383838", "#282828")

btn17 = Button(cal, text="3", font="Times 19", height=1, width=5, command=three, bg="#383838", fg="#ffffff", bd=3)
btn17.place(x=177, y=385)
changeOnHover(btn17, "#282828", "#383838")

btn18 = Button(cal, text="2", font="Times 19", height=1, width=5, command=two, bg="#383838", fg="#ffffff", bd=3)
btn18.place(x=94, y=385)
changeOnHover(btn18, "#282828", "#383838")

btn19 = Button(cal, text="1", font="Times 19", height=1, width=5, command=one, bg="#383838", fg="#ffffff", bd=3)
btn19.place(x=11, y=385)
changeOnHover(btn19, "#282828", "#383838")

btn20 = Button(cal, text="=", font="Times 19", height=1, width=5, command=equal, fg="#000", bg="#ff8257", bd=5)
btn20.place(x=260, y=440)
changeOnHover(btn20, "#ff9057", "#ff8257")

btn21 = Button(cal, text=".", font="Times 19", height=1, width=5, command=decimal, fg="#ffffff", bg="#282828", bd=3)
btn21.place(x=177, y=440)
changeOnHover(btn21, "#383838", "#282828")

btn22 = Button(cal, text="0", font="Times 19", height=1, width=5, command=zero, fg="#ffffff", bg="#282828", bd=3)
btn22.place(x=92, y=440)
changeOnHover(btn22, "#383838", "#282828")

btn23 = Button(cal, text="+/-", font="Times 19", height=1, width=5, command=opr1, fg="#ffffff", bg="#282828", bd=3)
btn23.place(x=10, y=440)
changeOnHover(btn23, "#383838", "#282828")

cal.mainloop()
