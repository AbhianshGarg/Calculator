##imports
import turtle as trtl
import math

##initialization
t = trtl.Turtle()
wn = trtl.Screen()
operation_list = ['+', '-', '*', '/']

##First Number
num_one = input('num 1: ' )



##Find operation
num_one = str(num_one)
for char in operation_list:
    try:
        result = num_one.find(char)
        if result >= 0:
            num_one = num_one.split(char)
            num_one[1] = char
    except AttributeError:
        break

