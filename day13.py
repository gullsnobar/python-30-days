#  What is a Python Module?

# A module in Python is just a file (.py) that contains code you want to reuse.

# Think of it like:

# A toolbox
# A library of functions + variables

# Instead of writing everything again, you just import and reuse it.

person1 = {
    "name": "Alice",
    "age": 30,
    "city": "Norway"
}
print(person1)


# Practical Examples

def add (a, b):
    return a + b

def multiply (a, b, c):
    return a * b * c

def format_name(name):
    return name.strip().title()

# Random password generator

import random
import string

def generate_password():
    chars = string.ascii_letters + string.digits
    return " ".join(random.choice(chars) for _ in range(8))

print(generate_password())


x = min(5, 10, 3, 4)
y = max(4,6,7,3)

print(x)
print(y)


# The abs() function returns the absolute (positive) value of the specified number:

x = abs(-90327)
print(x)

# The pow(x, y) function returns the value of x to the power of y (xy).

x = pow(4,6)
print(x)