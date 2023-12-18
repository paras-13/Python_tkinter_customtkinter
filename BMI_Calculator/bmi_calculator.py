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

frame1=ctk.CTkFrame(master=win,
             corner_radius=10,
             fg_color="#292929",
             border_color="#fff",
             border_width=2,
             height=70,
             width=300
             )
frame1.place(x=50, y=80)

frame2=ctk.CTkFrame(master=win,
             corner_radius=10,
             fg_color="#292929",
             border_color="#fff",
             border_width=2,
             height=180,
             width=300
             )
frame2.place(x=50, y=160)
def get_gender():
    gender=radio.get()
    print(gender)
radio=ctk.StringVar(value="Gender")
ctk.CTkRadioButton(frame1,
                   text="Male",
                   text_color="#fff",
                   font=("Georgia", 19),
                   value="M",
                   variable=radio,
                   command=get_gender,
                   radiobutton_width=15,
                   radiobutton_height=15,
                   border_width_checked=4,
                   border_width_unchecked=2,
                   border_color="#fff").place(x=40, y=20)
ctk.CTkRadioButton(frame1,
                   text="Female",
                   text_color="#fff",
                   font=("Georgia", 19),
                   value="F",
                   variable=radio,
                   command=get_gender,
                   radiobutton_width=15,
                   radiobutton_height=15,
                   border_width_checked=4,
                   border_width_unchecked=2,
                   border_color="#fff").place(x=170, y=20)

# weight label
ctk.CTkLabel(frame2,
             text="Weight(in kg): ",
             font=("Aerial", 20),
             text_color="#fff").place(x=30, y=30)

#weight entry
ctk.CTkEntry(frame2,
             font=("Aerial", 16),
             placeholder_text="(in kg)",
             placeholder_text_color="#808080",
             justify="center",
             height=30,
             width=80).place(x=165, y=30)

# height label
ctk.CTkLabel(frame2,
             text="Height (in cm): ",
             font=("Aerial", 20),
             text_color="#fff").place(x=30, y=90)

def get_height(val):
    slider_label.configure(text=str(int(val))+"cm")
slider=ctk.CTkSlider(frame2,
                    from_=0,
                    to=200,
                    command=get_height,
                    width=180,
                    height=18
                    )
slider.place(x=70, y=130)
slider.set(0)
slider_label=ctk.CTkLabel(frame2, text="", font=("Calibri", 18))
slider_label.place(x=180, y=90)


ctk.CTkLabel(win, 
             font=("Calibri", 12, "italic"),
             text="By Paras Upadhyay").place(x=300, y=475)
win.mainloop();


