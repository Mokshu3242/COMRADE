import tkinter
from tkinter import *
import os

root = Tk()

root.title('Volume Controller')
root.minsize(height=250, width=250)
lbl = Label(root, text="VOLUME CONTROLLER", font=('Times_New_Roman', 25), bg="blue")


def onVoice():
    os.startfile("voice.py")


def onHand():
    os.startfile("gesture.py")


btn1 = Button(root, text="Voice Recognition", command=onVoice, font=('Times_New_Roman', 10), bd=10, bg="grey",
              fg="white")
btn2 = Button(root, text="Hand Gesture", command=onHand, font=('Times_New_Roman', 10), bd=10, bg="grey", fg="white")

lbl.pack(fill=tkinter.X)
btn1.pack(fill=tkinter.X, padx=60, pady=40)
btn2.pack(fill=tkinter.X, padx=60)
root.mainloop()
