import turtle
import time

print("Player 1: WASD")
print("Player 2: Arrow Keys")
print("Player 3: IJKL")
print("Player 4: TFGH")
stPlayers = input("Number of players: ")
intPlayers = int(stPlayers)

scr = turtle.Screen()

global alive
alive = []

global p1
global p2
global p3
global p4

p1 = turtle.Turtle()
p2 = turtle.Turtle()
p3 = turtle.Turtle()
p4 = turtle.Turtle()
p1.hideturtle()
p2.hideturtle()
p3.hideturtle()
p4.hideturtle()


def t1(t):
    #Define Player 1
    t.pensize(3)
    t.shape("turtle")
    t.setheading(0)
    t.color("red")
    t.goto(1, 0)
    t.st()
def t2(t):
    #Define Player 2
    t.pensize(3)
    t.shape("triangle")
    t.setheading(180)
    t.color("blue")
    t.goto(-1, 0)
    t.st()
def t3(t):
    #Define Player 3
    t.pensize(3)
    t.shape("circle")
    t.setheading(270)
    t.color("green")
    t.goto(0, -1)
    t.st()
def t4(t):
    #Define Player 4
    t.pensize(3)
    t.shape("square")
    t.setheading(90)
    t.color("purple")
    t.goto(0, 1)
    t.st()
def defTurtle(num):
    global alive
    if(num <= 1):
        t1(p1)
        alive = [1]
    if(num == 2):
        t1(p1)
        t2(p2)
        alive = [1, 2]
    if(num == 3):
        t1(p1)
        t2(p2)
        t3(p3)
        alive = [1, 2, 3]
    if(num >= 4):
        t1(p1)
        t2(p2)
        t3(p3)
        t4(p4)
        alive = [1, 2, 3, 4]

def drawBoard():
    t = turtle.Turtle()
    t.speed(100)
    t.up()
    t.goto(-200, 200)
    t.down()
    t.forward(400)
    t.right(90)
    t.forward(400)
    t.right(90)
    t.forward(400)
    t.right(90)
    t.forward(400)
    t.right(90)
    t.hideturtle()

def kill(p, t):
    alive.remove(p)
    t.hideturtle()
    w = turtle.Turtle()
    w.ht()
    w.up()
    w.goto(-200 + (p-1)*100, -240)
    w.st()
    w.write("Player " + str(p) + " has died!", font=("Arial", 9, "normal"))
    w.hideturtle()

global xcors, ycors

pointsOccupied = {}

def moveTurtle(p, t, d):
    xp = str(round(t.pos()[0]))
    yp = str(round(t.pos()[1]))
    t.forward(1)
    if xp in d:
        if yp in d[xp]:
            kill(p, t)
            return
        else:
            d[xp].append(yp)
    else:
        d[xp] = [yp]
    if(t.pos()[0] >=200 or t.pos()[0] <= -200 or t.pos()[1] >= 200 or t.pos()[1] <= -200):
        kill(p, t)
        return
    else:
        return

def announceWinner(winner):
    t = turtle.Turtle()
    t.color('white')
    t.begin_fill()
    t.speed(1000)
    t.hideturtle()
    t.goto(-500, 500)
    t.forward(1000)
    t.right(90)
    t.forward(1000)
    t.right(90)
    t.forward(1000)
    t.right(90)
    t.forward(1000)
    t.right(90)
    t.hideturtle()
    t.end_fill()
    t.goto(0, 0)
    t.showturtle()
    t.color('black')
    t.write("Player " + str(winner) + " has won the game!", align='center', font=("Arial", 32, "normal"))
    t.ht()

drawBoard()
defTurtle(intPlayers)

def turnUp1():
    if(p1.heading() != 270):
        p1.setheading(90)
def turnDown1():
    if(p1.heading() != 90):
        p1.setheading(270)
def turnLeft1():
    if(p1.heading() != 0):
        p1.setheading(180)
def turnRight1():
    if(p1.heading() != 180):
        p1.setheading(0)

def turnUp2():
    if(p2.heading() != 270):
        p2.setheading(90)
def turnDown2():
    if(p2.heading() != 90):
        p2.setheading(270)
def turnLeft2():
    if(p2.heading() != 0):
        p2.setheading(180)
def turnRight2():
    if(p2.heading() != 180):
        p2.setheading(0)

def turnUp3():
    if(p3.heading() != 270):
        p3.setheading(90)
def turnDown3():
    if(p3.heading() != 90):
        p3.setheading(270)
def turnLeft3():
    if(p3.heading() != 0):
        p3.setheading(180)
def turnRight3():
    if(p3.heading() != 180):
        p3.setheading(0)

def turnUp4():
    if(p4.heading() != 270):
        p4.setheading(90)
def turnDown4():
    if(p4.heading() != 90):
        p4.setheading(270)
def turnLeft4():
    if(p4.heading() != 0):
        p4.setheading(180)
def turnRight4():
    if(p4.heading() != 180):
        p4.setheading(0)
    
scr.onkey(turnUp1, "w")
scr.onkey(turnDown1, "s")
scr.onkey(turnLeft1, "a")
scr.onkey(turnRight1, "d")
scr.onkey(turnUp2, "Up")
scr.onkey(turnDown2, "Down")
scr.onkey(turnLeft2, "Left")
scr.onkey(turnRight2, "Right")
scr.onkey(turnUp3, "i")
scr.onkey(turnDown3, "k")
scr.onkey(turnLeft3, "j")
scr.onkey(turnRight3, "l")
scr.onkey(turnUp4, "t")
scr.onkey(turnDown4, "g")
scr.onkey(turnLeft4, "f")
scr.onkey(turnRight4, "h")
scr.listen()

while (len(alive) > 1):

    if(1 in alive):
        moveTurtle(1, p1, pointsOccupied)
    if(2 in alive):
        moveTurtle(2, p2, pointsOccupied)
    if(3 in alive):
        moveTurtle(3, p3, pointsOccupied)
    if(4 in alive):
        moveTurtle(4, p4, pointsOccupied)

announceWinner(alive[0])
time.sleep(10)
