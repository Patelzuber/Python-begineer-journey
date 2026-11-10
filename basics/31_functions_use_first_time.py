# my first basic calculator using functions first time in python 
a = float(input("Enter the value of a : "))
b = float(input("Enter the value of b : "))
def calculate(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b if b != 0 else "Undefined (division by zero)"
    return add, sub, mul, div
# Unpacking or unboxing the returned tuple from the calculate function
addition, subtraction, multiplication, division = calculate(a, b)
print("The addition, subtraction, multiplication and division of these numbers a and b are : ",
    addition,subtraction,multiplication,division,)
