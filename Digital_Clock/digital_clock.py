import customtkinter as ctk
from time import strftime, localtime

def update_time():
    current_time = strftime('%H:%M:%S %p')
    current_date = strftime('%B %d, %Y (%A)', localtime())
    date_label.configure(text=current_date)
    time_label.configure(text=current_time)
    time_label.after(1000, update_time) 

clock = ctk.CTk()
ctk.set_appearance_mode("dark")
clock.title("Digital Clock")
clock.geometry("400x200")
clock.maxsize(400, 200)
clock.minsize(400, 200)
clock.iconbitmap("D:\\Python\\Python Git\\Python_tkinter_customtkinter\\Digital_Clock\\Clock.ico")

font_style = ("ds-digital", 60, "bold")
date_label=ctk.CTkLabel(
                    clock,
                    font=("aerial", 20, "bold"),
                    text_color="white")
date_label.place(x=120, y=65)
time_label = ctk.CTkLabel(clock, font=font_style, text_color="cyan")
time_label.place(x=25, y=100)
update_time()
clock.mainloop()
