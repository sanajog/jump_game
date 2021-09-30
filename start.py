from tkinter import *
import subprocess
from PIL import ImageTk, Image

# main
root = Tk()
root.geometry("800x600")
my_image = ImageTk.PhotoImage(Image.open("backgr.png"))
my_label = Label(root, image= my_image)
my_label.place(x=0, y=0)
frame = Frame(root)
frame.pack(pady= 40)

# function
def open():
    root.destroy()
    subprocess.call(["python", "jump_game.py"])

# button
img = PhotoImage(file = 'play.png')
start = Button(frame, command=open, image= img, bd = .0)
start.pack()



root.mainloop()
