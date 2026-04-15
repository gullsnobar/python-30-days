# Python Function
# Function is a block of code which only runs when it is called
# A function helps avoiding code repeatition

from unicodedata import name


def my_function():
    print("Hello, World!")
my_function()




def my_function(fname):
  
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


# Parameters vs Arguments
# The terms parameter and argument can be used for the same thing: information that are passed into a function.

# From a function's perspective:

# A parameter is the variable listed inside the parentheses in the function definition.

# An argument is the actual value that is sent to the function when it is called.

def my_function(name): # name is a parameter
 print("Hello", name)

my_function("Emil") # "Emil" is an argument