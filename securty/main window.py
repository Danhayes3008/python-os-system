import tkinter
from tkinter import *
from tkinter import Tk, StringVar, ttk
import random
import os
import datetime
import time;
import sys

#==============Define Functions=======================
def close(event):
    root.withdraw() # if you want to bring it back
    sys.exit() # if you want to exit the entire thing

def raise_frame(frame):
    frame.tkraise()


# sets the window
root = Tk()
root.attributes('-fullscreen', True)
root.configure(background='black')#sets background of the window

#==================Top Frames=============================

TopFrame = Frame(root, width=2000, height=100, bd=14, bg='black')
TopFrame.pack(side=TOP)

#==================Bottom Frames===========================
BottomFrame= Frame(root, width=2000, height=100, bd=14, bg='black')
BottomFrame.pack(side=BOTTOM)

#====================Left Frames===========================
LF1 = Frame(root, width=300, height=1000, bd=14, bg='black')
LF1.pack(side=LEFT)

LF2 = Frame(root, width=300, height=1000, bd=14, bg='black')
LF2.pack(side=LEFT)

#===================Right Frames===========================
RightFrame = Frame(root, width=1375, height=200, bd=14, bg='black')
RightFrame.pack(side=RIGHT)

for frame in (LF1, LF2):
    frame.pack()


#==================Left Frame 1 buttons============================
btn1 = Button(LF1,padx=16,pady=16,bd=8,fg="black", width=15, font=('arial',15, 'bold'),
              text="Science", background='DarkOrange1', command=lambda:raise_frame(LF2)).grid(row=0,column=0, padx=3, pady=1)
btn1 = Button(LF1,padx=16,pady=16,bd=8,fg="black", width=15, font=('arial',15, 'bold'),
              text="History", background='DarkOrange1').grid(row=1,column=0, padx=3, pady=1)
btn1 = Button(LF1,padx=16,pady=16,bd=8,fg="black", width=15, font=('arial',15, 'bold'),
              text="Math", background='DarkOrange1').grid(row=2,column=0, padx=3, pady=1)
btn1 = Button(LF1,padx=16,pady=16,bd=8,fg="black", width=15, font=('arial',15, 'bold'),
              text="Art", background='DarkOrange1').grid(row=3,column=0, padx=3, pady=1)
btn1 = Button(LF1,padx=16,pady=16,bd=8,fg="black", width=15, font=('arial',15, 'bold'),
              text="Drama", background='DarkOrange1').grid(row=4,column=0, padx=3, pady=1)
btn1 = Button(LF1,padx=16,pady=16,bd=8,fg="black", width=15, font=('arial',15, 'bold'),
              text="Language", background='DarkOrange1').grid(row=5,column=0, padx=3, pady=1)
btn1 = Button(LF1,padx=16,pady=16,bd=8,fg="black", width=15, font=('arial',15, 'bold'),
              text="Sports", background='DarkOrange1').grid(row=6,column=0, padx=3, pady=1)
btn1 = Button(LF1,padx=16,pady=16,bd=8,fg="black", width=15, font=('arial',15, 'bold'),
              text="Next", background='DarkOrange1').grid(row=7,column=0, padx=3, pady=1)
btn2 = Button(LF1,padx=16,pady=16,bd=8,fg="black", width=15, font=('arial',15, 'bold'),
              text="Back", background='DarkOrange1').grid(row=8,column=0, padx=3, pady=1),

#==================Left Frame 2 buttons============================
btn1 = Button(LF2,padx=16,pady=16,bd=8,fg="black", width=15, font=('arial',15, 'bold'),
              text="Science", background='DarkOrange1').grid(row=0,column=0, padx=3, pady=1)
btn1 = Button(LF2,padx=16,pady=16,bd=8,fg="black", width=15, font=('arial',15, 'bold'),
              text="History", background='DarkOrange1').grid(row=1,column=0, padx=3, pady=1)
btn1 = Button(LF2,padx=16,pady=16,bd=8,fg="black", width=15, font=('arial',15, 'bold'),
              text="Math", background='DarkOrange1').grid(row=2,column=0, padx=3, pady=1)
btn1 = Button(LF2,padx=16,pady=16,bd=8,fg="black", width=15, font=('arial',15, 'bold'),
              text="Art", background='DarkOrange1').grid(row=3,column=0, padx=3, pady=1)
btn1 = Button(LF2,padx=16,pady=16,bd=8,fg="black", width=15, font=('arial',15, 'bold'),
              text="Drama", background='DarkOrange1').grid(row=4,column=0, padx=3, pady=1)
btn1 = Button(LF2,padx=16,pady=16,bd=8,fg="black", width=15, font=('arial',15, 'bold'),
              text="Language", background='DarkOrange1').grid(row=5,column=0, padx=3, pady=1)
btn1 = Button(LF2,padx=16,pady=16,bd=8,fg="black", width=15, font=('arial',15, 'bold'),
              text="Sports", background='DarkOrange1').grid(row=6,column=0, padx=3, pady=1)
btn1 = Button(LF2,padx=16,pady=16,bd=8,fg="black", width=15, font=('arial',15, 'bold'),
              text="Next", background='DarkOrange1').grid(row=7,column=0, padx=3, pady=1)
btn2 = Button(LF2,padx=16,pady=16,bd=8,fg="black", width=15, font=('arial',15, 'bold'),
              text="Back", background='DarkOrange1').grid(row=8,column=0, padx=3, pady=1),


#===================Lebals==============================
lblTitle = Label(TopFrame, font=('arial',10, 'bold'), text=" ", bd=10, width= 230,height=3, justify='right', anchor='s' 'e',  background='MediumPurple3')
lblTitle.grid(row=0,column=0)

lblTitle = Label(BottomFrame, font=('arial',10, 'bold'), text=" ", bd=10, width= 230,height=3, justify='right', anchor='s' 'e',  background='MediumPurple3')
lblTitle.grid(row=0,column=0)

root.bind('<Escape>', close)

raise_frame(LF1)
root.mainloop()
