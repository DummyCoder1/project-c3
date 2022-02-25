import turtle
turtle.speed(0)
length = 10#Initialize the length variable

while length <= 80 :#Write the condition
    for i in range(10):
        turtle.pencolor("red")
        #Write the line for pen color
        turtle.forward(length)
        #Write the line for moving the turtle forward by passing length as a variable
        turtle.right(89)
        length += 0.5
        #write the break statement to exit this for loop
        break
    #Write the line for pen color
    turtle.pencolor("green")
    turtle.forward(length)
    #Write the line for moving the turtle forward by passing length as a variable
    turtle.right(89)
    length += 0.5
