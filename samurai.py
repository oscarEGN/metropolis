import turtle

def draw_samurai_logo():
    turtle.bgcolor("black")
    turtle.pensize(2)
    turtle.speed(2)

    turtle.color("red")
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()

    turtle.color("white")
    turtle.penup()
    turtle.goto(-50, 130)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-35, 100)
    turtle.pendown()
    turtle.right(45)
    turtle.forward(40)

    turtle.penup()
    turtle.goto(-20, 100)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(40)

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    draw_samurai_logo()
