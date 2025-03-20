import turtle as cube
import math

cube.title = "3D Cube using Python Turtle"
cube.setup(width=1000, height=1000)
cube.hideturtle()
cube.penup()
cube.tracer(0)

rotation_x = 0
rotation_y = 0
zoom = 7

def coords (x, y, z):
  return cylind(math.atan2(y, x), math.sqrt(x^2+y^2), z)
    
def cylind (deg, r, h):
  global rotation_x
  global rotation_y
  
  if (zoom-int(findz(deg, r, h)) > 0):
    return (zoom/(zoom-int(findz(deg, r, h))))*r*math.cos(rotation_y+deg), (zoom/(zoom-int(findz(deg, r,h))))*(r*math.sin(rotation_x)*math.sin(rotation_y + deg)+h*math.cos(rotation_x))
  else:   
    return False
        
def findz(deg, r, h):
  global rotation_x
  global rotation_y
    
  return math.cos(rotation_x)*r*math.sin(rotation_y+deg)-math.sin(rotation_x)*h

while (True):
  cube.update()
  cube.exitonclick()
