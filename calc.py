##imports
import turtle as trtl
import math


##initialization
t = trtl.Turtle()
cover = trtl.Turtle()
wn = trtl.Screen()
global line_list
line_list = []

wn.bgpic('calc.png')
wn.setup(570, 696)
cover.ht()
t.penup()
t.ht()
t.pencolor('white')
t.goto(-250, 150)
startpos = (-250,150)
t.pendown()

#Used to cover 0 when button pressed.
#wn.addshape('cover.gif')
#cover.shape('cover.gif')
cover.speed(0)
cover.penup()
cover.goto(225, 225)
cover.pendown() 
#cover.stamp()

##Operator Function

def write(button):
    t.write(button, font=("Arial", 74, "bold"))
    t.penup()
    t.fd(55)
    t.pendown() 

    
def button_pressed(x, y):
    global button
    if 46 - 55*0 > y > 46 - 55*1:
        if -290 + 115*0 < x < -290 + 115*1:
            button = '1/x'
            
        elif -290 + 115*1 < x < -290 + 115*2:
            button = 'Natural Logarithim'
        elif -290 + 115*2 < x < -290 + 115*3:
            button = 'log'
        elif -290 + 115*3 < x < -290 + 115*4:
            button = 'Clear'
        elif -290 + 115*4 < x < -290 + 115*5:
            button = 'Delete'

    if 46 - 55*1 > y > 46 - 55*2:
        if -290 + 115*0 < x < -290 + 115*1:
            button = 'sin'
        elif -290 + 115*1 < x < -290 + 115*2:
            button = 'cosin'
        elif -290 + 115*2 < x < -290 + 115*3:
            button = 'tan'
        elif -290 + 115*3 < x < -290 + 115*4:
            button = 3.14
        elif -290 + 115*4 < x < -290 + 115*5:
            button = '%' #Modulus
  
    if 46 - 55*2 > y > 46 - 55*3:
        if -290 + 115*0 < x < -290 + 115*1:
            button = '|x|'
        elif -290 + 115*1 < x < -290 + 115*2:
            button = '(' #Open Paranthesis
        elif -290 + 115*2 < x < -290 + 115*3:
            button = ')' #Closed Parenthesis
        elif -290 + 115*3 < x < -290 + 115*4:
            button = '!' #Factorial
        elif -290 + 115*4 < x < -290 + 115*5:
            button = '/' #Division

    if 46 - 55*3 > y > 46 - 55*4:
        if -290 + 115*0 < x < -290 + 115*1:
            button = 'e' #exponent
        elif -290 + 115*1 < x < -290 + 115*2:
            button = 7
        elif -290 + 115*2 < x < -290 + 115*3:
            button = 8
        elif -290 + 115*3 < x < -290 + 115*4:
            button = 9
        elif -290 + 115*4 < x < -290 + 115*5:
            button = '*' #Multiplication

    if 46 - 55*4 > y > 46 - 55*5:
        if -290 + 115*0 < x < -290 + 115*1:
            button = 'x^2' #Ten to the power of x
        elif -290 + 115*1 < x < -290 + 115*2:
            button = 4
        elif -290 + 115*2 < x < -290 + 115*3:
            button = 5
        elif -290 + 115*3 < x < -290 + 115*4:
            button = 6
        elif -290 + 115*4 < x < -290 + 115*5:
            button = '-' #subtraction

    if 46 - 55*5 > y > 46 - 55*6:
        if -290 + 115*0 < x < -290 + 115*1:
            button = '+'
        elif -290 + 115*1 < x < -290 + 115*2:
            button = 1
        elif -290 + 115*2 < x < -290 + 115*3:
            button = 2
        elif -290 + 115*3 < x < -290 + 115*4:
            button = 3
        elif -290 + 115*4 < x < -290 + 115*5:
            button = '+' #Addition
  
    if 46 - 55*6 > y > 46 - 55*7:
        if -290 + 115*0 < x < -290 + 115*1:
            button = 'Natural Logarithm'
        elif -290 + 115*1 < x < -290 + 115*2:
            button = '-' #Negative
        elif -290 + 115*2 < x < -290 + 115*3:
            button = 0
        elif -290 + 115*3 < x < -290 + 115*4:
            button = '.' #Decimal
        elif -290 + 115*4 < x < -290 + 115*5:
            button = '=' #Equal
            
    try:
        if t.xcor() <= 140:
          if button == 'Clear':
            line_list.clear()
            t.clear()
            t.pu()
            t.goto(startpos)
            t.pd()

          else:
            if button != '':
              #print(line_list)
              line_list.append(str(button))
              write(button)
            button = ''
        else:
          button = '='
          line_list.append(button)
          write(button)
  
    except NameError:
        print('')
    for char in line_list:
        if char == '=':
            line_list.pop()
            sum = eval(''.join(line_list))
            print(sum)
            t.clear()
            write(sum)


wn.onclick(button_pressed)
wn.mainloop()
