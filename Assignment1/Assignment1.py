"""
Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.
"""
num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = float(num1 / num2)

print("Addition: ",add)
print("Subtraction: ",sub)
print("Multiplication: ",mul)
print("Division: ",div)

"""
Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
"""

str1 = input("Enter your first name: ")
str2 = input("Enter your last name: ")

print("Hello,"+" "+str1+" "+str2+"!"+" "+"Welcome to the Python Program")


