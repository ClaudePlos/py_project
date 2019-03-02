#autor klaudiusz.skowronski claude-plos@o2.pl
#title:drow alien
#add 2017.02.23
from tkinter import *
#from random import *

canvHeight = 500
canvWidth  = 800
window = Tk()
window.title('Submarine kill the boubbles');
c = Canvas(window, width=canvWidth, height=canvHeight, bg='darkblue')
c.pack()

subm_p1 = c.create_polygon(5, 5, 5, 25, 30, 15, fill='red')
subm_p2 = c.create_oval(0, 0, 30, 30, outline='red')
radius_subm = 15
center_x = canvWidth / 2
center_y = canvHeight / 2
c.move(subm_p1, center_x, center_y)
c.move(subm_p2, center_x, center_y)



input("Press enter to exit ;)")
