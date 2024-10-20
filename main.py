import turtle
turtle.Screen().bgcolor("Aqua")
board = turtle.Turtle()
board.forward(100)
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)
board.penup()
board.right(150)
board.forward(50)
board.pendown()
board.right(90)
board.forward(100)
board.right(120)
board.forward(100)
board.right(120)
board.forward(100)
size = 0
while True:
    for i in range(4):
        board.fd(size + 1)
        board.left(90)
        size = size - 5
    size = size + 1
turtle.done