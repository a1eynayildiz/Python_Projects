import turtle
import random


screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("catch the turtle !!!")
FONT=("Courier", 16, "bold")
game_over =False
#FONT yerine font da yazabilirdik ama FONT yazmamızın bir anlamı var, sabit hiç değiştirmeyeceğimiz gibi bir anlamı var.
score = 0
#turtle list
turtle_list = []


colors = ["red", "blue", "green", "purple", "yellow", "orange", "pink", "white", "gold"]
fw = turtle.Turtle()
fw.hideturtle()
fw.speed(0)
fw.width(3)

#score turtle
score_turtle = turtle.Turtle()

#countdown turtle
count_down_turtle = turtle.Turtle()

def setup_score_turtle():
 score_turtle.hideturtle()
 score_turtle.color("deeppink")
 score_turtle.penup()

 top_height = screen.window_height()/2
 y = top_height*0.9
 score_turtle.setposition(0, y)
 score_turtle.write("Score:0", move=False, align="center", font=FONT)

#make turtle
gridsize = 15
def make_turtle(x,y):
    t=turtle.Turtle()

    def handle_click(x,y):
        global score
        print(x,y)
        score += 1
        score_turtle.clear()
        score_turtle.write("Score:{}".format(score), move=False, align="center", font=FONT)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2) #kaç ile çarptığını yazıyorsun parametrede
    t.color("green")
    t.goto(x * gridsize,y * gridsize)
    t.pendown()
    turtle_list.append(t)

x_coordinates = [-20,-10,0,10,20]
y_coordinates = [20,10,0,-10]

def setup_turtles():
 for x in x_coordinates:
    for y in y_coordinates:
        make_turtle(x,y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)

def countdown(time):
    global game_over
    top_height = screen.window_height() / 2
    y = top_height - top_height / 10
    count_down_turtle.hideturtle()
    count_down_turtle.penup()
    count_down_turtle.setposition(0, y - 30)
    count_down_turtle.clear()

    if time > 0:
        count_down_turtle.clear()
        count_down_turtle.write("Time: {}".format(time),move=False,align="center",font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        count_down_turtle.clear()
        hide_turtles()
        count_down_turtle.write("Game Over!", align='center', font=FONT)
        start_fireworks()

def start_game_up():
    global game_over
    game_over = False
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    turtle.tracer(1)
    screen.ontimer(lambda: countdown(10), 10)


def start_fireworks():
    if game_over:

        x = random.randint(-screen.window_width() // 2, screen.window_width() // 2)
        y = random.randint(-screen.window_height() // 2, screen.window_height() // 2)

        fw.penup()
        fw.goto(x, y)
        fw.pendown()

        fw.color(random.choice(colors))
        size = random.randint(50, 120)


        turtle.tracer(0)


        for i in range(12):
            fw.forward(size)
            fw.backward(size)
            fw.right(30)

        screen.update()
        turtle.tracer(1)
        screen.ontimer(start_fireworks, 200)
start_game_up()

turtle.mainloop()
