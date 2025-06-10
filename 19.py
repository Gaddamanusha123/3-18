# task:-Implement the program to print true when the first and last element in the list was even, else print false
numbers = [2, 5, 7, 9, 4]

# Check if first and last elements are even
if numbers[0] % 2 == 0 and numbers[-1] % 2 == 0:
    print("True")
else:
    print("False")

# 2) implement the program to create a function which performs the count method. Without using any methods.

my_list = ['a', 'b', 'c', 'a', 'a']
element_to_count = 'a'

# Initialize counter
count = 0

# Manually count occurrences
for item in my_list:
    if item == element_to_count:
        count += 1

print("The element", element_to_count, "appears", count, "time(s).")


# 3) write a program to print the prime numbers in the new list from the existing list.

original_list = [4, 5, 6, 7, 8, 9, 10, 11, 13]
prime_list = []

# Check each number for primality
for num in original_list:
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(num)

print("Prime numbers in the list:", prime_list)
