import turtle
import random

def dessiner_goutte(x, y, longueur):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(270)  # Orienté vers le bas
    turtle.forward(longueur)
    turtle.penup()  # Relever le stylo pour éviter de relier les gouttes

def animer_gouttes_de_pluie(nombre_gouttes):
    turtle.speed(0)
    turtle.hideturtle() # Couleur de fond simulant le ciel
    turtle.color("blue")  # Couleur des gouttes de pluie
    turtle.title("Gouttes de pluie")

    largeur, hauteur = turtle.window_width(), turtle.window_height()

    gouttes = []

    # Initialiser les positions des gouttes
    for _ in range(nombre_gouttes):
        x = random.randint(-int(largeur / 2), int(largeur / 2))
        y = random.randint(0, int(hauteur / 2))
        longueur = random.randint(5, 20)
        gouttes.append([x, y, longueur])

    def animation():
        turtle.clear()  # Effacer les anciennes gouttes
        for i in range(len(gouttes)):
            x, y, longueur = gouttes[i]
            y -= 5  # Ajustez la vitesse ici
            gouttes[i] = [x, y, longueur]
            dessiner_goutte(x, y, longueur)

            # Si la goutte touche le haut de la fenêtre, réinitialisez sa position
            if y < -int(hauteur / 2):
                gouttes[i] = [random.randint(-int(largeur / 2), int(largeur / 2)), random.randint(0, int(hauteur / 2)), longueur]

        turtle.ontimer(animation, 50)  # Appel récursif de la fonction toutes les 50 millisecondes

    animation()

    turtle.done()
