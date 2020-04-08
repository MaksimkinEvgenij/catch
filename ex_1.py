from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue']

score = 0

balls =[]

def new_ball():
    """ Создание очередного шара. """
    global x,y,r
    #canv.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    balls.append(canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0))
    

    
    root.after(1000,new_ball)


def move_balls():
    """ Движение шаров. """
    for b in balls:
        canv.move(b, +10, +10)
    root.after(100,move_balls)


def click(event):
    """ Проверка попадания щелчком мыши в шар. """
    global score
    if ((x - event.x)**2 + (y - event.y)**2)**(1/2) <= r:
        print('Попал')
        score += 1
        

new_ball()
move_balls()
canv.bind('<Button-1>', click)
mainloop()
