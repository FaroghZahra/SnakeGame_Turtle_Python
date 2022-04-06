from turtle import *
from random import *
from time import *

#setting screen
win = Screen()
win.title("My Snake Game in Turtle")
win.setup(width= 600, height= 600)
win.bgcolor("purple")
win.tracer(0)

#head
head = Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "STOP"

#movements
def move():
    if  head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if  head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if  head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
    if  head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

#directions
def move_up():
    if head.direction != "down":
        head.direction = "up"
def move_down():
    if head.direction != "up":
        head.direction = "down"
def move_left():
    if head.direction != "right":
        head.direction = "left"
def move_right():
    if head.direction != "left":
        head.direction = "right"

#food
food = Turtle()
food.speed(0)
food.color("yellow")
food.shape("circle")
food.shapesize(0.5,0.5)
food.penup()
food.goto(0,100)

#taking input
win.listen()
win.onkey(move_up,"w")
win.onkey(move_down,"s")
win.onkey(move_left,"a")
win.onkey(move_right,"d")

#to handle tails
tails = []

#scores
score = 0
highScore = 0
pen2 = Turtle()
pen2.speed(0)
pen2.color("white")
pen2.hideturtle()
pen2.penup()
pen2.goto(0,260)
pen2.write("Score: {} High Score: {}".format(score, highScore), align="center", font=("Courier", 24, "bold"))

#restarting game
def restart():
    sleep(1)
    head.goto(0,0)
    head.direction = "STOP"
        
    #hiding tails
    for tail in tails:
        tail.goto(1000,1000)
        #clear tails array
    tails.clear()
    pen = Turtle()
    pen.speed(0)
    pen.hideturtle()
    pen.color("black")
    pen.write("restarting", align="center", font=("candara", 24, "bold"))
    pen.color("purple")
    pen2.clear()
    pen2.write("Score: {} High Score: {}".format(score, highScore), align="center", font=("Courier", 24, "bold"))
    sleep(1)
    pen.clear()
    

#main
delay = 0.1
while True:
    win.update()
    
    sleep(delay)
    #collision with border
    if(head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290):
        score = 0
        restart()
    
    #creating distance between food and head
    if head.distance(food) < 15:
        food.goto(randint(-290,290), randint(-290,290))

        #creating new tail
        new_tail = Turtle()
        new_tail.speed(0)
        new_tail.shape("square")
        colors = choice(["red","white","grey","orange"])
        new_tail.color(colors)
        new_tail.penup()
        tails.append(new_tail)
        score = score + 10
        if score > highScore:
            highScore = score
        pen2.clear()
        pen2.write("Score: {} High Score: {}".format(score, highScore), align="center", font=("Courier", 24, "bold"))


    #movinng tails
    for i in range(len(tails)-1,0,-1):
        x = tails[i-1].xcor()
        y = tails[i-1].ycor()
        tails[i].goto(x,y)
    if len(tails) > 0:
        x = head.xcor()
        y = head.ycor()
        tails[0].goto(x,y)
    move()

    #tail head collisions
    for tail in tails:
        if tail.distance(head) < 15:
            score = 0
            restart()