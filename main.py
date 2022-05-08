import turtle

t = turtle.Turtle()

for star in ['red']:
  t.color(star)
  for star in range(0,5):
    t.forward(110)
    t.left(216)

for square in ['green']:
  t.color(square)
  for square in range(0,4):
    t.forward(110)
    t.left(90)

for hexagon in ['blue']:
  t.color(hexagon)
  for hexagon in range(0,6):
    t.forward(50)
    t.right(60)