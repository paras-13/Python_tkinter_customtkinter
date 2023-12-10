# Python GUI calculator
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox as tmsg
# functions
# Back-end Code

exp = ""
opr = ""
N1 = 0


def zero():
    global exp
    exp += "0"
    equation.set(exp)


def one():
    global exp
    exp += "1"
    equation.set(exp)


def two():
    global exp
    exp += "2"
    equation.set(exp)


def three():
    global exp
    exp += "3"
    equation.set(exp)


def four():
    global exp
    exp += "4"
    equation.set(exp)


def five():
    global exp
    exp += "5"
    equation.set(exp)


def six():
    global exp
    exp += "6"
    equation.set(exp)


def seven():
    global exp
    exp += "7"
    equation.set(exp)


def eight():
    global exp
    exp += "8"
    equation.set(exp)


def nine():
    global exp
    exp += "9"
    equation.set(exp)


def decimal():
    global exp
    exp += "."
    equation.set(exp)


def addition():
    global exp
    global opr
    global N1
    N1 = float(exp)
    exp += "+"
    opr = "+"
    equation.set(exp)


def subtract():
    global opr
    global exp
    global N1
    N1 = float(exp)
    exp += "-"
    opr = "-"
    equation.set(exp)


def product():
    global exp
    global opr
    global N1
    N1 = float(exp)
    exp += "x"
    opr = "x"
    equation.set(exp)


def divison():
    global exp
    global opr
    global N1
    N1 = float(exp)
    exp += '\u00F7'
    opr = '\u00F7'
    equation.set(exp)


def equal():
    global N1
    global opr
    global exp
    temp_exp = exp
    if opr == "+":
        var1 = float((temp_exp.split("+")[1]))
        var2 = str(N1 + var1)
        equation.set(var2)
        exp = var2
    elif opr == "-":
        var1 = float((temp_exp.split("-")[1]))
        var2 = str(N1 - var1)
        equation.set(var2)
        exp = var2
    elif opr == "x":
        var1 = float((temp_exp.split("x")[1]))
        var2 = str(N1 * var1)
        equation.set(var2)
        exp = var2
    elif opr == '\u00F7':
        var1 = float((temp_exp.split('\u00F7')[1]))
        if var1 == 0:
            equation.set("Zero Division Error")
            tmsg.showerror(":(", "Error")
            N1 == ""
            exp = ""
        else:
            var2 = float(N1 / var1)
            var2 = round(var2, 10)
            temp = str(var2)
            if len(temp.split(".")[1]) > 10:
                equation.set("{:.10f}".format(var2))
                exp = str(var2)
            else:
                equation.set(var2)
                exp = str(var2)
    elif opr == "^2":
        var1 = float(temp_exp.split("^2")[0])
        var2 = str(var1*var1)
        equation.set(var2)
        exp = var2
    elif opr == "\u221A":
        var1 = float(temp_exp.split("\u221A")[1])
        var2 = str(var1**0.5)
        equation.set(var2)
        exp = var2

def square():
    global opr
    global exp
    opr = "^2"
    exp += "^2"
    equation.set(exp)


def underoot():
    global exp
    global opr
    exp += "\u221A"
    opr = "\u221A"
    equation.set(exp)


def opr1():
    tmsg.showinfo("Info","Under Development...Sorry for incovenience")


def opr2():
    global exp
    val = round(1/int(exp), 10)
    val = str(val)
    equation.set(val)
    exp = val

def clear():
    global exp
    exp = ""
    equation.set(exp)


def allClear():
    global opr
    global exp
    global N1
    exp = ""
    opr = ""
    N1 = 0
    equation.set(exp)


def backSpace():
    global exp
    length = len(exp)
    temp = ""
    for i in range(length-1):
        temp += exp[i]
    exp = temp
    equation.set(exp)


def percent():
    tmsg.showinfo("Info","Under Development...Sorry for incovenience")

colors={
            "button_txt_color":"#fff",
            "num_fg_color":"#383838",
            "num_hover_color":"#282828",
            "opr_fg_color":"#282828",
            "opr_hover_color":"#383838",
            "equal_fg_color":"#ff8257",
            "equal_hover_color":"#FF5733"
        }

def mode(choice):
    if(choice == "Dark"):
        ctk.set_appearance_mode("dark")
        ctk.CTkLabel(
                cal,
                text="Calculator Standard",
                font=("Calibri", 20, "bold", "italic"),
                text_color="white",
                fg_color="#282828").place(x=20, y=12)
        ctk.CTkLabel(
                cal,
                text="- By Paras Upadhyay",
                font=("Calibri", 10, "bold", "italic"),
                text_color="white").place(x=250, y=478)
        
        colors["button_txt_color"]="#fff"
        colors["num_fg_color"]="#383838"
        colors["num_hover_color"]="#282828"

        colors["opr_fg_color"]="#282828"
        colors["opr_hover_color"]="#383838"
        colors["equal_fg_color"]="#ff8257"
        colors["equal_hover_color"]="#FF5733"
        buttons()

    elif(choice=="Light"):
        ctk.set_appearance_mode("light")
        ctk.CTkLabel(
                cal,
                text="Calculator Standard",
                font=("Calibri", 20, "bold", "italic"),
                text_color="black").place(x=20, y=12)
        ctk.CTkLabel(
                cal,
                text="- By Paras Upadhyay",
                font=("Calibri", 10, "bold", "italic"),
                text_color="black").place(x=250, y=478)
        
        colors["button_txt_color"]="#000"
        colors["num_fg_color"]="#FAF9F6"
        colors["num_hover_color"]="#F9F6EE"

        colors["opr_fg_color"]="#F9F6EE"
        colors["opr_hover_color"]="#FAF9F6"

        colors["equal_fg_color"]="#48BBDB"
        colors["equal_hover_color"]="#0096C7"
        buttons()

# Front-end Code
ctk.set_appearance_mode("dark")  # Modes: system (default) --> dark
cal = ctk.CTk()                                                      # Screen
cal.title("Calculator")                                         # Screen Title
cal.geometry("350x500")                                         # Screen-Size
cal.maxsize(350, 500)                                           # Screen Max Size
cal.minsize(350, 500)                                           # Screen Min Size
cal.iconbitmap("D:\\Python\\Python Git\\Python_tkinter_customtkinter\\GUI_Calculator\\calc.ico")                                # Calculator icon
equation=StringVar()

ctk.CTkLabel(
                cal,
                text="Calculator Standard",
                font=("Calibri", 20, "bold", "italic"),
                text_color="white",
                fg_color="#282828").place(x=20, y=12)

modes=["Dark", "Light"]
combo=ctk.CTkComboBox(
                        cal,
                        values=modes,
                        height=25,
                        width=70,
                        border_width=2,
                        dropdown_font=("Times", 15, "italic"),
                        command=mode)
combo.place(x=270, y=12)
ctk.CTkEntry(cal,
             height=70,
             width=330,
             font=("Times", 38),
             textvariable=equation,
             justify=RIGHT,
             fg_color="#282828",
             text_color="white").place(x=11, y=80)

photo = PhotoImage(file="D:\\Python\\Python Git\\Python_tkinter_customtkinter\\GUI_Calculator\\clear.png")
ctk.CTkLabel(
                cal,
                text="- By Paras Upadhyay",
                font=("Calibri", 10, "bold", "italic"),
                text_color="white").place(x=250, y=478)

# Buttons
button_height = 50
button_width = 83

def buttons():
    #Backspace
    ctk.CTkButton(
                cal,
                text="",
                image=photo,
                height=button_height,
                width=button_width,
                command=backSpace,
                fg_color=colors["equal_fg_color"],
                text_color=colors["button_txt_color"],
                hover_color=colors["equal_hover_color"],
                corner_radius=10).place(x=260, y=155)

    #Clear
    ctk.CTkButton(
                cal,
                text="C",
                font=("Times", 19),
                height=button_height,
                width=button_width, command=clear,
                text_color=colors["button_txt_color"],
                fg_color=colors["opr_fg_color"],
                hover_color=colors["opr_hover_color"],
                corner_radius=10).place(x=177, y=155)

    #All Clear
    ctk.CTkButton(
                cal,
                text="AC",
                font=("Times", 19),
                height=button_height,
                width=button_width,
                command=allClear,
                text_color=colors["button_txt_color"],
                fg_color=colors["opr_fg_color"],
                hover_color=colors["opr_hover_color"],
                corner_radius=10).place(x=92, y=155)

    #Percent
    ctk.CTkButton(
                cal,
                text=chr(37),
                font=("Times", 19),
                height=button_height,
                width=button_width,
                command=percent,
                text_color=colors["button_txt_color"],
                fg_color=colors["opr_fg_color"],
                hover_color=colors["opr_hover_color"],
                corner_radius=10).place(x=10, y=155)

    #Division
    ctk.CTkButton(
                cal,
                text='\u00F7',
                font=("Times", 19),
                height=button_height,
                width=button_width,
                command=divison,
                text_color=colors["button_txt_color"],
                fg_color=colors["opr_fg_color"],
                hover_color=colors["opr_hover_color"],
                corner_radius=10).place(x=260, y=210)

    #Underoot
    ctk.CTkButton(
                cal,
                text="\u221A",
                font=("Times", 19),
                height=button_height,
                width=button_width,
                command=underoot,
                text_color=colors["button_txt_color"],
                fg_color=colors["opr_fg_color"],
                hover_color=colors["opr_hover_color"],
                corner_radius=10).place(x=177, y=210)

    #Square
    ctk.CTkButton(
                cal,
                text="x^2",
                font=("Times", 19),
                height=button_height,
                width=button_width,
                command=square,
                text_color=colors["button_txt_color"],
                fg_color=colors["opr_fg_color"],
                hover_color=colors["opr_hover_color"],
                corner_radius=10).place(x=94, y=210)

    #1/x
    ctk.CTkButton(
                cal,
                text="1/x",
                font=("Times", 19),
                height=button_height,
                width=button_width,
                command=opr2,
                text_color=colors["button_txt_color"],
                fg_color=colors["opr_fg_color"],
                hover_color=colors["opr_hover_color"],
                corner_radius=10).place(x=11, y=210)
    # Product
    ctk.CTkButton(
                cal,
                text="x",
                font=("Times", 19), 
                height=button_height,
                width=button_width, 
                command=product,
                text_color=colors["button_txt_color"],
                fg_color=colors["opr_fg_color"],
                hover_color=colors["opr_hover_color"],
                corner_radius=10).place(x=260, y=265)

    # 9
    ctk.CTkButton(
                cal,
                text="9",
                font=("Times", 19),
                height=button_height,
                width=button_width,
                command=nine,
                fg_color=colors["num_fg_color"],
                text_color=colors["button_txt_color"],
                hover_color=colors["num_hover_color"],
                corner_radius=10).place(x=177, y=265)

    # 8
    ctk.CTkButton(
                cal,
                text="8",
                font=("Times", 19),
                height=button_height,
                width=button_width,
                command=eight,
                fg_color=colors["num_fg_color"],
                text_color=colors["button_txt_color"],
                hover_color=colors["num_hover_color"],
                corner_radius=10).place(x=94, y=265)

    # 7
    ctk.CTkButton(
                cal,
                text="7",
                font=("Times", 19),
                height=button_height,
                width=button_width,
                command=seven,
                fg_color=colors["num_fg_color"],
                text_color=colors["button_txt_color"],
                hover_color=colors["num_hover_color"],
                corner_radius=10).place(x=11, y=265)

    # Subtract
    ctk.CTkButton(
                cal,
                text="-",
                font=("Times", 19),
                height=button_height,
                width=button_width,
                command=subtract,
                text_color=colors["button_txt_color"],
                fg_color=colors["opr_fg_color"],
                hover_color=colors["opr_hover_color"],
                corner_radius=10).place(x=260, y=320)

    # 6
    ctk.CTkButton(
                cal,
                text="6",
                font=("Times", 19),
                height=button_height,
                width=button_width,
                command=six,
                fg_color=colors["num_fg_color"],
                text_color=colors["button_txt_color"],
                hover_color=colors["num_hover_color"],
                corner_radius=10).place(x=177, y=320)

    # 5
    ctk.CTkButton(
                cal,
                text="5",
                font=("Times", 19),
                height=button_height,
                width=button_width,
                command=five,
                fg_color=colors["num_fg_color"],
                text_color=colors["button_txt_color"],
                hover_color=colors["num_hover_color"],
                corner_radius=10).place(x=94, y=320)

    # 4
    ctk.CTkButton(
                cal,
                text="4",
                font=("Times", 19),
                height=button_height,
                width=button_width,
                command=four,
                fg_color=colors["num_fg_color"],
                text_color=colors["button_txt_color"],
                hover_color=colors["num_hover_color"],
                corner_radius=10).place(x=11, y=320)

    # Addition
    ctk.CTkButton(
                cal,
                text="+",
                font=("Times", 19),
                height=button_height,
                width=button_width,
                command=addition,
                text_color=colors["button_txt_color"],
                fg_color=colors["opr_fg_color"],
                hover_color=colors["opr_hover_color"],
                corner_radius=10).place(x=260, y=375)

    # 3
    ctk.CTkButton(
                cal,
                text="3",
                font=("Times", 19),
                height=button_height,
                width=button_width,
                command=three,
                fg_color=colors["num_fg_color"],
                text_color=colors["button_txt_color"],
                hover_color=colors["num_hover_color"], 
                corner_radius=10).place(x=177, y=375)

    # 2
    ctk.CTkButton(
                cal,
                text="2",
                font=("Times", 19),
                height=button_height,
                width=button_width,
                command=two,
                fg_color=colors["num_fg_color"],
                text_color=colors["button_txt_color"],
                hover_color=colors["num_hover_color"],
                corner_radius=10).place(x=94, y=375)

    #1
    ctk.CTkButton(
                cal,
                text="1",
                font=("Times", 19),
                height=button_height,
                width=button_width,
                command=one,
                fg_color=colors["num_fg_color"],
                text_color=colors["button_txt_color"],
                hover_color=colors["num_hover_color"],
                corner_radius=10).place(x=11, y=375)

    # equal
    ctk.CTkButton(
                cal,
                text="=",
                font=("Times", 19),
                height=button_height,
                width=button_width,
                command=equal,
                text_color=colors["button_txt_color"],
                fg_color=colors["equal_fg_color"],
                hover_color=colors["equal_hover_color"],
                corner_radius=10).place(x=260, y=430)

    # decimal
    ctk.CTkButton(
                cal,
                text=".",
                font=("Times", 19),
                height=button_height,
                width=button_width,
                command=decimal,
                text_color=colors["button_txt_color"],
                fg_color=colors["opr_fg_color"],
                hover_color=colors["opr_hover_color"],
                corner_radius=10).place(x=177, y=430)

    # 0
    ctk.CTkButton(
                cal,
                text="0",
                font=("Times", 19),
                height=button_height,
                width=button_width,
                command=zero,
                text_color=colors["button_txt_color"],
                fg_color=colors["opr_fg_color"],
                hover_color=colors["opr_hover_color"],
                corner_radius=10).place(x=92, y=430)

    # +/-
    ctk.CTkButton(
                cal,
                text="+/-",
                font=("Times", 19),
                height=button_height,
                width=button_width,
                command=opr1,
                text_color=colors["button_txt_color"],
                fg_color=colors["opr_fg_color"],
                hover_color=colors["opr_hover_color"],
                corner_radius=10).place(x=10, y=430)
buttons()
cal.mainloop()