import time
import tkinter as tk
from tkinter import *
def TM():
    Time=time.strftime('%I:%M:%S')
    clock.config(text=Time)
    clock.after(200,TM)


gui=Tk()
clock=tk.Label(gui, font=('arial 100 bold'))
clock.pack()
fajar=tk.Label(gui,text="فجر              05:40 ", font=('arial 50 bold')).pack()
Duhr=tk.Label(gui,text="ظهر             04:30 ", font=('arial 50 bold')).pack()
Asar=tk.Label(gui,text="عصر             05:20", font=('arial 50 bold')).pack()
Maghrib=tk.Label(gui,text="مغرب            06:10", font=('arial 50 bold')).pack()
Esha=tk.Label(gui,text="عشاء             08:40", font=('arial 50 bold')).pack()
Jummah=tk.Label(gui,text="جمعہ             02:40", font=('arial 50 bold')).pack()

TM()
gui.mainloop()
