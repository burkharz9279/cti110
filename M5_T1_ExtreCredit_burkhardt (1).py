#CTI 110
#M5 T1 (Extra Credit)
#Zachary Burkhardt
#10/25/17

def main():

    import turtle
    win = turtle.Screen()
    t = turtle.Turtle()
    win.bgcolor ("blue")
    t.penup()
    t.goto(-200, 0)
    t.pendown()

    #Display options
    t.pensize(3)
    t.pencolor("white")
    t.shape("arrow")

    #Draw snowflake
    for i in range(10):
        t.forward(150)
        t.right(100)
        t.forward(150)
        t.right(200)

    t.penup()
    t.right(50)
    t.forward(75)
    t.left(50)
    t.pendown()

    for i in range (10):
        t.forward(150)
        t.right(100)
        t.forward(150)
        t.right(200)

    t.penup()
    t.right(50)
    t.forward(75)
    t.left(50)
    t.pendown()

    for i in range (10):
        t.forward(150)
        t.right(100)
        t.forward(150)
        t.right(200)
        
main()
