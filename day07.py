# Python Lists
# Lists are used to store multiple items in a single variable.

mylist = ["apple", "orange" ,"banana" ,"graphes"]
print(mylist);

# Lists Items
# Lists items are ordered, changeable and allow duplicate values.


# List Length
# To determine how many items a list has, use the len() function:

list = ["Hello", "Snobar", "Amjad", "Ali"]
print(len(list));



# Example of lists

fruits = ["apple", "mango", "orange", "grapes"]
print(fruits);

# Example 2 (Modify lists)

numbers = [1,2,3,4,5];
numbers[0] = 10;
print(numbers)


# What is a Tuple?

# A tuple is like a list BUT:

# Ordered 
# NOT changeable (immutable) 
# Allows duplicates 

# Think: “fixed data (cannot change)”


# Example 1

colors = ("red", "green", "blue", "yellow");
print(colors);

# Example 2

# colors = ("red", "green", "blue", "yellow");
# colors[1] = "purple"    # here it shows error becoz tuple is immutable
# print(colors)



# What is a Set?

# A set is:

# Unordered 
# No duplicates 
# Changeable 

# Think: “unique values only”


numbers = {1,2,3,3,4,5,6,6,7,8,9,10}
print(numbers)

# Add Items is set allows

my_lists = {"apple", "banana", "orange"}
my_lists.add("cherry");
print(my_lists);
        