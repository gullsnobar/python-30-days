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