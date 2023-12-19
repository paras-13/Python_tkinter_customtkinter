import customtkinter as ctk
from tkinter import messagebox as tmsg
win=ctk.CTk();
win.title("BMI Calculator")
win.iconbitmap("D:\\Python\\Python Git\\Python_tkinter_customtkinter\\BMI_Calculator\\bmi.ico")
win.geometry("350x450")
win.maxsize(350,450)
win.minsize(350,440)

height=0
gender=""
age=""
weight=0

screen = ctk.CTkFrame(master=win,corner_radius=15,
             fg_color="#292929", border_color="#fff",
             border_width=2, height=440, width=330)
screen.place(x=10, y=5)
ctk.CTkLabel(screen, 
             text="BMI Calculator",
             font=("Times", 25, "italic"),
             text_color="yellow").place(x=20, y=15)
    
def new_window():
    global weight, height, gender
    new_win=ctk.CTkToplevel(win)
    new_win.title("Your BMI...")
    new_win.geometry("350x250")
    new_win.resizable(False, False)
    display_gender=ctk.CTkLabel(new_win,
                                text="",
                                font=("Georgia", 17, "italic"))
    display_gender.place(x=15, y=10)
    display_age=ctk.CTkLabel(new_win,
                            text="",
                            font=("Georgia", 17, "italic"))
    display_age.place(x=15, y=35)
    display_height=ctk.CTkLabel(new_win,
                            text="",
                            font=("Georgia", 17, "italic"))
    display_height.place(x=15, y=60)
    display_weight=ctk.CTkLabel(new_win,
                            text="",
                            font=("Georgia", 17, "italic"))
    display_weight.place(x=15, y=85)

    display_bmi=ctk.CTkLabel(new_win,
                         text="",
                         font=("Florida", 20, "bold"))
    display_bmi.place(x=110, y=130)

    display_status=ctk.CTkLabel(new_win,
                            text="",
                            text_color="#fff",
                            font=("Georgia",25, "underline"))
    display_status.place(x=20, y=160)
    dis_h = "> Height: "+str(height)+" cm"
    dis_w = "> Weight: "+str(weight)+" kg"
    dis_g = "> "+gender
    dis_age="> Age: "+age
    display_gender.configure(text=dis_g)
    display_age.configure(text=dis_age)
    display_height.configure(text=dis_h)
    display_weight.configure(text=dis_w)
    
    bmi=float("{:.1f}".format(weight/(height/100)**2))
    print(bmi)
    dis_bmi="BMI: "+str(bmi)
    display_bmi.configure(text=dis_bmi)
    if(bmi<18.5):
         display_status.configure(text="Underweight", text_color="blue")
    elif(bmi>=18.5 and bmi<=24.9):
         display_status.configure(text="Normal", text_color="green")
    elif(bmi>=25.0 and bmi<=29.9):
         display_status.configure(text="Overweight", text_color="#BC544B")
    elif(bmi>=30.0 and bmi<=34.9):
         display_status.configure(text="Obesity Class I", text_color="#D21404")
    elif(bmi>=30.0 and bmi<=34.9):
         display_status.configure(text="Obesity Class II", text_color="#900D09")
    elif(bmi>=40.0):
         display_status.configure(text="Obesity Class III", text_color="#4E0707")

def get_gender():
    global gender
    gender=radio1.get()

def get_age():
     global age
     age=radio2.get()
     print(age)
     
def get_height(val):
    global height
    height=int(val)
    slider_label.configure(text=str(int(val))+"cm")

def submit():
        global weight
        weight = int(entry.get())

        if(gender=="" or height==0 or weight==0 or age==""):
            tmsg.showinfo("Info", "Fill all details")
        else:
            new_window()

frame1=ctk.CTkFrame(master=screen,corner_radius=30,
             fg_color="#292929", border_color="#fff",
             border_width=2, height=130, width=310)
frame1.place(x=10, y=80)

radio1=ctk.StringVar(value="Gender")
ctk.CTkLabel(frame1,
             text="Gender: ",
             font=("Calibri", 20, "bold")).place(x=30, y=10)
ctk.CTkRadioButton(frame1,
                   text="Male", text_color="#fff",
                   font=("Georgia", 15), value="Male",
                   variable=radio1, command=get_gender,
                   radiobutton_width=15, radiobutton_height=15,
                   border_width_checked=4, border_width_unchecked=2,
                   border_color="#fff").place(x=30, y=45)

ctk.CTkRadioButton(frame1,
                   text="Female", text_color="#fff",
                   font=("Georgia", 15), value="Female",
                   variable=radio1, command=get_gender,
                   radiobutton_width=15, radiobutton_height=15,
                   border_width_checked=4, border_width_unchecked=2,
                   border_color="#fff").place(x=30, y=70)

radio2=ctk.StringVar(value="other")
age=["Bellow 20", "Between 20 and 60", "Above 60"]
ctk.CTkLabel(frame1,
             text="Age: ",
             font=("Calibri", 20, "bold")).place(x=140, y=10)
ctk.CTkRadioButton(frame1,
                   text=age[0], text_color="#fff",
                   font=("Georgia", 15), value=age[0],
                   variable=radio2, command=get_age,
                   radiobutton_width=15, radiobutton_height=15,
                   border_width_checked=4, border_width_unchecked=2,
                   border_color="#fff").place(x=140, y=45)
ctk.CTkRadioButton(frame1,
                   text=age[1], text_color="#fff",
                   font=("Georgia", 15), value=age[1],
                   variable=radio2, command=get_age,
                   radiobutton_width=15, radiobutton_height=15,
                   border_width_checked=4, border_width_unchecked=2,
                   border_color="#fff").place(x=140, y=70)
ctk.CTkRadioButton(frame1,
                   text=age[2], text_color="#fff",
                   font=("Georgia", 15), value=age[2],
                   variable=radio2, command=get_age,
                   radiobutton_width=15, radiobutton_height=15,
                   border_width_checked=4, border_width_unchecked=2,
                   border_color="#fff").place(x=140, y=95)


frame2=ctk.CTkFrame(master=screen, corner_radius=30,
             fg_color="#292929", border_color="#fff",
             border_width=2, height=130, width=310)
frame2.place(x=10, y=215)

# weight label
ctk.CTkLabel(frame2,
             text="Weight(in kg): ",
             font=("Georgia", 18),
             text_color="#fff").place(x=30, y=20)

#weight entry
entry=ctk.CTkEntry(frame2,
             font=("Aerial", 16),
             placeholder_text="(in kg)",
             placeholder_text_color="#808080",
             justify="center", height=30, width=80)
entry.place(x=165, y=20)

# height label
ctk.CTkLabel(frame2,
             text="Height (in cm): ",
             font=("Georgia", 18),
             text_color="#fff").place(x=30, y=60)

slider=ctk.CTkSlider(frame2,
                    from_=0, to=200,
                    command=get_height, width=180, height=18)
slider.place(x=70, y=95)
slider.set(0)
slider_label=ctk.CTkLabel(frame2, text="", font=("Calibri", 18))
slider_label.place(x=180, y=60)


button=ctk.CTkButton(win,
                     text="Calculate BMI", width=35,
                     font=("Georgia", 16, "italic"), 
                     corner_radius=20, command=submit,
                     text_color="#000",
                     fg_color="#48BBDB",
                     hover_color="#0096C7")
button.place(x=130, y=360)




ctk.CTkLabel(win, 
             font=("Calibri", 12, "italic"),
             text="By Paras Upadhyay").place(x=235, y=415)
win.mainloop();


