# Python Booleans

# Booleans represent one of two values: True or False.

a = 200;
b = 45;

if(a > b):{
    print("a is greater than b")
}
else: {
    print("a is not greater than b")
}

# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return,

x = "Snobar";
y = b;

print(bool(x));
print(bool(y));


x1 = 0;
print(bool(x1))


# Most Values are True
# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.



# Python Operators
# Operators are used to perform operations on variables and values.

# Python divides the operators in the following groups:

# Arithmetic operators


x = 15;
y = 4;

print(x + y);
print(x - y);
print(x * y)
print(x / y)



# Assignment operators
# Assignment operators are used to assign values to variables:

# The Walrus Operator
# Python 3.8 introduced the := operator, known as the "walrus operator". It assigns values to variables as part of a larger expression:

numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

