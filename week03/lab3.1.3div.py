# Program  that reads in two numbers and
# divides the first one by the second and give the integer result and the
# remainder
# Author: Jaime Lara Carrillo

num1 = int(input("Enter first number: "))
num2 = int(input("Enter the number you want to divide by: "))
div = int(num1//num2)
divremainder =(round(num1/num2, 2))
print("{} divided by {} is {} with remainder {}".format(num1, num2, div,  divremainder))