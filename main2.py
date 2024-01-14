import turtle
from turtle import Screen
from random import randint, shuffle
from sol import sol
from immeuble import immeuble
from lampadaire import lampadaire
import winsound
from borders import borders
from buildings import buildings
from windows import windows
from stars import draw_star
from stars import set_turtle, move_turtle
from legs import draw_leg
from eye import draw_eye
from sunset import draw_sunset
from cherry_blossom_tree import draw_cherry_blossom_tree
import random
# ------------------------------
# ------------------------------
# ------------------------------



def main():

    


    turtle.setup(1920, 1080)
    screen = Screen()
    turtle.speed(0)
    # On définit la hauteur du sol
    y_sol = -250
    turtle.hideturtle
    turtle.tracer(False)

    COLOR = (0.60156, 0, 0.99218)  # (154, 0, 254)
    TARGET = (0.86328, 0.47656, 0.31250)  # (221, 122, 80)
    WIDTH, HEIGHT = screen.window_width(), screen.window_height()


    

   
    # Dessin du sol de la rue
    sol(y_sol)
    #création du ciel
    turtle.fillcolor('midnightblue')
    turtle.pensize(0)
    turtle.begin_fill()
    turtle.up()
    turtle.goto(-1100,-500)
    turtle.down()
    turtle.forward(2500)
    turtle.left(90)
    turtle.forward(1080)
    turtle.left(90)
    turtle.forward(2500)
    turtle.left(90)
    turtle.forward(1080)
    turtle.left(90)
    turtle.end_fill()

    deltas = [(hue - COLOR[index]) / HEIGHT for index, hue in enumerate(TARGET)]

    
    turtle.color(COLOR)

    turtle.penup()
    turtle.goto(-WIDTH/2, HEIGHT/2)
    turtle.pendown()

    direction = 1

    for distance, y in enumerate(range(HEIGHT//2, -HEIGHT//2, -1)):

        turtle.forward(WIDTH * direction)
        turtle.color([COLOR[i] + delta * distance for i, delta in enumerate(deltas)])
        turtle.sety(y)

        direction *= -1

    #Dessin de la lune
    turtle.hideturtle()
    turtle.goto(-500,300)
    turtle.pendown()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

    #creation etoile 
    turtle.pencolor("white")
    turtle.pensize(5)
    turtle.penup()
    for i in range(100):
        rx = randint(-900,900)
        ry = randint(-200,900)
        turtle.goto(rx,ry)
        turtle.pendown()
        turtle.forward(1)
        turtle.penup()
    turtle.pencolor('black')


    # flag
    flag = turtle.Turtle()
    set_turtle(flag, '#624A3A', '#624A3A', 7)
    move_turtle(flag, 195, -257)
    flag.lt(90)
    flag.fd(350)

    set_turtle(flag, '#002395', '#ED2939', 7)
    flag.begin_fill()
    flag.lt(-90)
    flag.fd(120)
    flag.lt(-90)
    flag.fd(70)
    flag.lt(-90)
    flag.fd(120)
    flag.end_fill()
    flag.hideturtle()

    #Dessin Grande Ours
    star = turtle.Turtle()
    set_turtle(star, '#002395', '#002395', 2)
    draw_star(star, 230, 63)


    #création du sol
    turtle.fillcolor('green')
    turtle.pensize(0)
    turtle.begin_fill()
    turtle.up()
    turtle.goto(-1100,-200)
    turtle.down()
    turtle.forward(2500)
    turtle.right(90)
    turtle.forward(1080)
    turtle.right(90)
    turtle.forward(2500)
    turtle.right(90)
    turtle.forward(1080)
    turtle.right(90)
    turtle.end_fill()
   
    #cerisiers
    draw_cherry_blossom_tree()

    #Dessin de la route
    turtle.fillcolor('dimgrey')
    turtle.pensize(0)
    turtle.begin_fill()
    turtle.up()
    turtle.goto(-1100,-300)
    turtle.down()
    turtle.forward(2500)
    turtle.right(90)
    turtle.forward(1080)
    turtle.right(90)
    turtle.forward(2500)
    turtle.right(90)
    turtle.forward(1080)
    turtle.right(90)
    turtle.end_fill()
    #dessin lampadaire
    turtle.goto(-740,-300)
    for i in range(10):
        lampadaire()
    #dessin ligne route
    turtle.goto(-1100,-375)
    turtle.pencolor("gray70")
    turtle.pensize(10)
    for i in range(5):
        turtle.forward(100)
        turtle.penup()
        turtle.forward(100)
        turtle.pendown()
        turtle.forward(200)
        turtle.penup()
    turtle.pencolor("black")

    


    # Dessin des immeubles
    turtle.pensize(3)
    for i in range(10):
        immeuble(-900+i*180, y_sol)

    
    turtle.tracer(True)

    

    #La voiture
    car = turtle.Turtle()
    car.hideturtle()
    car.penup()
    car.goto(-1000, -360)
    turtle.register_shape('yellow.gif') 
    
    car.shape('yellow.gif')
    car.speed(1)
    #car.shapesize(1)
    #car.setheading(0)    
    car.showturtle()    
    
    winsound.PlaySound('car.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
    car.forward(2000)

    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
    

if __name__ == '__main__':
    main()


