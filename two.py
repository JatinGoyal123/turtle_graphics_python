# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

# import turtle
# turtle.right(25)
# turtle.done()

from turtle import *
t=Turtle()
t.shape("turtle")
wn=Screen()
wn.title('Turtle Graphics')
# help('turtle.shape')
# wn.bgcolor('yellow')
wn.bgpic('test.gif')
t.color('red','green')#pencolor,fillcolor
t.speed(3)
t.hideturtle()
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
t.penup()
t.forward(200)
t.pendown()

for i in range(4):
    t.forward(100)
    t.left(90)

t.end_fill()
done()