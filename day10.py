# While loop

# Basic Counter
i = 1

while i <= 5:
    print(i)
    i += 1


# Infinite Loop (⚠️ Uncomment to run)
# while True:
#     print("Hello")


# Control Statement
# Break loop
for i in range(10):
    if i == 5:
        break
    print(i)


# Continue
# Skip current iteration
for j in range(5):
    if j == 2:
        continue
    print(j)


# pass statement (does nothing)
print("Pass statement does nothing")

for i in range(7):
    pass


# Example: Even and Odd Numbers
numbers = [40, 37, 89, 28, 20, 46, 90, 39]

for num in numbers:
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")


# Another example
# Find Maximum Number in the list
numbers = [3, 6, 9, 5, 89, 67, 2]
max_number = numbers[0]

for num in numbers:
    if num > max_number:
        max_number = num

print("Max:", max_number)