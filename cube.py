import turtle
import math

zoom = 7
rotation_x = 0
rotation_y = 0

def coords (x, y, z):
  return (cylind(math.atan2(int(y), int(x)), math.sqrt(int(x)^2+int(y)^2), z))
  
def cylind (deg, r, h):
  return ((int(zoom)/(int(zoom)-int(z(deg, r, h))))*int(r)*math.cos(int(rotation_y)+int(deg)),(int(zoom)/(int(zoom)-int(z(deg, r, h))))*(int(r)*math.sin(int(rotation_y)+int(deg))+int(h)*math.cos(int(rotation_x))))
  
