import turtle

def lampadaire():
    turtle.pencolor("darkgray")
    turtle.pensize(7)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(90)
    turtle.right(90)
    turtle.pencolor("sandy brown")
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.pensize(4)
    turtle.circle(10)
    turtle.end_fill()
    turtle.pencolor("darkgray")
    turtle.left(90)
    turtle.penup()
    turtle.back(90)
    turtle.right(90)
    turtle.forward(180)

if __name__ == '__main__':
    lampadaire()
    turtle.exitonclick()