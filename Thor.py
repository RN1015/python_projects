import turtle

t = turtle.Turtle()

screen = turtle.Screen()
screen.bgcolor('snow')

def ankur(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)
    t.pensize(5)
    t.speed(10)

def golo(r, color):
    x_point = 0
    y_pont = -r
    ankur(x_point, y_pont)
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

turtle.title('THOR, THE GOD OF THUNDER')

golo(250, 'gray')

t.color('black')
turtle.hideturtle()
t.pensize(5)
t.speed(2)
t.penup()
t.goto(-100, 120)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.forward(80)
t.left(70)
t.forward(10)
t.right(70)
t.forward(40)
t.right(70)
t.forward(10)
t.left(70)
t.forward(80)
t.right(45)
t.forward(20)
t.right(45)
t.forward(120)
t.right(45)
t.forward(20)
t.right(45)
t.forward(207)
t.right(45)
t.forward(20)
t.right(45)
t.forward(120)
t.right(45)
t.forward(20)
t.right(45)
t.end_fill()

t.color('gray')
turtle.hideturtle()
t.pensize(5)
t.speed(2)
t.penup()
t.goto(100, 120)
t.pendown()
t.right(90)
t.goto(100, -37)

t.color('gray')
turtle.hideturtle()
t.pensize(5)
t.speed(2)
t.penup()
t.goto(-93, 120)
t.pendown()
t.goto(-93, -37)


t.color('black')
turtle.hideturtle()
t.pensize(5)
t.speed(2)
t.fillcolor('black')
t.begin_fill()
t.penup()
t.goto(-18, -25)
t.pendown()
t.goto(-18, -180)
t.left(60)
t.forward(20)
t.left(30)
t.forward(16.2842712)
t.left(30)
t.forward(20)


t.penup()
t.goto(-18, -180)
t.pendown()
t.goto(33.2842712, -180)


t.penup()
t.goto(33.2842712, -180)
t.pendown()
t.goto(33.2842712, -25)


t.penup()
t.goto(33.2842712, -25)
t.pendown()
t.goto(-18, -25)
t.end_fill()

t.color('gray')
turtle.hideturtle()
t.pensize(5)
t.speed(2)
t.penup()
t.goto(-18, -40)
t.pendown()
t.goto(33.2842712, -55)

t.penup()
t.goto(-18, -70)
t.pendown()
t.goto(33.2842712, -85)

t.penup()
t.goto(-18, -100)
t.pendown()
t.goto(33.2842712, -115)

t.penup()
t.goto(-18, -130)
t.pendown()
t.goto(33.2842712, -145)

t.penup()
t.goto(-18, -160)
t.pendown()
t.goto(33.2842712, -175)

t.penup()
t.goto(25, 10)
t.pendown()
t.circle(35)

t.color('gray')
turtle.hideturtle()
t.pensize(5)
t.speed(2)
t.penup()
t.goto(-20, 0)
t.pendown()
t.goto(20, 80)

t.penup()
t.goto(20, 80)
t.pendown()
t.goto(20, 20)

t.penup()
t.goto(-5, 30)
t.pendown()
t.goto(20, 30)

turtle.done()