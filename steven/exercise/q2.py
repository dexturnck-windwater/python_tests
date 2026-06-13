#2. Create a turtle and use a loop to move it forward 50 pixels, 8 times.
import turtle

s=turtle.Screen()

t=turtle.Turtle()
t.goto(0,0)
t.shape('square')

for x in range(1,8,1):
    t.forward(50)
    
while True:
    s.update()

