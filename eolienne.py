import turtle

def eolienne():
    turtle.pencolor("gray")
    turtle.pensize(4)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(500)
    turtle.back(500)
    turtle.left(90)
    turtle.pensize(2)
    turtle.fillcolor("white")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(50)
        turtle.right(120)
        turtle.forward(10)
        turtle.right(70)
        turtle.forward(46.25)
        turtle.left(100)
    turtle.end_fill()
    turtle.penup()

if __name__ == '__main__':
    eolienne()
    turtle.exitonclick()