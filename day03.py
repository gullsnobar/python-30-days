# Functions in Python

#  A function is a reuseable block of code that performs a specific task
#  Instead of writing a block of code again and again you write that code inside function and reuse it.

def greet():
    print("How are you?")
greet();

#  Another example

def say_hello():
    print("Hello World!");
say_hello()

# Functions with Parameters
# You can pass data into a function

def greet(name):
    print("Helle", name);
greet("Gull");

# ✔ name is called a parameter
# ✔ "Gull" is an argument

def say_hello(name):
    print("Hi", name);
say_hello("Hayya")

# Functions with Return Value
# Functions can also return data

def add(a, b):
    return a + b;
result = add(6,6)
print(result);

# Real Example

def check_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even(6));
print(check_even(9));
        

