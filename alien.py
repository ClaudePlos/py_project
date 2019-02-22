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
text1 = canv.create_text(200, 280, text='I\'m an alien')
text2 = canv.create_text(200, 350, text='Check kays: A, Z, up, down, left, righy, left button mouse')

#drow the alien
tors = canv.create_oval(100, 150, 300, 250, fill='green') # x, y w, h -
eye = canv.create_oval(170, 70, 230, 130, fill='white') #
pupil = canv.create_oval(190, 90, 210, 110, fill='black') #zrenica
mouth = canv.create_oval(150, 220, 250, 240, fill='red')
neck = canv.create_line(200, 150, 200, 130, fill='black')
hat = canv.create_polygon(180, 75, 220, 75, 200, 20, fill='purple')
canv.update()

#events
def open_mouth():
    canv.itemconfig(mouth, outline='red', fill='black')
def close_mouth():
    canv.itemconfig(mouth, fill='red')

#event mouse
i = 0
def sneezing(event):
    global i
    check = int(i)%int(2)
    print(check)
    if check == 0:
        open_mouth()
        canv.itemconfig(text1, text='Achoo')
    else:
        close_mouth()
        canv.itemconfig(text1, text='Ok')
    i+=1
canv.bind_all('<Button-1>', sneezing)

#events key
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
