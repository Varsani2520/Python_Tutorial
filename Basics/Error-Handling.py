# 1.handling specific exceptions

try:
    x=10/0
except ZeroDivisionError:
    print("You cannot divide by zero")          
    
    
#2. Handling Multiple Exceptions 

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter a number.")

#3.handling multiple exceptions in 1 block:
# You can use a tuple to handle multiple exceptions in one except block.

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except (ZeroDivisionError, ValueError) as e:
    print(f"An error occurred: {e}")

# 4. Using else Block
# The else block executes if no exception is raised in the try block.

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter a number.")
else:
    print(f"Result is: {result}")


# 5. Using finally Block
# The finally block executes regardless of whether an exception is raised or not.
try:
    f = open("test.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution complete.")


#6. Raising Exceptions Manually
# You can manually raise exceptions using the raise keyword.

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
except ValueError as e:
    print(e)


# 7. Custom Exceptions
# You can create your own exceptions by subclassing the Exception class.


class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error.")
except CustomError as e:
    print(e)



# 8. Handling Exceptions in Functions
# You can handle exceptions in function definitions.

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."

result = divide(10, 0)
print(result)


# 9. Logging Errors
# Use the logging module to log errors instead of printing them.

import logging

logging.basicConfig(level=logging.ERROR)
try:
    num = int("a")  # Invalid conversion
except ValueError as e:
    logging.error(f"An error occurred: {e}")



# Quick Summary of Keywords
# try	Contains code that might raise exceptions.
# except	Handles specific or generic exceptions.
# else	Executes code if no exceptions are raised.
# finally	Executes code regardless of exceptions.
# raise	Raises exceptions manually.