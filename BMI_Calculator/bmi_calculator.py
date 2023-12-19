import customtkinter as ctk
from tkinter import messagebox as tmsg
win=ctk.CTk();
win.title("BMI Calculator")
win.iconbitmap("D:\\Python\\Python Git\\Python_tkinter_customtkinter\\BMI_Calculator\\bmi.ico")
win.geometry("350x520")
win.maxsize(350,520)
win.minsize(350,520)

height=0
gender=""
weight=0
def get_gender():
    global gender
    gender=radio.get()

def get_height(val):
    global height
    height=int(val)
    slider_label.configure(text=str(int(val))+"cm")

def submit():
        global weight
        weight = int(entry.get())

        if(gender=="" or height==0 or weight==0):
            tmsg.showinfo("Info", "Fill all details")
        else:
            frame3.configure(border_color="#fff", fg_color="#292929")
            dis_h = "Your height: "+str(height)+" cm"
            dis_w = "Your weight: "+str(weight)+" kg"
            display_height.configure(text=dis_h)
            display_weight.configure(text=dis_w)
            calculate_bmi()
def calculate_bmi():
    global weight, height, gender
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
    
    


ctk.CTkLabel(win, 
             text="BMI Calculator",
             font=("Times", 30, "bold"),
             text_color="yellow").place(x=80, y=15)

frame1=ctk.CTkFrame(master=win,
             corner_radius=10,
             fg_color="#292929",
             border_color="#fff",
             border_width=2,
             height=50,
             width=300
             )
frame1.place(x=25, y=80)

frame2=ctk.CTkFrame(master=win,
             corner_radius=10,
             fg_color="#292929",
             border_color="#fff",
             border_width=2,
             height=130,
             width=300
             )
frame2.place(x=25, y=135)

frame3=ctk.CTkFrame(master=win,
                    corner_radius=10,
                    fg_color="#fff",
                    border_color="#000",
                    border_width=2,
                    height=180,
                    width=300)
frame3.place(x=25, y=310)
radio=ctk.StringVar(value="Gender")
ctk.CTkRadioButton(frame1,
                   text="Male",
                   text_color="#fff",
                   font=("Georgia", 17),
                   value="M",
                   variable=radio,
                   command=get_gender,
                   radiobutton_width=15,
                   radiobutton_height=15,
                   border_width_checked=4,
                   border_width_unchecked=2,
                   border_color="#fff").place(x=40, y=15)
ctk.CTkRadioButton(frame1,
                   text="Female",
                   text_color="#fff",
                   font=("Georgia", 17),
                   value="F",
                   variable=radio,
                   command=get_gender,
                   radiobutton_width=15,
                   radiobutton_height=15,
                   border_width_checked=4,
                   border_width_unchecked=2,
                   border_color="#fff").place(x=170, y=15)

# weight label
ctk.CTkLabel(frame2,
             text="Weight(in kg): ",
             font=("Georgia", 18),
             text_color="#fff").place(x=30, y=25)

#weight entry
entry=ctk.CTkEntry(frame2,
             font=("Aerial", 16),
             placeholder_text="(in kg)",
             placeholder_text_color="#808080",
             justify="center",
             height=30,
             width=80)
entry.place(x=165, y=25)

# height label
ctk.CTkLabel(frame2,
             text="Height (in cm): ",
             font=("Georgia", 18),
             text_color="#fff").place(x=30, y=70)

slider=ctk.CTkSlider(frame2,
                    from_=0,
                    to=200,
                    command=get_height,
                    width=180,
                    height=18
                    )
slider.place(x=70, y=100)
slider.set(0)
slider_label=ctk.CTkLabel(frame2, text="", font=("Calibri", 18))
slider_label.place(x=180, y=70)

button=ctk.CTkButton(win,
                     text="Calculate BMI",
                     width=35,
                     font=("Georgia", 16, "italic"),
                     corner_radius=10,
                     text_color="#000",
                     fg_color="#48BBDB",
                     hover_color="#0096C7",
                     command=submit)
button.place(x=130, y=270)

display_height=ctk.CTkLabel(frame3,
                            text="",
                            font=("Georgia", 17, "italic"))
display_height.place(x=15, y=10)
display_weight=ctk.CTkLabel(frame3,
                            text="",
                            font=("Georgia", 17, "italic"))
display_weight.place(x=15, y=35)

display_bmi=ctk.CTkLabel(frame3,
                         text="",
                         font=("Florida", 20, "bold"))
display_bmi.place(x=100, y=70)

display_status=ctk.CTkLabel(frame3,
                            text="",
                            text_color="#fff",
                            font=("Georgia",25, "underline"))
display_status.place(x=20, y=100)
ctk.CTkLabel(win, 
             font=("Calibri", 12, "italic"),
             text="By Paras Upadhyay").place(x=250, y=495)
win.mainloop();


