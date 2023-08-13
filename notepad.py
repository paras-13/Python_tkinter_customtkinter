from tkinter import *
from tkinter import messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfile
import os
#Structure
pad = Tk()
pad.title("Untitled - Notepad")
pad.wm_iconbitmap("notes.ico")
pad.geometry("800x600")

# Textarea
textarea = Text(pad,font="lucida 12")
textarea.pack(fill=BOTH,expand=True)

file = None
# Functions
def New():
    global file
    pad.title("Untitled - Notepad")
    file = Nonel
    textarea.delete(1.0,END)
def Open():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        pad.title(os.path.basename(file) + "- Notepad")
        textarea.delete(1.0,END)
    f = open(file,"r")
    textarea.insert(1.0, f.read())
    f.close()
def Save():
    global file
    if file == None:
        file = asksaveasfile(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file =="":
            file = None
        else:
            f = open(file,"w")
            f.write(textarea.get(1.0,END))
            f.close()

            pad.title(os.path.basename(file)+"- Notepad")
    else:
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()


def Exit():
    pad.destroy()
def Cut():
    textarea.event_generate("<<Cut>>")
def Copy():
    textarea.event_generate("<<Copy>>")
def Paste():
    textarea.event_generate("<<Paste>>")
def About():
    tmsg.showinfo("Notepad","Working with notepad today")
def help():
    tmsg.showinfo("Any problem?","Any problem\nMail us at parasupadhyay025@gmail.com")

# Menu bars

MenuBar = Menu(pad)
File = Menu(MenuBar, tearoff=0)
File.add_command(label="New", command=New)
File.add_command(label="Open" ,command=Open)
File.add_command(label="Save" ,command=Save)
File.add_command(label="Exit", command=Exit)
MenuBar.add_cascade(label="File",menu=File)

Edit = Menu(MenuBar, tearoff=0)
Edit.add_command(label="Cut", command=Cut)
Edit.add_command(label="Copy", command=Copy)
Edit.add_command(label="Paste", command=Paste)
MenuBar.add_cascade(label="Edit",menu=Edit)

Help = Menu(MenuBar,tearoff=0)
Help.add_command(label="About",command=About)
Help.add_command(label="Help",command=help)
MenuBar.add_cascade(label="Help",menu=Help)
pad.config(menu=MenuBar)

# Scroll Bar
Scrollbar = Scrollbar(textarea)
Scrollbar.pack(side=RIGHT, fill=Y)
Scrollbar.config(command=textarea.yview)
textarea.config(yscrollcommand=Scrollbar.set)
pad.mainloop()
# m1.add_command(text="New")
