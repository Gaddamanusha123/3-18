    
# Task 1: Take a paragraph check the count of words, if count is more than 100, print valid ; else invalid
paragraph = """Python is a powerful programming language. It is widely used in web development, data analysis, machine learning, and more.
It’s known for its simplicity and readability. Developers around the world prefer Python for rapid development."""

word_count = 0
in_word = False

for char in paragraph:
    if char == ' ' or char == '\n':
        if in_word:
            word_count += 1
            in_word = False
    else:
        in_word = True

# To count the last word if the paragraph doesn't end with space
if in_word:
    word_count += 1

print("Word count:", word_count)
if word_count > 100:
    print("Valid")
else:
    print("Invalid")
   
#Task2: take a input with both upper and lower cases characters count the no.of uppercases and lower cases without using any methods
    text = "HeLLo PyThOn"

uppercase_count = 0
lowercase_count = 0

for ch in text:
    ascii_val = ord(ch)
    if 65 <= ascii_val <= 90:      # Uppercase A-Z
        uppercase_count += 1
    elif 97 <= ascii_val <= 122:   # Lowercase a-z
        lowercase_count += 1

print("Uppercase letters:", uppercase_count)
print("Lowercase letters:", lowercase_count)

