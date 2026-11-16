import turtle
import random
bob=turtle.Turtle()
turtle.colormode(255)
screen=turtle.Screen()
screen.bgcolor("sky blue")
def circle():
    for times in range(10):
        c=random.randint(10,20)
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        bob.fillcolor(r,g,b)
        bob.begin_fill()
        bob.circle(c)
        bob.end_fill()
        jump(times*25,times*10)
        
        


def polygon(sides, dist):
  angle = 360/sides
  bob.begin_fill()
  for times in range(sides):        
    bob.forward(dist)
    bob.left(angle)
  bob.end_fill()

def jump(x,y):
  bob.penup()
  bob.goto(x,y)
  bob.pendown()
  
def comet(c, distance, angle):
  bob.color(c)
  for times in range(10):
    bob.pensize(times)
    bob.forward(distance)
    bob.left(angle)
    
def rainbow(x,y):
  jump(x,y)
  bob.width(20)
  bob.color("red")
  bob.left(90)
  bob.circle(-60, 180)
  # circle with neg radius = clockwise
  # circle with 2nd value = arc (180 is semi-circle)
  
  jump(x,y)
  bob.setheading(0) # sets turtle direction
  bob.penup()  
  bob.forward(10)
  bob.pendown()
  bob.left(90)
  bob.color("orange")  
  bob.circle(-50, 180)
  
  jump(x,y)
  bob.setheading(0)
  bob.penup()
  bob.forward(20)
  bob.pendown()
  bob.left(90)
  bob.color("yellow")
  bob.circle(-40, 180)


# start here

circle()
