# What is OOP?
# OOP stands for Object-Oriented Programming.

# Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.

# What are Classes and Objects?
# Classes and objects are the two core concepts in object-oriented programming.

# A class defines what an object should look like, and an object is created based on that class. For example:

# Create a Class

class MyClass:
    x = 5;
print(MyClass)

class Student:
    name = "Gull";
    age = 21;
    
    # Create Object
s1 = Student()
print(s1.name);
print(s1.age)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating objects
s1 = Student("Ali", 21)
s2 = Student("Sara", 22)

print(s1.name, s1.age)
print(s2.name, s2.age)