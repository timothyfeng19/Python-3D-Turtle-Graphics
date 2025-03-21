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

# def side(list):
#  global cube
  
#  cube.penup()
#  cube.goto(coords(list[0]))
#  cube.pendown()
  
#  for i in range(len(list)-1):
#    cube.goto(coords(list[i+1]))
#  cube.goto(coords(list[0]))
    
#  cube.penup()

while (True):
  cube.penup()
  cube.goto(coords(1, 1, 1))
  cube.pendown()
  cube.goto(coords(1, -1, 1))
  cube.goto(coords(-1, -1, 1))
  cube.goto(coords(-1, 1, 1))
  cube.goto(coords(1, 1, 1))
  cube.penup()

  cube.penup()
  cube.goto(coords(1, 1, -1))
  cube.pendown()
  cube.goto(coords(1, -1, -1))
  cube.goto(coords(-1, -1, -1))
  cube.goto(coords(-1, 1, -1))
  cube.goto(coords(1, 1, -1))
  cube.penup()

  screen.listen()
  turtle.mainloop()
