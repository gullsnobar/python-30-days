#  Python PIP

# What is python PIP

# Pip is a package manager for python packages, or a module if you like

# What is a package
# A package contains all the files you need for a module.


# Note: If you have Python version 3.4 or later, PIP is included by default.

# Python Try Except

# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# Basic Example (Handling Errors)

try:
    x = int(input("Enter a number: "))
    print(10 / x)
except:
    print("Something went wrong!")
    
    
    # Specific Exception Handling
    
    try:
        x = int(input("Enter a Number: "))
        result = 10 / x;
    except ValueError:
        print("Invalid Input! Please enter a number.")    
    except ZeroDivisionError:
        print("You cannot divide by zero.")
    
    
    
    

