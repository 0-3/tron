# turtle Game
import turtle
import math
import random
import time

# set up screen
wn = turtle.Screen()
wn.bgcolor("lightgreen")

# draw border
mypen = turtle.Turtle()
mypen.speed(100)
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()
mypen.penup()
mypen.setposition(-295, 305)
mypen.write("Eat 8 circles to win!", font=("Arial", 16, "normal"))
mypen.setposition(0, 305)
mypen.write("Score:", font=("Arial", 16, "normal"))
mypen.setposition(75, 305)

# create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.penup()
player.speed(0)

# create game goal
goal = turtle.Turtle()
goal.color("red")
goal.shape("circle")
goal.penup()
goal.speed(0)
goal.setposition(-100, -100)

# set speed of turtle
speed = 1

# define variables
goalspeed = 1
goals = 0


# define functions
def turnleft():
    player.setheading(180)


def turnright():
    player.setheading(0)


def turnup():
    player.setheading(90)


def turndown():
    player.setheading(270)


def increasespeed():
    global speed
    speed += 1
    if(speed > 10):
        speed = 10

def decreasespeed():
    global speed
    speed -= 1
    if(speed < 1):
        speed = 1


def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if d < 20:
        return True
    else:
        return False


# key bindings
turtle.listen()
turtle.onkey(turnleft, "a")
turtle.onkey(turnright, "d")
turtle.onkey(turnup, "w")
turtle.onkey(turndown, "s")
turtle.onkey(increasespeed, "Up")
turtle.onkey(decreasespeed, "Down")

while goals < 8:
    player.forward(speed)

    # boundary check x axis (player)
    if player.xcor() > 290 or player.xcor() < -290:
        player.right(180)

    # boundary check y axis (player)
    if player.ycor() > 290 or player.ycor() < -290:
        player.right(180)

    # collision check
    if isCollision(player, goal):
        goal.setposition(random.randint(-300, 300), random.randint(-300, 300))
        goal.right(random.randint(0, 360))
        goalspeed += 2
        goals += 1
        mypen.write("I", font=("Arial", 16, "normal"))
        mypen.forward(5)

    # move the goal
    goal.forward(goalspeed)

    # boundary check x axis (food)
    if goal.xcor() > 290 or goal.xcor() < -290:
        goal.right(random.randint(160, 200))

    # boundary check y axis (food)
    if goal.ycor() > 290 or goal.ycor() < -290:
        goal.right(random.randint(160, 200))
    # failsafe
    if goal.ycor() > 320 or goal.ycor() < -320 or goal.xcor() > 320 or goal.xcor() < -320:
        goal.setposition(0, 0)

# end game
player.hideturtle()
goal.hideturtle()
mypen.setposition(-285, 0)
wn.bgcolor("gold")
mypen.write("Congrats you ate all eight fruits!", font=("Arial", 28, "bold"))
time.sleep(5)
wn.bye()