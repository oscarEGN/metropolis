# cherry_blossom_tree.py

from turtle import *
from random import *
from math import *

def tree(n, l):
    pd()  # Writing
    # Shadow effect
    t = cos(radians(heading() + 45)) / 8 + 0.25
    pencolor(t, t, t)
    pensize(n / 3)
    forward(l)  # Draw a branch

    if n > 0:
        b = random() * 15 + 10  # Right branch deflection angle
        c = random() * 15 + 10  # Left branch deflection angle
        d = l * (random() * 0.25 + 0.7)  # The length of the next branch

        # Turn right at a certain angle, Draw the right branch
        right(b)
        tree(n - 1, d)

        # Turn left at a certain angle, Draw left branch
        left(b + c)
        tree(n - 1, d)

        # Turn around
        right(c)
    else:
        # Painting leaves
        right(90)
        n = cos(radians(heading() - 45)) / 4 + 0.5
        pencolor(n, n * 0.8, n * 0.8)
        circle(3)
        left(90)

        # Add to 0.3 times of falling leaves
        if random() > 0.7:
            pu()  # Falling
            t = heading()
            an = -40 + random() * 40
            setheading(an)
            dis = int(800 * random() * 0.5 + 400 * random() * 0.3 + 200 * random() * 0.2)
            forward(dis)
            setheading(t)

            # Painting leaves
            pd()
            right(90)
            n = cos(radians(heading() - 45)) / 4 + 0.5
            pencolor(n * 0.5 + 0.5, 0.4 + n * 0.4, 0.4 + n * 0.4)
            circle(2)
            left(90)
            pu()  # return
            t = heading()
            setheading(an)
            backward(dis)
            setheading(t)
            pu()

    backward(l)  # return

def draw_cherry_blossom_tree():
    bgcolor(0.5, 0.5, 0.5)  # Background color
    ht()  # Hide turtle
    speed(0)  # Speed 1-10 gradual, 0 Fastest
    tracer(0, 0)
    pu()  # Pen-up
    backward(100)
    left(90)  # Turn left 90 degree
    pu()  # Pen-up
    backward(300)  # Back off 300
    tree(12, 100)  # Recursion 7 layers done