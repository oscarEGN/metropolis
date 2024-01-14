from tkinter import *
from turtle import *

def windows():
    def win():
        pd()
        begin_fill()
        color("white")
        for x in range(4):
            fd(15)
            lt(90)
        end_fill()
        pu()

    pu()
    setpos(-210.00, -7.00)
    win()
    setpos(-135.00, 175.00)
    win()
    setpos(-135.00, 200.00)
    win()
    setpos(-60.00, -100.00)
    win()
    setpos(-30.00, 115.00)
    win()
    setpos(90.00, 105.00)
    win()

if __name__ == '__main__':
    windows()
    turtle.exitonclick()