import random

from facade import facade
from random import shuffle
from porte import porte
from fenetre import fenetre
from random import randint
import turtle

def rdc(x, y_sol, c_facade, c_porte):
    '''
    Paramètres
        x : (int) abscisse du centre
        y_sol : ordonnée du sol du la rue
        c_facade : couleur de la façade
        c_porte : couleur de la porte
    remarque:
        Cette fonction dessine le rdc en 2 étapes
        D'abord la façade
        Puis les 3 élements : 1 porte et 2 fenêtres disposées au hasard
    '''
    # Dessine la facade
    facade(x, y_sol, c_facade, 0)
    # Construit les 3 éléments (1 porte et 2 fenetres)
    posPorte = random.randint(0,2)
    for i in range(3):
        x += 20
        if posPorte == i:
            porte(x,y_sol, c_porte)
        else:
            fenetre(x, y_sol + 20)
        x += 20

    pass

if __name__ == '__main__':
    rdc(0,0,"red","green")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()