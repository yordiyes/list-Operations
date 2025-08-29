my_list = []

# Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert 15 at the second position (index 1)
my_list.insert(1, 15)

# Extend with another list
my_list.extend([50, 60, 70])

# Remove the last element
my_list.pop()

# Sort in ascending order
my_list.sort()

# Find and print index of value 30
index_of_30 = my_list.index(30)

# Print final list and index of 30
print("Final List:", my_list)
print("Index of 30:", index_of_30)
