import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Turtle object
t = turtle.Turtle()
t.speed(3)
t.pensize(3)

# ----- Equilateral Triangle -----
t.color("red", "yellow")
t.begin_fill()

for i in range(3):
    t.forward(100)
    t.left(120)

t.end_fill()

# Move to next shape
t.penup()
t.goto(-150, -120)
t.pendown()

# ----- Rectangle -----
t.color("blue", "green")
t.begin_fill()

for i in range(2):
    t.forward(150)
    t.left(90)
    t.forward(80)
    t.left(90)

t.end_fill()

# Move to next shape
t.penup()
t.goto(150, -50)
t.pendown()

# ----- Hexagon -----
t.color("purple", "orange")
t.begin_fill()

for i in range(6):
    t.forward(70)
    t.left(60)

t.end_fill()

turtle.done()