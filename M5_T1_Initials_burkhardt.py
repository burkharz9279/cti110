#CTI 110
#M5 T1 - Turtle Graphics
#Zachary Burkhardt
#10/11/17

def main():

    import turtle
    win = turtle.Screen()
    t = turtle.Turtle()
    t.penup()
    t.goto(-300, 100)
    t.pendown()

    #Display options
    t.pensize(10)
    t.pencolor("red")
    t.shape("turtle")

    #Draw "Z"
    t.forward(100)
    t.right(130)
    t.forward(150)
    t.left(130)
    t.forward(100)

    #Draw "T"
    t.penup()
    t.goto(-50, 100)
    t.pendown()
    t.forward(100)
    t.backward(50)
    t.right(90)
    t.forward(120)

    #Draw "B"
    t.penup()
    t.goto(200, 100)
    t.pendown()
    t.forward(120)
    t.left(90)
    t.forward(50)
    t.left(30)
    t.forward(17)
    t.left(30)
    t.forward(17)
    t.left(30)
    t.forward(17)
    t.left(30)
    t.forward(17)
    t.left(30)
    t.forward(17)
    t.left(30)
    t.forward(50)
    t.right(180)
    t.forward(50)
    t.left(30)
    t.forward(17)
    t.left(30)
    t.forward(17)
    t.left(30)
    t.forward(17)
    t.left(30)
    t.forward(17)
    t.left(30)
    t.forward(17)
    t.left(30)
    t.forward(50)

main()
