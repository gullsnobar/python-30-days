def check_even(num):
    if num % 2 == 0:
        return ("Even")
    else:
        return ("Odd")

print(check_even(7));


#  Strings in Python

# Multiline strings

a = """ Hello World """
print(a)

# Upper Case: The upper case method returns the strings in upper case.

a = "Snobar"
print(a.upper());

# Lower Case: The lower case method returns the strings in lower case. 

a = "Snobar"
print(a.lower())

# Remove Whitespace
# Strip method removes the white spaces from the start or in the end.

a = " Tayyab "
print(a.strip())

# Replace String

a =  "Martoon"
print(a.replace("M", "C"))

# Split String
# The split metho splits the string into substrings if it finds the instances of the separator.

a = "Hello, World, Gull"
print(a.split(","));

# String Concatication

#  You can concatate two or more strings by using + operator.

x = "Hello";
y = "Snoabre";
z = x + y
print(z)

# Adding space we use "  "

a = "Gull"
b = "Snobar"
c = a + " " + b;
print(c)

# To add a space between them, add a " ":