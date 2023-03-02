# Write a program (floor.py), that takes in a float and outputs an int rounded
# down, you will need the math module math.floor()
# Author: Jaime Lara Carrillo

import math
number = float(input("Enter a float number : "))
floated_number = math.floor(number)
print("If we round down the number {} it become {} " .format(number, floated_number))