import turtle
from rectangle import rectangle
from trait import trait

def fenetre_balcon(x,y):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte-fenetre-balcon
        y est l'ordonnée du sol du niveau de la porte-fenetre-balcon
    Remarque:
        Dessine une porte-fenetre avec balcon en 2 temps: la porte fenetre de 30 pixels de large par 50 pixels de hauteur
        puis le balcon
    '''
    # porte-fenetre
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.color('black', 'lightgrey')
    turtle.begin_fill()
    for i in range (2):
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()
    
    turtle.up()

    # balcon
    turtle.pensize(3)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(5)
    turtle.right(180)
    turtle.down()
    for i in range(2):
        turtle.forward(40)
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
    
    for i in range(3):
        turtle.forward(5)
        turtle.right(90)
        turtle.forward(25)
        turtle.left(90)
        turtle.forward(5)
        turtle.left(90)
        turtle.forward(25)
        turtle.right(90)
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)


# test

if __name__ == '__main__':
    fenetre_balcon(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()