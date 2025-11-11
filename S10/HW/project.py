import turtle
import time
import math
import random

dt = 0.01

def make_ajor1():
    turtle.color("black")
    turtle.begin_fill()
    for i in range(2):
        turtle.fd(50)
        turtle.right(90)
        turtle.fd(10)
        turtle.right(90)
    turtle.end_fill()

def make_ajor2():
    turtle.color("black")
    turtle.begin_fill()
    for i in range(2):
        turtle.fd(10)
        turtle.right(90)
        turtle.fd(50)
        turtle.right(90)
    turtle.end_fill()
    

turtle.tracer(0)
  

def make_box():
    x = -300
    y = 300
    
    for i in range(10):
        turtle.penup()
        turtle.setpos(x,y)
        turtle.pendown()
        make_ajor1()
        x = x + 60
    
    x = -300
    y = -300
    for i in range(10):
        turtle.penup()
        turtle.setpos(x,y)
        turtle.pendown()
        make_ajor1()
        x = x +60


    x = -300
    y = 300

    for i in range(10):
        turtle.penup()
        turtle.setpos(x,y)
        turtle.pendown()
        make_ajor2()
        y = y -60

    x = 300
    y = 300

    for i in range(10):
        turtle.penup()
        turtle.setpos(x,y)
        turtle.pendown()
        make_ajor2()
        y = y -60


make_box()



colors = "orange" , "red" , "yellow" , "gray"

def make_ball():
    b = turtle.Turtle()
    b.shape("circle")
    b.pensize(5)
    b.color(random.choice(colors))
    b.penup()

    alpha = random.randint(0,360)
    vb = random.randint(-300,300)
    vx = vb *math.sin(math.radians(alpha))
    vy = vb * math.cos(math.radians(alpha))
    b.vx = vx
    b.vy = vy
    b.hits = 0
    return b



balls =[]

for c in range(100):
    c = make_ball()
    balls.append(c)


def move(b):
    x,y = b.pos()
    x = x + b.vx*dt
    y = y + b.vy*dt
    b.setpos(x, y)


divar = 280
def reverse(b):
     
    if x>divar or x<-divar:
        b.hits+=1
        if b.hits<4:
            b.vx=-b.vx
        
    if y>divar or y<-divar:
        b.hits+=1
        if b.hits<4:
            b.vy = -b.vy



 
divar = 280
for b in balls:
    b.hits = 0
while True:

    for b in balls:
        
        move(b)
        x,y = b.pos() 
        reverse(b)
            
        
    turtle.update()
    time.sleep(dt)

    




    
        
    


    















turtle.mainloop()