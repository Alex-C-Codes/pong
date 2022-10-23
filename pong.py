# Import required library
import turtle

screen_height = 600
max_y_from_center = screen_height/2
screen_width = 1000
paddle_speed = 10


# Moves paddle paddle_speed * pixels in direction set via setheading()
def move_left_paddle_up():
    if left_pad.ycor() <= max_y_from_center:
        left_pad.forward(paddle_speed)


# Moves paddle paddle_speed * pixels opposite to direction set via setheading()
def move_left_paddle_down():
    if left_pad.ycor() >= -1 * max_y_from_center:
        left_pad.backward(paddle_speed)


def move_right_paddle_up():
    if right_pad.ycor() <= max_y_from_center:
        right_pad.forward(paddle_speed)


def move_right_paddle_down():
    if right_pad.ycor() >= -1 * max_y_from_center:
        right_pad.backward(paddle_speed)


# Create screen
sc = turtle.Screen()
sc.title("Pong")
sc.bgcolor("black")
sc.setup(width=screen_width, height=screen_height)
# turtle.Screen().exitonclick()

# Create left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("white")
left_pad.shapesize(stretch_wid=2, stretch_len=6)
left_pad.penup()
left_pad.goto(-400, 0)
left_pad.setheading(90)

# Create right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("white")
right_pad.shapesize(stretch_wid=2, stretch_len=6)
right_pad.penup()
right_pad.goto(400, 0)
right_pad.setheading(90)

# Create pong ball
pong = turtle.Turtle()
pong.speed(0)
pong.shape("circle")
pong.color("white")
pong.shapesize(stretch_wid=3)
pong.penup()
pong.goto(0, 0)

sc.listen()

# Create score

# Create ball movement

# Create paddle movement

sc.onkeypress(move_right_paddle_up, "Up")
sc.onkeypress(move_right_paddle_down, "Down")
sc.onkeypress(move_left_paddle_up, "w")
sc.onkeypress(move_left_paddle_down, "s")

sc.mainloop()

input('Press ENTER to exit')
