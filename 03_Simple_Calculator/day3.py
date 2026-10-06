#Simple Calculator

#Step 1 : Get User input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#Step 2 : Perform arithmetic operation 
add = num1 + num2
sub = num1 - num2 
mul = num1 * num2 
div = num1 / num2 if num2 != 0 else "Cannot divide by zero"

#Step 3 : Display the results
print("\n --- Calculator Results ---- ")
print(f"Addition:{num1} + {num2} = {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Division: {div}")