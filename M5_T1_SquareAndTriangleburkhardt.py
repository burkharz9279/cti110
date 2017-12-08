#CTI 110
#M5 T1 - Turtle Lab
#Zachary Burkhardt
#10/11/17

def main():

    import turtle
    win = turtle.Screen()
    t = turtle.Turtle()
    t.penup()
    t.goto(-250, -75)
    t.pendown()

    #Display options
    t.pensize(5)
    t.pencolor("green")
    t.shape("turtle")

    #Draw the square
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)

    #Draw the triangle
    t.penup()
    t.forward(500)
    t.pendown()
    t.left(120)
    t.forward(225)
    t.left(120)
    t.forward(225)
    t.left(120)
    t.forward(225)

main()
