import turtle
import subprocess

# Fonction pour lancer le script principal
def lancer_partie(x, y):
    subprocess.run(["python3", "main.py"])

# Fonction pour changer la couleur du bouton lorsqu'il est pressé
def changer_couleur():
    turtle.color("red")

# Configuration de la fenêtre Turtle
fenetre = turtle.Screen()
fenetre.title("Metropolis Menu")
fenetre.bgcolor("deepskyblue")
fenetre.setup(width=1920, height=1080)



# Ajout d'un logo en tant qu'image
fenetre.addshape("assets/logoMetro.gif")
logo_turtle = turtle.Turtle()
logo_turtle.shape("assets/logoMetro.gif")
logo_turtle.penup()
logo_turtle.goto(0, 185)

# Dessiner un simple bouton blanc
turtle.shape("square")
turtle.shapesize(stretch_wid=2, stretch_len=12)  # Ajustez la taille du bouton
turtle.color("goldenrod")

turtle.penup()
turtle.goto(0, -195)
turtle.write("LANCER !", align="center", font=("Arial", 20, "bold"))

# Liaison du clic sur le bouton avec la fonction lancer_partie
turtle.onclick(lancer_partie)

# Liaison du clic pressé sur le bouton avec la fonction changer_couleur
#turtle.onkeypress(changer_couleur, "Button-1")

# Message d'instruction
instruction_turtle = turtle.Turtle()
instruction_turtle.hideturtle()
instruction_turtle.penup()
instruction_turtle.goto(0, -260)
instruction_turtle.write("Cliquez sur le bouton pour lancer la partie", align="center", font=("Arial", 14, "normal"))

#Texte lancer
textLancer = turtle.Turtle()
textLancer.hideturtle()
textLancer.penup()
textLancer.goto(0, -205)
textLancer.write("LANCER !", align="center", font=("Arial", 20, "bold"))

#Credits
credits = turtle.Turtle()
credits.hideturtle()
credits.penup()
credits.goto(0, -350)
credits.write("Un projet de Oscar E. Adrien D. et Evan C.", align="center", font=("Arial", 11, "normal"))

# Boucle principale
fenetre.listen()
turtle.done()
