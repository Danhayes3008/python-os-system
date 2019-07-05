import tkinter
from tkinter import *
from tkinter import Tk, StringVar, ttk
import random
import os
import datetime
import time;
import sys

password = ("1234")


def try_login():
      if code.get() == password:
       print ("Complete sucsessfull!")
       os.startfile('main window.py')
#       messagebox.showinfo("ACCESS GRANTED")
#    elif code != password:
#         print ("Error: (Incorrect value entered)")
#        messagebox.showinfo("-- ERROR --", "Please enter valid infomation!", icon="warning")



#set the window to center of the screen
def center_window(width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

# creats the window 
root = Tk()
#set window size
center_window(510, 600)
#root.geometry("500x700+0+0")
# set to full screen
#root.attributes('-fullscreen', True)
# set window name
root.title("Key Pad")
# sets window background colour
root.configure(background='black')

text_Input = StringVar()
operator = ""

#closes the window
def close(event):
    root.withdraw() # if you want to bring it back
    sys.exit() # if you want to exit the entire thing

root.bind('<Escape>', close)

# creates a frame at the top of the window
TopFrame = Frame(root, width = 1375, height = 100, bd=14,  background='black')
TopFrame.pack(side=TOP)

BottomFrame = Frame(root, width = 1375, height = 100, bd=14,  background='black')
BottomFrame.pack(side=BOTTOM)

#============================================================================== Top frame ===============================================================

lblTitle = Label(TopFrame, font=('arial',10, 'bold'), text=" ", bd=10, width= 50,height=2, justify='right', anchor='s' 'e',  background='MediumPurple3')
lblTitle.grid(row=0,column=0, pady=17)
code = Entry(TopFrame, font=('arial',14, 'bold'), textvariable=text_Input, bd=10, insertwidth=4,justify='center', show="*", bg='Orchid1')
code.grid(row=1,column=0, padx=3, pady=13)

#============================================================================== Left Frame ===============================================================

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClrDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEntrInput():
    global operator
    operator= password
    

LeftMidFrame = Frame(width = 640, height = 750, bd=14, background='black')
LeftMidFrame.pack(side=LEFT)

btn1 = Button(LeftMidFrame,padx=16,pady=16,bd=8,fg="black", width=13, font=('arial',10, 'bold'),
              text="1", background='DarkOrange1', command=lambda: btnClick(1)).grid(row=0,column=0, padx=3)
btn2 = Button(LeftMidFrame,padx=16,pady=16,bd=8,fg="black", width=13, font=('arial',10, 'bold'),
              text="2", background='DarkOrange1', command=lambda: btnClick(2)).grid(row=0,column=1, padx=3)
btn3 = Button(LeftMidFrame,padx=16,pady=16,bd=8,fg="black", width=13, font=('arial',10, 'bold'),
              text="3", background='DarkOrange1', command=lambda: btnClick(3)).grid(row=0,column=2, padx=3)
btn4 = Button(LeftMidFrame,padx=16,pady=16,bd=8,fg="black", width=13, font=('arial',10, 'bold'),
              text="4", background='DarkOrange1', command=lambda: btnClick(4)).grid(row=1,column=0, padx=3)
btn5 = Button(LeftMidFrame,padx=16,pady=16,bd=8,fg="black", width=13, font=('arial',10, 'bold'),
              text="5", background='DarkOrange1', command=lambda: btnClick(5)).grid(row=1,column=1, padx=3)
btn6 = Button(LeftMidFrame,padx=16,pady=16,bd=8,fg="black", width=13, font=('arial',10, 'bold'),
              text="6", background='DarkOrange1', command=lambda: btnClick(6)).grid(row=1,column=2, padx=3)
btn7 = Button(LeftMidFrame,padx=16,pady=16,bd=8,fg="black", width=13, font=('arial',10, 'bold'),
              text="7", background='DarkOrange1', command=lambda: btnClick(7)).grid(row=2,column=0, padx=3)
btn8 = Button(LeftMidFrame,padx=16,pady=16,bd=8,fg="black", width=13, font=('arial',10, 'bold'),
              text="8", background='DarkOrange1', command=lambda: btnClick(8)).grid(row=2,column=1, padx=3)
btn9 = Button(LeftMidFrame,padx=16,pady=16,bd=8,fg="black", width=13, font=('arial',10, 'bold'),
              text="9", background='DarkOrange1', command=lambda: btnClick(9)).grid(row=2,column=2, padx=3)
btnclr = Button(LeftMidFrame,padx=16,pady=16,bd=8,fg="black", width=13, font=('arial',10, 'bold'),
              text="clr", background='DarkOrange1', command = btnClrDisplay).grid(row=3,column=0, padx=3)
btn0 = Button(LeftMidFrame,padx=16,pady=16,bd=8,fg="black", width=13, font=('arial',10, 'bold'),
              text="0", background='DarkOrange1', command=lambda: btnClick(0)).grid(row=3,column=1, padx=3)
btnentr = Button(LeftMidFrame,padx=16,pady=16,bd=8,fg="black", width=13, font=('arial',10, 'bold'),
              text="entr", background='DarkOrange1', command=try_login).grid(row=3,column=2, padx=3)


#=============================================================== Bottom Frame ===================================================================================

lblTitle = Label(BottomFrame, font=('arial',10, 'bold'), text=" ", bd=10, width= 50,height=2, justify='right', anchor='s' 'e',  background='MediumPurple3')
lblTitle.grid(row=0,column=0)


root.mainloop()
