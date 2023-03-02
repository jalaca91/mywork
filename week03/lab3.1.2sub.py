# Program to subtract on number from another.
# input reads in a string so we need to convert it into an int
# so we can perform mathematical operations
# Author: Jaime Lara Carrillo

num1 = int(input(" First number is :"))
num2 = int(input(" Second number is :"))
restart = (num1 - num2)
print("{} minus {} is {} ".format(num1, num2, restart))