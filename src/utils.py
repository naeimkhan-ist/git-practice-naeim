# Adding
def add(a, b):
    return a + b

# Subtracting
def subtract(a, b):
    return a - b

# Multipling
def multiply(a, b):
    return a * b

# Dividing with error handling
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"