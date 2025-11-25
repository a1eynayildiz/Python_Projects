import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light pink")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()

#  Kare çiz
''' for i in range(4):
    turtle_instance.forward(200)# = Kalemi bulunduğu yönde 100 birim ileri götür
    turtle_instance.right(90)#right(90) = Kalemi sağa doğru 90 derece döndür
    turtle.done() # bunu demezsek ekran kapanmaz
'''
#yıldız
'''

for i in range(5):
    turtle_instance.color("brown")
    turtle_instance.forward(200)
    turtle_instance.left(144)

turtle.done()
'''

#iç içe kare çiz
"""def shrinkingSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 5

shrinkingSquare(150)
shrinkingSquare(130)
shrinkingSquare(110)
shrinkingSquare(90)
shrinkingSquare(80)
shrinkingSquare(60)
shrinkingSquare(40)
shrinkingSquare(20)
shrinkingSquare(10)"""


#kalp çiz
turtle_instance.speed(3)
turtle_instance.color("red")
turtle_instance.begin_fill()
turtle_instance.left(140)
turtle_instance.forward(200)
turtle_instance.circle(-100,200) #yarıçap ve derece
turtle_instance.left(120)
turtle_instance.circle(-100,200)
turtle_instance.forward(200)
turtle_instance.end_fill()

turtle.done()

