import turtle
import winsound

wn = turtle.Screen()
wn.title("pong by kriv0")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score_1 = 0
score_2 = 0

# Stick 1
stick_1 = turtle.Turtle()
stick_1.speed(0)
stick_1.shape("square")
stick_1.color("white")
stick_1.shapesize(stretch_wid=5, stretch_len=1)
stick_1.penup()
stick_1.goto(-350, 0)

# Stick 2
stick_2 = turtle.Turtle()
stick_2.speed(0)
stick_2.shape("square")
stick_2.color("white")
stick_2.shapesize(stretch_wid=5, stretch_len=1)
stick_2.penup()
stick_2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("P1: 0 | P2: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def stick_1_up():
    y = stick_1.ycor()
    y += 20
    stick_1.sety(y)

def stick_1_down():
    y = stick_1.ycor()
    y -= 20
    stick_1.sety(y)

def stick_2_up():
    y = stick_2.ycor()
    y += 20
    stick_2.sety(y)

def stick_2_down():
    y = stick_2.ycor()
    y -= 20
    stick_2.sety(y)

# Keybinds
wn.listen()
wn.onkeypress(stick_1_up, "w")
wn.onkeypress(stick_1_down, "s")
wn.onkeypress(stick_2_up, "Up")
wn.onkeypress(stick_2_down, "Down")

# Game Loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("P1: {} | P2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("P1: {} | P2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))

    # Stick-ball collision
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < stick_1.ycor() + 40 and ball.ycor() > stick_1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < stick_2.ycor() + 40 and ball.ycor() > stick_2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    