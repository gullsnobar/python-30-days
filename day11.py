# Array = A container that stores multiple values in one variable

# But important point 👇
# ⚠️ Python does NOT have built-in arrays like C/Java
# 👉 Instead, we mostly use Lists as arrays

cars = ["Ford", "Volvo", "BMW"]
print(cars)

# Indexing is very important
# Indexing always starts from zero

colors = ["Red", "Blue", "Green", "Yellow"]
print(colors[0]);
print(colors[2])

# neagative indexing
print(colors[-1])

# Modify Elements

fruits = ["Apple", "Banana", "Mango"]
print("Fruits", fruits)

fruits[0] = "Strawberry"
print(fruits)

# find the length of elements

print(len(fruits))

# Important Methods

numbers = [1,2,9,5,3,7,3,10,26];
print(numbers)
print(numbers.sort());
print(numbers.remove(1));
numbers.append(1);
numbers.count(2);
numbers.index(7);