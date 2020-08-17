#SOLOLEARN PYTHON COURSE LESSON 3

#IMPORTING MODULES
import random
from math import pi, exp
from math import sqrt as square_root #naming the sqrt function as square_root

for i in range(5):
   value = random.randint(1, 6)

print("This is your random number: ")
print(value)
print(pi)
print(square_root(100))

#FUNCTIONS AND MODULES
def my_func():
    print("Hola mundo")

my_func()

#FUNCTIONS AND VARIABLES INSIDE THEM MUST BE DECLARED BEFORE CALLING THEM

def print_some(word1, word2):
    print(word1+" "+word2+" !!!!!")

print_some("Hello", "World")

#VARIABLES INSIDE FUNCTIONS CANNOT BE REFERENCED OUTSIDE THEM

def numbers(num1, num2):
    if(num1>num2):
        return num1
    else:
        return num2
        #print("Cierto") THIS WILL NOT BE EXECUTED

num3=numbers(5,8)
print(num3)

"""
THE RETURNED VALUE CAN BE USED LATER IN OTHER DECLARATIONS
AFTER RETURN STATEMENT, ANY CODE WILL NOT BE EXECUTED
"""

#FUNCTIONS AS ARGUMENTS
def comp_func(numbers, num4, num5):
    return numbers(5,8)+num4+num5

print(comp_func(numbers, 2, 6))



