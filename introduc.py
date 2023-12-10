import turtle

pen = turtle.Turtle()

pen.speed(500)

for i in range(12):
    pen.forward(30)
    pen.left(30)
    pen.forward(30)
    pen.left(150)
    pen.forward(30)
    pen.left(30)
    pen.forward(30)

for i in range(12):
    pen.home()
    pen.left((i-1)*30)
    pen.forward(30)
    pen.right(30)
    pen.forward(30)
    pen.left(60)
    pen.forward(30)
    pen.left(120)
    pen.forward(30)

pen.home()
    
for i in range(12):
    pen.home()
    pen.left((i-1)*30)
    pen.forward(30)
    pen.left(30)
    pen.forward(30)
    pen.right(60)
    for p in range(4):
        pen.forward(30)
        pen.left(90)

pen.speed(100)

for i in range(12):
    pen.penup()
    pen.home()
    pen.pendown()
    pen.left((i-1)*30)
    pen.forward(30)
    pen.left(30)
    pen.forward(30)
    pen.right(60)
    pen.forward(30)
    pen.left(90)  
    pen.forward(30) #koniec cesty
    pen.left(30)
    pen.forward(30)
    pen.left(60)
    pen.forward(30)
    pen.left(30)


for i in range(12):
    pen.penup()
    pen.home()
    pen.pendown()
    pen.left((i-1)*30)
    pen.forward(30)
    pen.left(30)
    pen.forward(30)
    pen.right(60)
    pen.forward(30)
    pen.left(90)  
    pen.forward(30) #koniec cesty
    pen.left(30)
    pen.forward(30)
    pen.left(15)
    pen.forward(30)
    pen.left(60)
    pen.forward(30)
    
    
    



turtle.done()

print()