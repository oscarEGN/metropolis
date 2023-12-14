import turtle

def toit1(x, y_sol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit triangulaire noir de base 160 pixels
    et de hauteur centrale 40 pixels
    '''
    turtle.up()
    y = y_sol+60*niveau
    turtle.goto(x+70,y)

    turtle.down()
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.forward(80)

    turtle.left(153.44)
    turtle.forward(89.44)

    turtle.left(53.12)
    turtle.forward(89.44)

    turtle.left(153.44)
    turtle.forward(80)
    turtle.end_fill()

if __name__ == '__main__':
    toit1(0,0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()