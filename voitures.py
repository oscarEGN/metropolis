import turtle
import random

# Initialisation de la fenêtre Turtle
turtle.setup(width=1920, height=1080)  # HD resolution
turtle.bgcolor("white")
turtle.title("Voitures Volantes")

# Création d'une classe pour les voitures volantes
class VoitureVolante(turtle.Turtle):
    def __init__(self):
        super().__init__(shape="square")  # Utilisez une forme carrée pour la voiture
        self.speed(0)
        self.penup()
        self.color("blue")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(random.randint(-800, 800), random.randint(300, 500))

    def deplacer(self):
        x = self.xcor()
        y = self.ycor()
        y -= 1  # Ajustez la vitesse ici
        self.sety(y)

        # Si la voiture vole trop haut, réinitialisez sa position
        if y < -400:
            y = random.randint(300, 500)
            x = random.randint(-800, 800)
            self.goto(x, y)

# Création d'une liste de voitures volantes
nombre_voitures = 5
voitures_volantes = [VoitureVolante() for _ in range(nombre_voitures)]

# Boucle principale
while True:
    for voiture in voitures_volantes:
        voiture.deplacer()

# Fermer la fenêtre lorsqu'elle est cliquée
turtle.Screen().exitonclick()
