import turtle
from random import randint, shuffle
from sol import sol
from immeuble import immeuble
# ------------------------------
# ------------------------------
# ------------------------------

def main():
    turtle.setup(1920, 1080)
    turtle.speed(0)
    # On définit la hauteur du sol
    y_sol = -250
   
    # Dessin du sol de la rue
    sol(y_sol)
    #création du ciel
    turtle.fillcolor('darkblue')
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
    #Dessin des etoiles


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

    #dessin ligne route
    turtle.goto(-1100,-375)
    turtle.pencolor("white")
    turtle.pensize(10)
    for i in range(10):

        turtle.forward(100)
        turtle.penup()
        turtle.forward(100)
        turtle.pendown()
        turtle.forward(100)
    
    turtle.pencolor("black")
    # Dessin des immeubles
    turtle.pensize(3)
    for i in range(10):
        immeuble(-900+i*180, y_sol)

    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
    

if __name__ == '__main__':
    main()



