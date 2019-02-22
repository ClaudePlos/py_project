#autor klaudiusz.skowronski claude-plos@o2.pl
#title:use the colors 
#add 2017.02.22
from tkinter import *
from random import * 

canvSize = 500
window = Tk()

canv = Canvas(window, width=canvSize, height=canvSize)
canv.pack()

#for x in range(6):
while True:
    color = choice(['pink','orange','green','purple','red','yellow'])
    x0 = randint(0, canvSize)
    y0 = randint(0, canvSize)
    d = randint(0, canvSize/5)
    canv.create_oval(x0, y0, x0 + d, y0 + d, fill=color)
    window.update()
