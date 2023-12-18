import turtle
from random import randint, shuffle
from sol import sol
from immeuble import immeuble
from lampadaire import lampadaire
#import winsound
# ------------------------------
# ------------------------------
# ------------------------------

def main():
    turtle.setup(1920, 1080)
    turtle.speed(0)
    # On définit la hauteur du sol
    y_sol = -250
    turtle.hideturtle
   
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
    
    #winsound.PlaySound('car.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
    car.forward(2000)

    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
    

if __name__ == '__main__':
    main()



