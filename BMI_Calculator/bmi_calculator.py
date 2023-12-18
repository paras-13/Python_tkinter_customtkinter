import customtkinter as ctk
from tkinter import *
win=ctk.CTk();
win.title("BMI Calculator")
win.iconbitmap("D:\\Python\\Python Git\\Python_tkinter_customtkinter\\BMI_Calculator\\bmi.ico")
win.geometry("400x250")
win.maxsize(400,500)
win.minsize(400,500)

ctk.CTkLabel(win, 
             text="BMI Calculator",
             font=("Times", 30, "bold"),
             text_color="yellow").place(x=100, y=15)
# weight label
ctk.CTkLabel(win,
             text="Enter Weight(in kg): ",
             font=("Aerial", 16),
             text_color="#fff").place(x=140, y=100)

#weight entry
ctk.CTkEntry(win,
             placeholder_text="(in kg)",
             placeholder_text_color="#808080",
             height=30,
             width=135).place(x=150, y=135)

# height label
ctk.CTkLabel(win,
             text="Enter Height(in metre): ",
             font=("Aerial", 18),
             text_color="#fff").place(x=135, y=190)

#height entry
ctk.CTkEntry(win,
             placeholder_text="in metres",
             placeholder_text_color="#808080",
             height=30,
             width=135).place(x=155, y=230)



ctk.CTkLabel(win, 
             font=("Calibri", 12, "italic"),
             text="By Paras Upadhyay").place(x=300, y=475)
win.mainloop();


