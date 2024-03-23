#Calculator project
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
Choice = input.("Enter Your Expression:")
print(eval(Choice))
    print(num_1 % num_2)


