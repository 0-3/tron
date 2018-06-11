import turtle
scr = turtle.Screen()
print("Player 1: Left = a, Right = s")
print("Player 2: Left = Left, Right = Right")
print("Player 3: Left = ,, Right = .")
print("Player 4: Left = 4, Right = 6")
stPlayers = input("Number of players: ")
intPlayers = int(stPlayers)
global alive
alive = []

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
    t.setheading(90)
    t.color("red")
    t.goto(1, 0)
    t.st()
def t2(t):
    #Define Player 2
    t.setheading(270)
    t.color("blue")
    t.goto(-1, 0)
    t.st()
def t3(t):
    #Define Player 3
    t.setheading(0)
    t.color("green")
    t.goto(0, -1)
    t.st()
def t4(t):
    #Define Player 4
    t.setheading(180)
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
    w.up()
    w.goto(-200 + (p-1)*100, -240)
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

drawBoard()
defTurtle(intPlayers)

def turnUp(t):
    t.setheading(90)
def turnDown(t):
    t.setheading(270)
def turnLeft(t):
    t.setheading(180)
def turnRight(t):
    t.setheading(0)
    
scr.onkey(turnUp(p1), "w")
scr.onkey(turnDown(p1), "s")
scr.onkey(turnLeft(p1), "a")
scr.onkey(turnRight(p1), "d")
scr.onkey(turnUp(p2), "Up")
scr.onkey(turnDown(p2), "Down")
scr.onkey(turnLeft(p2), "Left")
scr.onkey(turnRight(p2), "Right")
scr.onkey(turnUp(p3), "i")
scr.onkey(turnDown(p3), "k")
scr.onkey(turnLeft(p3), "j")
scr.onkey(turnRight(p3), "l")
scr.onkey(turnUp(p4), "t")
scr.onkey(turnDown(p4), "g")
scr.onkey(turnLeft(p4), "f")
scr.onkey(turnRight(p4), "h")
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

        
scr.bye
print("Player " + str(alive[0]) + " has won the game!")
