#Q.No54 Draw f(X)=X^2
import turtle
import math
turtle.penup()
turtle.pendown()
turtle.goto(-195,0)
turtle.forward(2*196)
turtle.left(150)
turtle.forward(10)
turtle.penup()
turtle.right(180)
turtle.forward(10)
turtle.right(120)
turtle.pendown()
turtle.forward(10)
turtle.penup()
turtle.home()
turtle.goto(0,-100)
turtle.left(90)
turtle.pendown()
turtle.forward(2*100)
turtle.left(150)
turtle.forward(10)
turtle.penup()
turtle.right(180)
turtle.forward(10)
turtle.right(120)
turtle.pendown()
turtle.forward(10)
turtle.left(120)
turtle.write('Y',font=('New Roman Times',35,'bold'))
turtle.penup()
turtle.home()
for x in range(-6,7):
    turtle.goto(x,math.pow(x,2))
    turtle.pendown()

turtle.done()