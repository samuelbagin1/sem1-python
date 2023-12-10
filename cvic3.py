import turtle
import math
bob = turtle.Turtle()

def square(t, length):
    for _ in range(4):
        t.forward(length)
        t.right(90)

square(bob,100)
bob.reset()

def polygon(t, n):
    for _ in range(n):
        t.forward(100)
        t.right(360/n)

polygon(bob, 8)
bob.reset()

def circle(t, r):
  # Calculate the number of sides and the length of each side.
  n = int(2 * math.pi * r / 4)  # 4 is an arbitrary constant that affects the smoothness of the circle.
  side_length = 2 * r * math.sin(math.pi / n)

  # Draw the circle.
  for _ in range(n):
    t.forward(side_length)
    t.left(360 / n)

circle(bob, 20)

bob.reset()
def arc(t, r, angle):
  """Draws an approximate arc with the given turtle, radius, and angle."""

  # Calculate the number of sides and the length of each side.
  n = int(angle * 2 * math.pi * r / 360 / 4)  # 4 is an arbitrary constant that affects the smoothness of the arc.
  side_length = 2 * r * math.sin(math.pi / n)

  # Draw the arc.
  for _ in range(n):
    t.forward(side_length)
    t.left(angle / n)

arc(bob, 20, 270)

   

turtle.done()
print()