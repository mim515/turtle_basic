import turtle

# Create a turtle screen and pen
screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.speed(2)
pen.pensize(3)

# Draw the letter S
pen.penup()
pen.goto(-50, 50)  # Starting position
pen.pendown()

# Top curve
pen.setheading(180)  # Face left
pen.circle(25, 180)  # Draw top half circle

# Middle section
pen.circle(-25, 180)  # Draw middle curve

# Bottom curve
pen.circle(25, 180)  # Draw bottom half circle

# Hide turtle and keep window open
pen.hideturtle()
screen.mainloop()
