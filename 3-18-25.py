# Take input from user
user_input = input("Enter elements of the list separated by spaces: ")
element_to_count = input("Enter the element to count: ")

# Convert input to list
elements = user_input.split()

# Initialize a counter
count = 0

# Loop through the list and manually count
for item in elements:
    if item == element_to_count:
        count += 1

# Display the result
print(f"The element '{element_to_count}' appears {count} time(s) in the list.")

# Take input from user
user_input = input("Enter elements of the list separated by spaces: ")

# Convert input to list
original_list = user_input.split()

# Create a new empty list for the copy
copied_list = []

# Manually copy elements one by one
for item in original_list:
    copied_list.append(item)

# Display both lists
print("Original List:", original_list)
print("Copied List:", copied_list)

