'''
9. Create a turtle and use a loop to draw a square.
'''

import turtle
screen=turtle.Screen()

s=turtle.Turtle()
for x in range(0,1,1):
    s=turtle.Turtle()
    s.goto(0,0)
    s.shape('square')
    s.shapesize(1,1)

while True:
    screen.update()