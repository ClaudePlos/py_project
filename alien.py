#autor klaudiusz.skowronski claude-plos@o2.pl
#title:drow alien
#add 2017.02.23
from tkinter import *
import time
#from random import *

canvSize = 500
window = Tk()
window.title('Alien');
canv = Canvas(window, width=canvSize, height=canvSize)
canv.pack()

#text
text = canv.create_text(200, 280, text='I\'m an alien')


#drow the alien
tors = canv.create_oval(100, 150, 300, 250, fill='green') # x, y w, h -
eye = canv.create_oval(170, 70, 230, 130, fill='white') #
pupil = canv.create_oval(190, 90, 210, 110, fill='black') #zrenica
mouth = canv.create_oval(150, 220, 250, 240, fill='red')
neck = canv.create_line(200, 150, 200, 130, fill='black')
hat = canv.create_polygon(180, 75, 220, 75, 200, 20, fill='purple')
canv.update()

#events
def close_the_eye(event):
    canv.itemconfig(eye, fill='green')
    canv.itemconfig(pupil, state=HIDDEN)
def open_the_eye(event):
    canv.itemconfig(eye, fill='white')
    canv.itemconfig(pupil, state=NORMAL)
canv.bind_all('<KeyPress-a>', close_the_eye)
canv.bind_all('<KeyPress-z>', open_the_eye)

def control_eye(event):
    key = event.keysym
    if  key == "Up":
        canv.move(pupil, 0, -1)
    elif  key == "Down":
        canv.move(pupil, 0, 1)
    elif  key == "Left":
        canv.move(pupil, -1, 0)
    elif  key == "Right":
        canv.move(pupil, 1, 0)
canv.bind_all('<Key>', control_eye)

input("Press enter to exit ;)")
