import turtle
import math

screen = turtle.Screen()
screen.title("3D Cube with Perspective Projection")
screen.setup(width=800, height=800)
screen.tracer(0)

cube = turtle.Turtle()
cube.hideturtle()
cube.penup()

rotation_x = 0
rotation_y = 0
up = 0
down = 0
left = 0
right = 0
forward = 0
backward = 0
zoom = 500
distance = 5
rotation_speed = 0.01
move_speed = 0.01

def coords(x, y, z):
    global zoom
    global distance
    global rotation_x
    global rotation_y

    temp_x = x * math.cos(rotation_y) + (y * math.sin(rotation_x) + z * math.cos(rotation_x)) * math.sin(rotation_y)
    temp_y = y * math.cos(rotation_x) - z * math.sin(rotation_x)
    temp_z = -x * math.sin(rotation_y) + (y * math.sin(rotation_x) + z * math.cos(rotation_x)) * math.cos(rotation_y)

    factor = zoom / (-temp_z + distance)

    return temp_x * factor, temp_y * factor

def draw(list, color):
    global cube

    cube.penup()
    cube.goto(list[0])
    cube.pencolor(color)
    cube.pendown()

    for i in range(len(list)):
        cube.goto(list[i])

    cube.goto(list[0])
    cube.penup()

def write(text, x, y, color, center, info):
    global cube

    cube.penup()
    cube.goto(x, y)
    cube.pencolor(color)
    cube.pendown()
    cube.write(text, False, align = center, font = info)
    cube.penup()

def rotate_up():
    global up
    up = 1

def rotate_down():
    global down
    down = -1

def rotate_left():
    global left
    left = 1

def rotate_right():
    global right
    right = -1

def move_forward():
    global forward
    forward =  1

def move_backward():
    global backward
    backward =  -1

def release_up():
    global up
    up = 0

def release_down():
    global down
    down = 0

def release_left():
    global left
    left = 0

def release_right():
    global right
    right = 0

def release_forward():
    global forward
    forward =  0

def release_backward():
    global backward
    backward =  0

screen.onkeypress(rotate_up, "Up")
screen.onkeypress(rotate_down, "Down")
screen.onkeypress(rotate_left, "Left")
screen.onkeypress(rotate_right, "Right")
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")

screen.onkeyrelease(release_up, "Up")
screen.onkeyrelease(release_down, "Down")
screen.onkeyrelease(release_left, "Left")
screen.onkeyrelease(release_right, "Right")
screen.onkeyrelease(release_forward, "w")
screen.onkeyrelease(release_backward, "s")

while True:
    cube.clear()

    front_face = [coords(1, 1, 1), coords(1, -1, 1), coords(-1, -1, 1), coords(-1, 1, 1)]
    back_face = [coords(1, 1, -1), coords(1, -1, -1), coords(-1, -1, -1), coords(-1, 1, -1)]
    top_face = [coords(1, 1, 1), coords(1, 1, -1), coords(-1, 1, -1), coords(-1, 1, 1)]
    bottom_face = [coords(1, -1, 1), coords(1, -1, -1), coords(-1, -1, -1), coords(-1, -1, 1)]

    guide = [coords(0, 0, 1), coords(0, 0, 2)]
    
    draw(front_face, "black")
    draw(back_face, "black")
    draw(top_face, "black")
    draw(bottom_face, "black")

    draw(guide, "red")

    write("Controls:", -380, -310, "black", 'left', ('Verdana', 15, 'normal'))
    write("← → : rotate left and right", -380, -330, "black", 'left', ('Verdana', 15, 'normal'))
    write("↑ ↓ : rotate up and down (along the red line)", -380, -350, "black", 'left', ('Verdana', 15, 'normal'))
    write("W S : move the cube forward and backward", -380, -370, "black", 'left', ('Verdana', 15, 'normal'))

    rotation_x -= (up + down) * rotation_speed
    rotation_y -= (left + right) * rotation_speed
    distance += (forward + backward) * move_speed

    if distance < 2:
        distance = 2

    screen.update()
    screen.listen()
