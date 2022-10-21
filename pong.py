# Import required library
import turtle

# Create screen
sc = turtle.Screen()
sc.title("Pong")
sc.bgcolor("black")
sc.setup(width=1000, height=600)
#turtle.Screen().exitonclick()

# Create left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("white")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)

# Create right paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("white")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(400, 0)

# Create pong ball
pong = turtle.Turtle()
pong.speed(0)
pong.shape("circle")
pong.color("white")
pong.shapesize(stretch_wid=3)
pong.penup()
pong.goto(0, 0)

# Create score

# Create ball movement

# Create paddle movement

input('Press ENTER to exit')