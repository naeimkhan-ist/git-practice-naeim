# date function call
from datetime import date
print("Naeim Khan")
print("Today's date:", date.today())

# add/subtract/multiply function call
from utils import add, subtract, multiply, divide
print("2 + 3 =", add(2, 3))
print("5 - 2 =", subtract(5, 2))
print("2 * 3 =", multiply(2, 3))
print("10 / 2 =", divide(10, 2))
print("10 / 0 =", divide(10, 0))