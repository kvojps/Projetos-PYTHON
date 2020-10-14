import turtle

cores = ['orange','blue','purple','green','blue','red']

tartaruga = turtle.Pen()
tartaruga.speed(30)
turtle.bgcolor("black")

#Desenhando com Turtle
for x in range(200):
    tartaruga.pencolor(cores[x%6])
    tartaruga.width(x/100 + 1)
    tartaruga.forward(x)
    tartaruga.left(59)

turtle.done()

