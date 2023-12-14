from rectangle import rectangle
import turtle

def fenetre(x,y):
    '''
    Paramètres :
        x est l'abcisse du centre de la fenêtre
        y est l'ordonnée du sol du niveau de la fenetre
    Remarque:
        dessine une fenetre de 30 pixels sur 30 pixels

    '''

    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.forward(30)  # Forward turtle by 100 units
    turtle.left(90)  # Turn turtle by 90 degree
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.up()
    turtle.forward(15)
    turtle.down()
    turtle.left(90)
    turtle.forward(30)
    turtle.up()
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.down()
    turtle.left(90)
    turtle.forward(30)

if __name__ == '__main__':
    fenetre(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    print("Hello thomas")
    turtle.exitonclick()
