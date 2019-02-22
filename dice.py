#autor klaudiusz.skowronski claude-plos@o2.pl
#add 2017.02.22
from tkinter import *
from random import randint

def throw():
    text.delete(0.0, END)
    text.insert(END, str(randint(1,6)))

window = Tk()

text = Text(window, width=1, height=1)

butA = Button(window, text='Click, to throw the dice', command=throw)

text.pack()
butA.pack()

input()
