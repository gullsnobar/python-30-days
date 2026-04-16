# What is a Python Module?
# A module is just a .py file containing reusable code

# Example dictionary
person1 = {
    "name": "Alice",
    "age": 30,
    "city": "Norway"
}
print(person1)


# Practical Examples

def add(a, b):
    return a + b

def multiply(a, b, c):
    return a * b * c

def format_name(name):
    return name.strip().title()


# Random password generator
import random
import string

def generate_password():
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(8))  # FIXED (removed spaces)

print(generate_password())


# Built-in functions
x = min(5, 10, 3, 4)
y = max(4, 6, 7, 3)

print(x)
print(y)

# Absolute value
x = abs(-90327)
print(x)

# Power function
x = pow(4, 6)
print(x)


# JSON Example
# JSON uses DOUBLE quotes only

import json

data = {
    "name": "Ali",
    "age": 30
}
print(data)

# Correct JSON string
# JSON requires double quotes

X = '{"name": "Ali", "age": 30}'

# Convert JSON -> Python
Y = json.loads(X)

print(Y)
print(Y["age"])

# Sets
# A set is a set of characters inside a pair of square brackets [] with a special meaning: