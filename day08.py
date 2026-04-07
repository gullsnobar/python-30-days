#  Python If Else statement
# if else statent used when you want two outcomes.

a = 200;
b = 40;

if (a > b):
    print("a is greater than b");
else:
    print("b is smaller than a");

# Indentation
# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

# Example

# If statement, without indentation (will raise an error):

a = 33
b = 200
if b > a:
 print("b is greater than a") # you will get an error

#  Multiple Statements in If Block
# You can have multiple statements inside an if block. All statements must be indented at the same level.

age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")


age = 16;
if age >= 18:
   print("You can vote");
else:
   print("You cannot vote");


# if-elif-else (Multiple Conditions)
# Used when you have multiple choices

marks = 70;

if marks >= 85:
   print("You are Topper");
elif marks >= 75:
   print("You are good student");
elif marks >= 65:
   print("You are average student");
else:
   print("You need to work hard")


age = 20;
has_id = True;

if age >= 20 and has_id:
   print("You can enter the club")

# Nested if (Intermediate)
#  if inside if called nested if

age = 20;
has_id = True;

if age > 20:
   if has_id:
      print("Entry Allowed");
   else:
      print("ID Required");
else:
   print("You are underage")


# Ternary Operator
#  write if else in one line also called short hand.


age = 18;
result = "Adult" if age >= 18 else "Minor"
print(result)

number = 20;
result1 = "Even Number" if number % 2 == 0 else "Number is Odd"
print(result1)

marks = 90;
result2 = "Wonderful have A Grade" if marks >= 90 else ("Grade B");
print(result2)