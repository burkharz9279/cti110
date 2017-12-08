#CTI 110
#M5 Lab 2
#Zachary Burkhardt
#10/29/17

def main():
    import turtle
    win = turtle.Screen()
    t = turtle.Turtle()

    #display options
    t.pensize(4)
    t.pencolor("black")
    t.shape("turtle")

    for i in range(10):
        t.forward(100)
        t.right(70)
        for i in range(5):
            t.left(70)

main()
