import turtle

from turtle import *
from tkinter import *

def borders():
    pu()
    setpos(-275.00, -350.00)
    pd()
    begin_fill()
    color("black" )
    for x in range(2):
        fd(550)
        lt(90)
        fd(700)
        lt(90)
    end_fill()

if __name__ == '__main__':
    borders()
    turtle.exitonclick()