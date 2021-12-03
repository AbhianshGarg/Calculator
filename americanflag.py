import turtle as trtl

t = trtl.Turtle()
t.speed(0)

wn = trtl.Screen()
wn.setup(1.0, 1.0)
colors = ['red', 'white']

x = -150
y = -100
def rectangle(x, y, fd, fd2, color):
  t.fillcolor(color)
  t.pu()
  t.goto(x, y)
  t.pd()
  t.begin_fill()
  for i in range(2):
    t.fd(fd)
    t.right(90)
    t.fd(fd2)
    t.right(90)
  t.end_fill()

def star(num):
  for i in range(num):
    for i in range(5):
      t.fd(10)
      t.right(144)
    t.pu()
    t.fd(15)
    t.pd()

for i in range(1, 7):
  rem = i%2
  if rem == 1:
    color = 'red'
  elif rem == 0:
    color = 'white'
  rectangle(x, y, 300, 15, color)
  y+=15
for i in range(1, 8):
  rem = i%2
  if rem == 1:
    color = 'red'
  elif rem == 0:
    color = 'white'
  rectangle(0, y, 150, 15, color)
  y+=15

rectangle(-150, 80, 150, 105, 'blue')

t.pu
t.goto(-135, 94.5)
t.pd
t.fillcolor('white')
t.begin_fill()
for i in range(1, 10):
  rem = i%2
  if rem == 1:
    star(6)
    t.pu()
    t.goto(-135, 94.5 - 10.5*i)
    t.pd
  elif rem == 0:
    star(5)
    t.pu()
    t.goto(-150, 94.5 - 10.5*i)
    t.pd

t.end_fill()
#10.5 Down
#15 Side

wn.mainloop()
