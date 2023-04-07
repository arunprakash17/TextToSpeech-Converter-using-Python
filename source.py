import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os



root=Tk()

root.title("Text to speech")
root.geometry("900x450+170+140")

# note
root.resizable(False,False)
root.configure(bg="#305065")


engine=pyttsx3.init()

def speaknow():
    
    text=text_area.get(1.0,END)
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if gender=='Male':
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()
    if(text):
        if speed=='Fast':
            engine.setProperty('rate',250)
            setvoice()
        elif speed=='Normal':
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()


def download():
    print()
    


# icon
image_icon=PhotoImage(file="speak.png")
root.iconphoto(False,image_icon)

# Top Frame

Top_frame = Frame(root,bg="white",width=900,height=100)
Top_frame.place(x=0,y=0)

Logo=PhotoImage(file="speaker logo.png")
Label(Top_frame,image=Logo,bg="White").place(x=10,y=5)

Label(Top_frame,text="TEXT TO SPEECH",font="arial 20 bold",bg="white",fg="black").place(x=100,y=30)


# for creating text area
text_area=Text(root,font="Roboto 20",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=500,height=250)

# creating labels for text in typing right side area
Label(root,text='VOICE',font="arial 15 bold",bg="#305065",fg="white").place(x=580,y=160)
Label(root,text="SPEED",font="arial 15 bold",bg="#305065",fg="white").place(x=760,y=160)


gender_combobox=Combobox(root,values=['Male','Female'],font="arial 14",state='r',width=10);
gender_combobox.place(x=550,y=200)
gender_combobox.set("Select")

speed_combobox=Combobox(root,values=['Fast','Normal','Slow'],font="arial 14",state='r',width=10);
speed_combobox.place(x=730,y=200)
speed_combobox.set("Normal")

# Button image icons
imageicon=PhotoImage(file="speak.png")
btn=Button(root,text="Speak",width=130,compound=LEFT,image=imageicon,bg="sky blue",font="arial 16 bold",command=speaknow)
btn.place(x=550,y=280)

imageicon2=PhotoImage(file="download.png")
save_btn=Button(root,text='Speak',width=130,compound=LEFT,image=imageicon2,bg="light green",font="arial 16 bold",command=download).place(x=730,y=280)

root.mainloop()
