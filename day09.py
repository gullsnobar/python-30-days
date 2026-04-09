# The Python Match Statement
# Instead of writing many if..else statements, you can use the match statement.

# The match statement selects one of many code blocks to be executed.

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")



# Loops: A loop repeat a block of code multiple times

for i in range(5):
  print("Hello, I am Gull.")


for i in range(10):
  print("Hello, I am Gull.")




# 2. Types of Loops in Python
# There are 2 main loops:

# 1. for loop → used when you know how many times to run
# 2. while loop → used when condition decides

# Example 1: Print numbers 1 to 5

for i in range(1, 6):
  print(i)

for j in range(1, 20):
  print(j)

# Example 2: Loop through a list

names = ["Ali", "Sana", "Salman", "Ahmad"]
for name in names:
  print(name)

