import turtle

# Create the screen and set properties
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Concentric Circles with Gaps")

# Create the turtle object
ring = turtle.Turtle()
ring.color("white")  # Set the color for the circles

# Define list of colors for concentric circles
colors = ["green", "yellow", "red", "blue"]  # You can add/remove colors

# Set loop parameters for customization
num_circles = 5  # Number of concentric circles
start_radius = 50  # Radius of the innermost circle
gap = 10  # Gap between circles

# Draw the concentric circles
for i in range(num_circles):
    ring.penup()
    ring.goto(0, 0)
    ring.pendown()
    ring.color(colors[i % len(colors)])
    ring.circle(start_radius + i * (gap + start_radius))

screen.exitonclick()

