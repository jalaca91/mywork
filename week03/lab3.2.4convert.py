# This program takes in a float amount of dollars and returns that
# absolute amount in cent.
# Author: Jaime Lara Carrillo

amount = float(input("Please enter an amount :"))
abs_amount = abs(amount)
convert = int(abs_amount * 100)
print("That amount {} in cent is {}" .format(amount, convert))