from tkinter import *
from tkinter import messagebox
import random

root = Tk()

#number = random.randint(1,3)
number = 2

def popup():
    if number == 1:
        messagebox.askyesno('QUESTION', 'r u gay')
    if number == 2:
        messagebox.showinfo('', 'U R GAY')
    if number == 3:
        messagebox.showinfo('HA HA HA', 'YOUR COMPUTER IS HACKED!!!')


Button(root, text="Popup", command=popup).pack()
Button(root, text="Quit", command=root.destroy).pack()


mainloop()