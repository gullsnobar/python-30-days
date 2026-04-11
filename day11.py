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


# 🔹 1. What is Slicing?

# Slicing = extracting a part (subset) of a list

nums = [1, 2, 3, 4, 5];
print(nums[1:4]);

cars = ["Ford", "Civic", "Camry", "Acura"];
print(cars[0:2])


#  Methods of arrays

# append method --> add some elements in the last

num = [1,2,2,5,7,8,3,4,5,0]
print(num.append(100));

# insert method --> add element in specific position

num = [1,8,5,3];
num.insert(1, 788);
print(num);

# extend --> extend method is used to merge the list

a = [1,2];
b = [6,9];

a.extend(b)
print(a)

# remove() --> removes the first occurrence of the specified value

num = [1,8,9,4,6,2,0,1];
num.remove(8);
print(num)

# Pop() --> remove by index

num = [7,8,9,4];
num.pop(2);
print(num)


# Clear --> remove everything

num = [1,2,3,4,4,5,5];
num.clear()
print(num)

# Count --> use to count occurrences of a value
num = [7,9,3,7,9,6,8,7,7]
print(num.count(7))

# sort --> Sort the list

num = [7,9,2,3,6,1,8]
num.sort()
print(num)

# reverse method is used to reverse the order

num = [1,2,3,5,6]
num.reverse()
print(num)