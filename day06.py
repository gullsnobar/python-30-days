# Comparison operators
# Comparison operators are used to compare two values

x = 6;
y = 3;

print(x == y);
print(x != y);
print(x > y);
print(x < y);
print(x >= y);
print(x <= y);


# Chaining Comparison Operators in Python

# In Python, you can combine multiple comparisons in a single expression. This is called chaining comparison operators.

x = 6;

print( 1 < x < 10);
print(1 < x and x < 10)


y = 10;
print( 2 < y < 20);
print(6 > y and y > 3);



# Logical operators
# Logical operators are used to combine conditional statements

# and 	Returns True if both statements are true	x < 5 and  x < 10	
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

#  and operator

s = 6;
print ("s is", s > 3 and s < 16);

s = 8
print( "s is", s > 3 or s > 5);


x = 5;
y = 2;

print(x != y);
print(x is not y)




# Identity operators
# Membership operators
# Bitwise operators
