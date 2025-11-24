import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("spiral helix")

turtle_instance = turtle.Turtle()
turtle_instance.color("deep pink")

turtle_colors = ["deep pink","red", "green", "brown", "purple", "orange" ,"yellow"]

for i in range(10):
 turtle_instance.color(turtle_colors[i%6])
 turtle_instance.circle(10 * i)
 turtle_instance.circle(-10 * i)
 turtle_instance.left(i)

turtle.done()

