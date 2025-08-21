
# Task 1: Calculate Factorial Using a Function
n=int(input('Enter a number :'))
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
simple_number = (n)
result= factorial(simple_number)
print(f'Factorial Of {simple_number} is {result}.')


# Task 2: Using the Math Module for Calculations
import math

number = int(input('Enter a number :'))
if number >=0:
    a= math.sqrt(number)
else :
    a = "Cannot calculate square root of a negative number."
if number > 0 :
    b=math.log(number)
else :
    b = "Cannot calculate natural logarithm for negative numbers."
if number > 0 :
    c = math.sin(number)
else :
    c = "Cannot calculate square root of a negative number."

print('Square Root :',a)
print('Logarithm :',b)
print('Sine :',c)