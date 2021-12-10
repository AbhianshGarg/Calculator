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
t.goto(195, 150)
t.pendown()

#Used to cover 0
wn.addshape('cover.gif')
cover.shape('cover.gif')
cover.speed(0)
cover.penup()
cover.goto(225, 280)
cover.pendown() 
cover.stamp()

##Operator Function
def write(list):
    mult = 0
    for char in reversed(list):
        for wt in reversed(char):
            t.pu()
            t.goto(195 - 55*mult, 150)
            t.pd() 
            t.write(wt, font=("Arial", 74, "bold"))
            mult += 1

def screen_check(mult):
  if 195 - 55*mult < -300:
    return True
  else:
    return False

def calc_factorial(char):
  while char > 0:
    return char * calc_factorial(char - 1)
  return 1

def trigonomtry(equation, arithmetic, char):
    trig = eval(str(equation.split(char)[1]))
    trigtoinsert = arithmetic.index(char)
    arithmetic.pop(int(trigtoinsert))
    if char == 'sin':
        trig = str(round(math.sin(float(trig)),5))
    elif char == 'cos':
        trig = str(round(math.cos(float(trig)),5))
    elif char == 'tan':
        trig = str(round(math.tan(float(trig)),5))
    arithmetic.insert(trigtoinsert,str(trig))
    return equation, arithmetic

#Works as an On and Off Switch. If equal sign is present, pop it out so error does not occur.
def calculate(arithmetic, bool):

    if bool == True:
        arithmetic.pop()

    #Used for factorial. String manipulation.
    if '!' in arithmetic:
        stringclone = ''.join(arithmetic)
        for chars in arithmetic:
            if chars == '!':
                tempolist = ''.join(arithmetic).split('!')
                tempolist = list(tempolist[0])
                for char in reversed(tempolist):
                    try:
                        int(char)
                    except:
                        tempolist = ''.join(tempolist).split(char)
                        break
    
        sum =  str(calc_factorial(int(tempolist[(len(tempolist)-1)])))
        stringclone = stringclone.replace(tempolist[(len(tempolist)-1)] + '!',sum )
        answer = eval(stringclone)
        print(answer)
        arithmetic = stringclone

    equation = ''.join(arithmetic)
    print(arithmetic)
    trig = ['sin', 'cos', 'tan']
    for char in trig:
        print(char)
        if char in arithmetic:
            print(char)
            equation, arithmetic = trigonomtry(equation, arithmetic, char)
            print(equation, arithmetic)
    print(equation, arithmetic)
    equation = ''.join(arithmetic)

    try:
        print(equation)
        equation = str(eval(equation))
        t.clear()
        write(equation)
    except UnboundLocalError:
        t.clear()
        t.pu()
        t.goto(50, 150)
        t.pendown()
        t.write('Error', font=("Arial", 74, "bold"))
    
    
def button_pressed(x, y):
    global button, line_list
    printed = True
    if 46 - 55*0 > y > 46 - 55*1:
        if -290 + 115*0 < x < -290 + 115*1:
            button = '1/x'
        elif -290 + 115*1 < x < -290 + 115*2:
            button = 'Natural Logarithim'
        elif -290 + 115*2 < x < -290 + 115*3:
            button = 'log'
        elif -290 + 115*3 < x < -290 + 115*4:
            button = 'Clear'
            printed = False
        elif -290 + 115*4 < x < -290 + 115*5:
            button = 'Delete'
            printed = False

    if 46 - 55*1 > y > 46 - 55*2:
        if -290 + 115*0 < x < -290 + 115*1:
            button = 'sin'
        elif -290 + 115*1 < x < -290 + 115*2:
            button = 'cos'
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
            button = '**2' #Ten to the power of x
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
            button = '**'
        elif -290 + 115*1 < x < -290 + 115*2:
            button = '-' #Negative
        elif -290 + 115*2 < x < -290 + 115*3:
            button = 0
        elif -290 + 115*3 < x < -290 + 115*4:
            button = '.' #Decimal
        elif -290 + 115*4 < x < -290 + 115*5:
            button = '=' #Equal

    if printed != False:
        line_list.append(str(button))
    t.clear()

    #writes characters clicked on screen.

    write(line_list)

      #if characters go off screen:
    screencheck = screen_check(len(line_list))
    if screencheck == True:
        t.clear()
        equation = ''.join(line_list)
        line_list = []
        try:
          equation = str(eval(equation))
        except SyntaxError:
          t.pu()
          t.goto(50, 150)
          t.pendown()
          t.write('Error', font=("Arial", 74, "bold"))
          print(equation)
        write(line_list)


    #Special signs.
    if button == '=':
        calculate(line_list, True)
        line_list = []
    
    if button == 'Clear':
        t.clear()
        line_list = []
    
    if button == 'Delete':
        t.clear()
        print(line_list)
        line_list.pop()
        print(line_list)
        write(line_list)

    

# Fix 1280+

wn.onclick(button_pressed)
wn.mainloop()
