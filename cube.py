import turtle
import math

screen = turtle.Screen()
screen.title = "3D Cube using Python Turtle"
screen.setup(width=1000, height=1000)
screen.tracer(0)

cube = turtle.Turtle()
cube.hideturtle()
cube.penup()

rotation_x = 0
rotation_y = 0
zoom = 7

def coords (x, y, z):
  return cylind(math.atan2(y, x), math.sqrt(x*x+y*y), z)
    
def cylind (deg, r, h):
  global rotation_x
  global rotation_y
  
  return ((zoom/(zoom-int(findz(deg, r, h))))*r*math.cos(rotation_y+deg))*100, ((zoom/(zoom-int(findz(deg, r,h))))*(r*math.sin(rotation_x)*math.sin(rotation_y + deg)+h*math.cos(rotation_x)))*100
        
def findz(deg, r, h):
  global rotation_x
  global rotation_y
    
  return math.cos(rotation_x)*r*math.sin(rotation_y+deg)-math.sin(rotation_x)*h

while (True):
  cube.goto(coords(1, 1, 1))
  cube.pendown()
  cube.goto(coords(1, -1, 1))
  cube.goto(coords(-1, -1, 1))
  cube.goto(coords(-1, 1, 1))
  cube.goto(coords(1, 1, 1))
  cube.penup()

  turtle.mainloop()
