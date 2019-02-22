from tkinter import *

def p1App():
    print('Thx!');

def p2App():
    print('Auu. It\'s hurt!');

window = Tk()

butA = Button(window, text='Clik me!', command=p1App)
butB = Button(window, text='Do not clik!', command=p2App)

butA.pack()
butB.pack()
