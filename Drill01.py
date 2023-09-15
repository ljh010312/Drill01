import turtle

def turtle_move_top():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()
    
def turtle_move_bottom():
    turtle.setheading(-90)
    turtle.forward(50)
    turtle.stamp()
    
def turtle_move_right():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def turtle_move_left():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()

def turtle_quit():
    quit()


turtle.shape('turtle')

turtle.onkey(turtle_move_top, 'w')
turtle.onkey(turtle_move_bottom, 's')
turtle.onkey(turtle_move_right, 'd')
turtle.onkey(turtle_move_left, 'a')
turtle.onkey(restart, 'Escape')
turtle.onkey(turtle_quit, 'q')
turtle.listen()


    
