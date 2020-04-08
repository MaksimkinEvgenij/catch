from tkinter import *
from random import randrange as rnd, choice
import time

root = Tk()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
root.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue']

score = 0

balls =[]   # список созданных шаров

def new_ball():
    """ Создание очередного шара. """
    #canv.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    dx = rnd (-10, 10)
    dy = rnd (-10, 10)
    r = rnd(30,50)

    if rnd(0,2) == 0:
        balls.append([canv.create_rectangle(x-r,y-r,x+r,y+r,fill = choice(colors), width=0), x, y, dx, dy, r, 'rectangle'])
    else:
        balls.append([canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0), x, y, dx, dy, r, 'oval'])

    
    root.after(1000,new_ball)


def move_balls():
    """ Движение шаров. """
    for i in balls:
        if i:
            i[1] += i[3]    # изменение x на dx
            i[2] += i[4]    # изменение y на dy
            canv.move(i[0], i[3], i[4])
    reflection_from_walls()
    root.after(100,move_balls)


def reflection_from_walls():
    """ Отражение от стен шаров. """
    # изменение dx и dy, если шар доходит до размеров окна
    for i in balls:
        if i:
            if i[1] + i[5] > SCREEN_WIDTH or i[1] - i[5] < 0:
                i[3] *= -1
            if i[2] + i[5] > SCREEN_HEIGHT or i[2] - i[5] < 0:
                i[4] *= -1    

def click(event):
    """ Проверка попадания щелчком мыши в шар. """
    global score

    for i in range(len(balls)):
        if balls[i]:
            if ((balls[i][1] - event.x)**2 + (balls[i][2] - event.y)**2)**(1/2) <= balls[i][5]:
                print('Попал')
                if balls[i][6] == 'rectangle':
                    score += 1
                elif balls[i][6] == 'oval':
                    score += 2
                canv.delete(balls[i][0])
                balls[i] = None


def save_score_in_the_end_of_program():
    with open('results.txt', 'a') as file:
        file.write(f'{score}\n')

new_ball()
move_balls()
canv.bind('<Button-1>', click)
mainloop()
save_score_in_the_end_of_program()

