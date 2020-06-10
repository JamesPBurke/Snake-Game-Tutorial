import turtle
import random
import time

# game board setup

def drawBorders():
  turtle.speed(0)
  turtle.penup()
  turtle.goto(-200,200)
  turtle.pendown()
  turtle.forward(400)
  turtle.right(90)  
  turtle.forward(400)
  turtle.right(90)  
  turtle.forward(400)
  turtle.right(90)
  turtle.forward(400)
  turtle.penup()
  turtle.goto(0,0)
  turtle.pendown()
  turtle.hideturtle()

# responses to user input

def go_left():
  if (head.behave != "right"):
    head.behave = "left"
    #print("going left")

def go_right():
  if (head.behave != "left"):
    head.behave = "right"
    #print("going right")

def go_up():
  if (head.behave != "down"):
    head.behave = "up"
    #print("going up")

def go_down():
  if (head.behave != "up"):
    head.behave = "down"
    #print("going down")

#
# sprite behaviors
#

# food behavior

def move_food():
  # hide food
  food.hideturtle()
  # change location of food
  randx = random.randint(-180,180)
  randy = random.randint(-180,180)
  food.goto(randx,randy)
  # show the food 
  food.showturtle()

# snake head behaviors

def step_right():
  head.setheading(0)
  head.forward(20)

def step_up():
  head.setheading(90)
  head.forward(20)

def step_down():
  head.setheading(270)
  head.forward(20)

def step_left():
  head.setheading(180)
  head.forward(20)

# set flag to end loop

def so_done():
  turtle.done = True
  print("stopping")

# Check whether the sprite has hit one of the boundaries
def collision_with_wall():
  collided = False
  if head.xcor() >= 200:
    collided = True
  if head.xcor() <= -200:
    collided = True
  if head.ycor() >= 200:
    collided = True
  if head.ycor() <= -200:
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

def grow_tail():
  new_segment = head.clone()
  new_segment.color("lightgreen")
  tail.insert(0,new_segment)

def move_tail():
  for i in range(len(tail)-1,-1,-1):
    if (i==0):
      tail[i].goto(head.xcor(),head.ycor())
    else:
      tail[i].goto(tail[i-1].xcor(),tail[i-1].ycor())


#
#
# Main part of our program
#
#

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

# initialize the score
score = 0

# get a reference to the screen
thescreen = turtle.getscreen()
thescreen.bgcolor("honeydew")
drawBorders()

# keyboard bidings setup
thescreen.listen()
thescreen.onkey(go_up,"Up")
thescreen.onkey(go_left, "Left")
thescreen.onkey(go_down, "Down")
thescreen.onkey(go_right, "Right")
thescreen.onkey(so_done,"x")

turtle.done = False
head.behave = "stopped"

thescreen.tracer(0)

tail = []

# The Main Game Loop
while (not turtle.done):

  if snake_ate_food():
    score = score + 1
    #print(score)
    move_food()
    grow_tail()
  else:
    move_tail()

  if (head.behave == "up"):
    step_up()

  if (head.behave == "down"):
    step_down()

  if (head.behave == "left"):
    step_left()

  if (head.behave == "right"):
    step_right()
  
  if collision_with_wall():
    turtle.done = True
    print("You hit the wall!")

  
  time.sleep(0.1)
  thescreen.update()

print("Game over!")
print("Done!")
