import turtle

t = turtle.Turtle()

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
    t.pensize(20)
    t.circle(r)

point1 = [[(-80, 65), (-110, 70), (-105, 30), (-115, -20), (-70, -70), (-70, -90), (-50, -107.5), (0, -100)],
         [(0, -100), (50, -107.5), (70, -90), (70, -70), (115, -20), (105, 30), (110, 70), (80, 65), (0, 80)]]


turtle.hideturtle()
turtle.bgcolor('white')  # Dark Red
turtle.setup(500, 500)
turtle.title('WAKANDA FOREVER')
point1Goto = (0, 80)
turtle.speed(2)


def logo(a, b):
    turtle.penup()
    turtle.goto(b)
    turtle.pendown()
    turtle.pensize(5)
    turtle.color('black')  # Light Yellow
    turtle.begin_fill()

    for i in range(len(a[0])):
        x, y = a[0][i]
        turtle.goto(x, y)

    for i in range(len(a[1])):
        x, y = a[1][i]
        turtle.goto(x, y)
    turtle.end_fill()

golo(150, 'black')
logo(point1, point1Goto)
turtle.hideturtle()
t.pensize(5)
t.pencolor('white')
t.speed(2)
t.penup()
t.goto(-77, -70)
t.pendown()
t.goto(-50, -96)
t.goto(-50, -107.5)


t.penup()
t.goto(77, -70)
t.pendown()
t.goto(50, -96)
t.goto(50, -107.5)

t.penup()
t.goto(-80, 65)
t.pendown()
t.goto(-77, 40)
t.goto(-20, 5)
t.goto(-20, -10)


t.penup()
t.goto(80, 65)
t.pendown()
t.goto(77, 40)
t.goto(20, 5)
t.goto(20, -10)

t.penup()
t.goto(-100, -10)
t.pendown()
t.goto(-40, -50)

t.penup()
t.goto(100, -10)
t.pendown()
t.goto(40, -50)


t.penup()
t.goto(-40, -50)
t.pendown()
t.goto(-30, -85)

t.penup()
t.goto(40, -50)
t.pendown()
t.goto(30, -85)

t.penup()
t.goto(-30, -85)
t.pendown()
t.goto(0, -80)

t.penup()
t.goto(30, -85)
t.pendown()
t.goto(0, -80)


t.pensize(2)
t.pencolor('white')
t.speed(2)
t.fillcolor('white')
t.begin_fill()
t.penup()
t.goto(-85, -10)
t.pendown()
t.goto(-60, 0)

t.penup()
t.goto(-60, 0)
t.pendown()
t.goto(-20, -15)

t.penup()
t.goto(-20, -15)
t.pendown()
t.goto(-50, -30)

t.penup()
t.goto(-50, -30)
t.pendown()
t.goto(-85, -10)
t.end_fill()


t.fillcolor('white')
t.begin_fill()
t.penup()
t.goto(85, -10)
t.pendown()
t.goto(60, 0)

t.penup()
t.goto(60, 0)
t.pendown()
t.goto(20, -15)

t.penup()
t.goto(20, -15)
t.pendown()
t.goto(50, -30)

t.penup()
t.goto(50, -30)
t.pendown()
t.goto(85, -10)
t.end_fill()


t.pensize(5)
t.pencolor('white')
t.speed(2)
t.penup()
t.goto(-100, -10)
t.pendown()
t.goto(-62.5, 5)

t.penup()
t.goto(-62.5, 5)
t.pendown()
t.goto(-20, -10)

t.penup()
t.goto(100, -10)
t.pendown()
t.goto(62.5, 5)

t.penup()
t.goto(62.5, 5)
t.pendown()
t.goto(20, -10)

t.penup()
t.goto(200, 200)

turtle.done()