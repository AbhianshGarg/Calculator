##imports
import turtle as trtl
import math

##initialization
t = trtl.Turtle()
wn = trtl.Screen()
operation_list = ['+', '-', '*', '/']

wn.bgpic('calc.png')
wn.setup(1.0, 1.0)


##Operator Function

def button_pressed(x, y):
  print(x, y)
   
  if 46 - 55*0 > y > 46 - 55*1:
    print(x,y)
    if -290 + 115*0 < x < -290 + 115*1:
      button = 'Second'
    elif -290 + 115*1 < x < -290 + 115*2:
      button = 3.14
    elif -290 + 115*2 > x > -290 + 115*3:
      button = 'Eulers'
    elif -290 + 115*3 > x > -290 + 115*4:
      button = 'Cancel'
    elif -290 + 115*4 > x > -290 + 115*5:
      button = 'Delete'
  else:
    print('No Button on this row.')

  if 46 - 55*1 > y > 46 - 55*2:
    if -290 + 115*0 > x > -290 + 115*1:
      button = 'Square'
    elif -290 + 115*1 > x > -290 + 115*2:
      button = '1/x'
    elif -290 + 115*2 > x > -290 + 115*3:
      button = 'Absolute Value'
    elif -290 + 115*3 > x > -290 + 115*4:
      button = 'second'
    elif -290 + 115*4 > x > -290 + 115*5:
      button = 'Modulus'
  else:
    print('No Button on this row.')
  
  if 46 - 55*2 > y > 46 - 55*3:
    if -290 + 115*0 > x > -290 + 115*1:
      button = 'Square Root'
    elif -290 + 115*1 > x > -290 + 115*2:
      button = 'Open Paranthesis'
    elif -290 + 115*2 > x > -290 + 115*3:
      button = 'Closed Parenthesis'
    elif -290 + 115*3 > x > -290 + 115*4:
      button = 'Factorial'
    elif -290 + 115*4 > x > -290 + 115*5:
      button = 'Division'
  else:
    print('No Button on this row.')

  if 46 - 55*3 > y > 46 - 55*4:
    if -290 + 115*0 > x > -290 + 115*1:
      button = 'Exponent'
    elif -290 + 115*1 > x > -290 + 115*2:
      button = 7
    elif -290 + 115*2 > x > -290 + 115*3:
      button = 8
    elif -290 + 115*3 > x > -290 + 115*4:
      button = 9
    elif -290 + 115*4 > x > -290 + 115*5:
      button = 'Multiplication'
  else:
    print('No Button on this row.')
  
  if 46 - 55*4 > y > 46 - 55*5:
    if -290 + 115*0 > x > -290 + 115*1:
      button = 'Ten Power'
    elif -290 + 115*1 > x > -290 + 115*2:
      button = 4
    elif -290 + 115*2 > x > -290 + 115*3:
      button = 5
    elif -290 + 115*3 > x > -290 + 115*4:
      button = 6
    elif -290 + 115*4 > x > -290 + 115*5:
      button = 'Subtraction'
  else:
    print('No Button on this row.')
  
  if 46 - 55*5 > y > 46 - 55*6:
    if -290 + 115*0 > x > -290 + 115*1:
      button = 'Logarithm'
    elif -290 + 115*1 > x > -290 + 115*2:
      button = 1
    elif -290 + 115*2 > x > -290 + 115*3:
      button = 2
    elif -290 + 115*3 > x > -290 + 115*4:
      button = 3
    elif -290 + 115*4 > x > -290 + 115*5:
      button = 'Addition'
  else:
    print('No Button on this row.')
  
  if 46 - 55*6 > y > 46 - 55*7:
    if -290 + 115*0 > x > -290 + 115*1:
      button = 'Natural Logarithm'
    elif -290 + 115*1 > x > -290 + 115*2:
      button = '+/-'
    elif -290 + 115*2 > x > -290 + 115*3:
      button = 0
    elif -290 + 115*3 > x > -290 + 115*4:
      button = 'Decimal'
    elif -290 + 115*4 > x > -290 + 115*5:
      button = 'Equal'
  else:
    print('No Button on this row.')
    
  print(button)





  





##Find operation
'''
num_one = str(num_one)
for char in operation_list:
    try:
        result = num_one.find(char)
        if result >= 0:
            num_one = num_one.split(char)
            num_one[1] = char
    except AttributeError:
        break
'''
wn.onclick(button_pressed)

wn.mainloop()
