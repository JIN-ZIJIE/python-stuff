from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Wack peoplr')

button_quit = Button(root, text='X', command=root.quit)
button_quit.pack()

button_quit1 = Button(root, text='X', command=root.quit)
button_quit1.pack()

button_quit2 = Button(root, text='X', command=root.quit)
button_quit2.pack()

button_quit3 = Button(root, text='X', command=root.quit)
button_quit3.pack()

button_quit4 = Button(root, text='X', command=root.quit)
button_quit4.pack()

root.mainloop()
