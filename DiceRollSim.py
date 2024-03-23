#Diceroll
import math
import random

lower_bound = int(input("Lower Bound: "))
upper_bound = int(input("Upper Bound: "))

if lower_bound < upper_bound:
    num_1 = random.randint(lower_bound, upper_bound)
    num_2 = random.randint(lower_bound, upper_bound)
    print(str(num_1) + ", " + str(num_2))
    print(num_1 + num_2)
else:
    print("Error in Bounds")
