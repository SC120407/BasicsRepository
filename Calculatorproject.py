#Calculator project
def calc():
    #First number input
    #Second number input

    print("addition: +")
    print("subtraction: -")
    print("multiplication: *")
    print("division: /")
    print("exponent: ^")
    print("floor dision: //")
    print("modulo: mod")
    operation = (input("Operation: "))

    if operation == "+":
        num_1 = float(input("First Number: "))
        num_2 = float(input("Second Number: "))
        print(num_1 + num_2)
    elif operation == "-":
        num_1 = float(input("First Number: "))
        num_2 = float(input("Second Number: "))
        print(num_1 - num_2)
    elif operation == "*":
        num_1 = float(input("First Number: "))
        num_2 = float(input("Second Number: "))
        print(num_1 * num_2)
    elif operation == "/":
        num_1 = float(input("First Number: "))
        num_2 = float(input("Second Number: "))
        print(num_1 / num_2)
    elif operation == "^":
        num_1 = float(input("First Number: "))
        num_2 = float(input("Second Number: "))
        print(num_1 ** num_2)
    elif operation == "//":
        num_1 = float(input("First Number: "))
        num_2 = float(input("Second Number: "))
        print(num_1 // num_2)
    elif operation == "mod":
        num_1 = float(input("First Number: "))
        num_2 = float(input("Second Number: "))
        print(num_1 % num_2)
    else:
        print("Invalid operation")

calc()

"""
#First number input
num_1 = float(input("First Number: "))
#Second number input
num_2 = float(input("Second Number: "))

operation = (input("Operation: "))
print("addition: +")
print("subtraction: -")
print("multiplication: *")
print("division: /")
print("exponent: ^")
print("floor dision: //")
print("modulo: mod")

if operation == "+":
    print(num_1 + num_2)
elif operation == "-":
    print(num_1 - num_2)
elif operation == "*":
    print(num_1 * num_2)
elif operation == "/":
    print(num_1 / num_2)
elif operation == "^":
    print(num_1 ** num_2)
elif operation == "//":
    print(num_1 // num_2)
elif operation == "mod":
    print(num_1 % num_2)
else:
    print("Invalid operation")
"""
