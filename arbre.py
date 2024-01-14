from turtle import *
import random

# Draw the trunk of the cherry tree(60,t)
def Tree(branch):
    if branch > 3:
        if 8 <= branch <= 10:
            if random.randint(0, 2) == 0:
                color('SpringGreen4')  # White
            else:
                color('green3')  # Pale coral
            pensize(branch / 3)
        elif branch < 8:
            if random.randint(0, 1) == 0:
                color('green3')
            else:
                color('green4')  # Pale coral
            pensize(branch / 2)
        else:
            color('sienna')  # Sienna
            pensize(branch / 8)  # 6
        forward(branch)
        a = 1.5 * random.random()
        right(20 * a)
        b = 1.5 * random.random()
        Tree(branch - 10 * b)
        left(40 * a)
        Tree(branch - 10 * b)
        right(20 * a)
        up()
        backward(branch)
        down()

if __name__ == '__main__':
    Tree()
    exitonclick()