#autor klaudiusz.skowronski claude-plos@o2.pl
#title:drow alien
#add 2018.12.23
#subm - submarine
from tkinter import *
from random import randint
from time import sleep, time
from math import sqrt

canvHEIGHT = 500
canvWIDTH  = 800
window = Tk()
window.title('Submarine kill the boubbles');
c = Canvas(window, width=canvWIDTH, height=canvHEIGHT, bg='darkblue')
c.pack()

#submarin
subm_p1 = c.create_polygon(5, 5, 5, 25, 30, 15, fill='red')
subm_p2 = c.create_oval(0, 0, 30, 30, outline='red')
sub_RADIUS = 15
center_x = canvWIDTH / 2
center_y = canvHEIGHT / 2
c.move(subm_p1, center_x, center_y)
c.move(subm_p2, center_x, center_y)

#key support
SPEED_sumb = 10
def run_subm(event):
    if event.keysym == 'Up':
        c.move(subm_p1, 0, -SPEED_sumb)
        c.move(subm_p2, 0, -SPEED_sumb)
    if event.keysym == 'Down':
        c.move(subm_p1, 0, SPEED_sumb)
        c.move(subm_p2, 0, SPEED_sumb)
    if event.keysym == 'Left':
        c.move(subm_p1, -SPEED_sumb, 0)
        c.move(subm_p2, -SPEED_sumb, 0)
    if event.keysym == 'Right':
        c.move(subm_p1, SPEED_sumb, 0)
        c.move(subm_p2, SPEED_sumb, 0)
c.bind_all('<Key>', run_subm)

#boubbles
boubble_id = list()
boubble_radius = list()
boubble_speed = list()
MINradiusBoubble = 10
MAXradiusBouble = 30
MAXspeedBoubble = 10
SPACE = 100
def create_boubble():
    x = canvWIDTH + SPACE
    y = randint(0, canvHEIGHT)
    r = randint(MINradiusBoubble, MAXradiusBouble)
    id1 = c.create_oval(x - r, y -r, x + r, y + r, outline='white')
    boubble_id.append(id1)
    boubble_radius.append(r)
    boubble_speed.append(randint(1,MAXspeedBoubble))
#
def run_boubble():
    for i in range(len(boubble_id)):
        c.move(boubble_id[i], -boubble_speed[i], 0)
#
def read_coordinates(num_id):
    poz = c.coords(num_id)
    x = (poz[0] + poz[2])/2
    y = (poz[1] + poz[3])/2
    return x, y
#
def delete_boubble(i):
    print("Spr: " + str(i))
    del boubble_radius[i]
    del boubble_speed[i]
    c.delete(boubble_id[i])
    del boubble_id[i]
#
def delete_boubbles():
    for i in range(len(boubble_id)-1, -1, -1):
        x, y = read_coordinates(boubble_id[i])
        if x < -SPACE:
            delete_boubble(i)
#
def distance(id1, id2):
    x1, y1 = read_coordinates(id1)
    x2, y2 = read_coordinates(id2)
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)
#
def incident():
    point = 0
    for boubble in range(len(boubble_id)-1, -1, -1):
        if distance(subm_p2, boubble_id[boubble]) < (sub_RADIUS + boubble_radius[boubble]):
            point += (boubble_radius[boubble] + boubble_speed[boubble])
            delete_boubble(boubble)
    return point


boubble_RANDOM = 10
score = 0
#main loop of the game
while True:
    if randint(1, boubble_RANDOM) == 1:
        create_boubble()
    run_boubble()
    delete_boubbles()
    score += incident()
    print(score)
    window.update()
    sleep(0.01)

input("Press enter to exit ;)")
