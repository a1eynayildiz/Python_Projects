import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("deeppink")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()

# Kare çiz
"""for i in range(4):
    turtle_instance.forward(200)# = Kalemi bulunduğu yönde 100 birim ileri götür
    turtle_instance.right(90)#right(90) = Kalemi sağa doğru 90 derece döndür
"""
#yıldız
import turtle

turtle_instance = turtle.Turtle()

for i in range(5):
    turtle_instance.forward(200)
    turtle_instance.left(144)

turtle.done()


turtle.done() # bunu demezsek ekran kapanmaz


