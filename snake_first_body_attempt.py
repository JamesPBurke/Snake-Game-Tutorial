import turtle
import time
import random

# game board setup

def drawBorders(size):
  turtle.speed(0)
  turtle.penup()
  turtle.goto(-size/2,size/2)
  turtle.pendown()
  turtle.forward(size)
  turtle.right(90)  
  turtle.forward(size)
  turtle.right(90)  
  turtle.forward(size)
  turtle.right(90)
  turtle.forward(size)
  turtle.penup()
  turtle.goto(0,0)
  turtle.pendown()
  turtle.hideturtle()

# responses to user input

def go_left():
  if (head.behave != "right"):
    head.behave = "left"
    print("going left")

def go_right():
  if (head.behave != "left"):
    head.behave = "right"
    print("going right")

def go_up():
  if (head.behave != "down"):
    head.behave = "up"
    print("going up")

def go_down():
  if (head.behave != "up"):
    head.behave = "down"
    print("going down")

#
# sprite behaviors
#


def move_snake():
  if (head.behave == "up"):
    head.setheading(90)
  elif (head.behave == "down"):
    head.setheading(270)
  elif (head.behave == "left"):
    head.setheading(180)
  elif (head.behave == "right"):
    head.setheading(0)
  if (head.behave != "stationary"):
    head.forward(20)
  for i in range(len(snake_body)-1,0,-1):
    newx = snake_body[i-1].xcor()
    newy = snake_body[i-1].ycor()
    snake_body[i].goto(int(newx), int(newy))

    

def grow_snake():
  snake_body.append(snake_body[len(snake_body)-1].clone())
  snake_body[len(snake_body)-1].color("lightgreen")
  print(snake_body)
  for turt in snake_body:
    print(turt.pos())
  


# food behavior

def move_food(size):
  # hide food
  food.hideturtle()
  # change location of food
  # food.goto(50,-100)
  midsize = size * .8
  food.goto(random.randint(-midsize/2,midsize/2), random.randint(-midsize/2,midsize/2))
  # show the food 
  food.showturtle()

# set flag to end loop

def so_done():
  turtle.done = True
  print("stopping")

# Check whether the sprite has hit one of the boundaries
def collision_with_wall(size):
  collided = False
  if head.xcor() >= size/2:
    collided = True
  if head.xcor() <= -size/2:
    collided = True
  if head.ycor() >= size/2:
    collided = True
  if head.ycor() <= -size/2:
    collided = True
  return collided

# function to see if the snake
# head has collided with the food

def snake_ate_food():
  ate = False
  # check if the snake is close
  # enough to the food that
  # we can consider it a collision
  if (head.distance(food)<15):
    ate=True
  return ate

#
#
# Main part of our program
#
#

random.seed()

# set up sprites

head = turtle.Turtle()
head.color("green")
head.speed(0)
head.shape("square")
head.penup()

food = turtle.Turtle()
food.speed(0)
food.color("orange")
food.penup()
food.shape("circle")
food.goto(50,50)

snake_body = []

snake_body.append(head)


# initialize the score
score = 0

area_size = 600

# get a reference to the screen
thescreen = turtle.getscreen()
thescreen.bgcolor("honeydew")
drawBorders(area_size)

# keyboard bidings setup
thescreen.listen()
thescreen.onkey(go_up,"Up")
thescreen.onkey(go_left, "Left")
thescreen.onkey(go_down, "Down")
thescreen.onkey(go_right, "Right")
thescreen.onkey(so_done,"x")

turtle.done = False
head.behave = "stationary"

thescreen.tracer(0)

# The Main Game Loop
while (not turtle.done):

  move_snake()
  
  if collision_with_wall(area_size):
    turtle.done = True
    print("You hit the wall!")

  if snake_ate_food():
    score = score + 1
    print(score)
    move_food(area_size)
    grow_snake()
  time.sleep(0.1)
  thescreen.update()

print("Game over!")
print("Done!")
