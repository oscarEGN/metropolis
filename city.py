import turtle
from turtle import *
from random import *
from random import randint, shuffle
from sol import sol
from immeuble import immeuble
from lampadaire import lampadaire
from eolienne import eolienne
from arbre import Tree
from pluie import animer_gouttes_de_pluie

def generer_smart_city():
    screen = Screen()
    turtle.setup(1920, 1080)
    turtle.speed(0)
    turtle.hideturtle
    turtle.tracer(False)
    COLOR = (0.60156, 0, 0.99218)  # (154, 0, 254)
    TARGET = (0.86328, 0.47656, 0.31250)  # (221, 122, 80)
    WIDTH, HEIGHT = screen.window_width(), screen.window_height()
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
    
    # On définit la hauteur du sol
    y_sol = -250
   
    # Dessin du sol de la rue
    sol(y_sol)
    
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

    #dessin lune
    xr1= randint(-700, 700)
    turtle.goto(xr1,300)
    turtle.pendown()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.penup()

    #dessin eolienne
    turtle.goto(-900,200)
    turtle.pendown()
    for i in range(13):
        xer=randint(120,300)
        eolienne()
        turtle.forward(xer)
    
    #dessin building
    couleur_batiment = ["#363432", "#196774", "#90A19D", "#F0941F", "#BD2A2E", "#3B3936", "#889C9B", "#486966"]
    couleur_fenetre = ["#F2F2F2", "#202022"]
    def building(x, y, h, w, col):
        turtle.penup()
        color(col)
        pencolor(col)
        setpos(x, y)
        setheading(90)
        pendown()
        begin_fill()
        for i in range(2):
            forward(h)
            right(90)
            forward(w)
            right(90)
        end_fill()
        penup()


    x = 1920/-2
    largeur_liste = [90, 110, 130] 
    n = 20

    for m in range(n + 1):
        b = choice(largeur_liste) 
        y = -200
        h = randrange(60, 600, 30) + 15
        building(x, y, h, b, choice(couleur_batiment))
        for w in range(int(h/30)): 
            for i in range(10, b, 20):
                building(x + i, y + 10, 20, 10, choice(couleur_fenetre))
            y = y + 30
        x = x + b + 1
    turtle.left(270)

    #arbre
    turtle.goto(-1100,-275)
    turtle.left(90)
    for i in range(35):
        turtle.right(90)
        turtle.left(90)
        Tree(45)
        turtle.penup()
        turtle.right(90)
        turtle.forward(70)
        turtle.left(90)
    turtle.right(90)

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
    #ligne de Bus
    turtle.penup()
    turtle.pencolor("gold")
    turtle.goto(-75,-365)
    turtle.pendown()
    turtle.write("BUS", font=("Verdana",38, "normal"))
    turtle.penup()
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

    #animer_gouttes_de_pluie(50)

    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()