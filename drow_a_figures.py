#autor klaudiusz.skowronski claude-plos@o2.pl
#title:drow a square
#add 2017.02.22
from tkinter import *
import time
#from random import *

canvSize = 500
window = Tk()
window.title('Figures');
canv = Canvas(window, width=canvSize, height=canvSize)
canv.pack()
rectangle = canv.create_rectangle(100, 100, 300, 200, outline='red') # x, y w, h -
square = canv.create_rectangle(30, 30, 80, 80) #
oval = canv.create_oval(100, 100, 300, 200, outline='blue')
circle = canv.create_oval(30, 30, 80, 80, outline='blue', fill='orange')
canv.update()


print("Start : %s" % time.ctime())
time.sleep(5.5)    # pause 5.5 seconds
print("End : %s" % time.ctime())
print("end program")
