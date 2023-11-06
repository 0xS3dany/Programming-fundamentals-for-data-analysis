statement = input("Enter a statement: ")

statement = statement.lower()

vowel_count = 0

vowels = "aeiou"

for char in statement:
    if char in vowels:
        vowel_count += 1

if vowel_count > 0:
    print(f"Number of vowel letters in the statement: {vowel_count}")
else:
    print("No vowels found in the statement.")
