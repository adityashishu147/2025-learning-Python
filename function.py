#Function reusable piece of code , we can call functionn anywhere in the program , we create function using def keyword 

def name(name):
    print(f"Hello , {name}")


name("aditya")
name ("shishu")


def addition(x,y):
    return x + y


print(addition(5,10))
print(addition(599,310))


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def even(num):
    return num % 2 == 0

def odd(num):
    return num % 2 != 0

def square(num):
    return num ** 2

num = int(input("Enter the number:--"))

if even(num):
    print(f"Number is even {num}")
else:
    print(f"Number is odd {num}")

print (f"The input {num} quare is  {square(num)}" )

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Funtion for mathematics


import another function into new file 

#math_operations.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

##### In another Python file, you can import and use the functions from the module:

import math_operations

result_add = math_operations.add(3, 4)
result_subtract = math_operations.subtract(7, 2)

print(result_add)     # Output: 7
print(result_subtract)  # Output: 5
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





