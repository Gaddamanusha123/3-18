text = "Hello Anusha Welcome To Python Programming"

# Convert to lowercase to make comparison easier
text = text.lower()

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in text:
    if char.isalpha():  # Check if the character is a letter
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
