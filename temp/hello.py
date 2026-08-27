# import re

# # Example 1️⃣: Match word at beginning
# text = "abcde"

# # re.match checks only at the beginning of the string
# match = re.match(r"[a-z]", a)
# match2 = re.match(r"[A-Z]", b)
# if match and match2:

# if match:
#     print("Word starts with Hello")
# else:
#     print("No match found")

# # Example 2️⃣: Search word anywhere in string

# text = "Learning Python regex"

# # re.search finds pattern anywhere in the string
# result = re.search(r"Python", text)

# if result:
#     print("Found:", result.group())

# # Example 3️⃣: Find all occurrences

# text = "cat dog cat bird cat"

# # re.findall returns all matches as a list
# animals = re.findall(r"cat", text)

# print(animals)

# # Example 4️⃣: Extract all numbers

# text = "Invoice 45 items, total cost 1200"

# # \d+ matches one or more digits
# numbers = re.findall(r"[a-z]", text)

# print(numbers)

# # Example 5️⃣: Validate Email

# email = "user.name@gmail.com"

# # Regex pattern for email validation
# pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+ \.[a-zA-Z]{2,}$"

# # Check if email matches pattern
# if re.match(pattern, email):
#     print("Valid Email")
# else:
#     print("Invalid Email")

# # Example 6️⃣: Replace text using regex

# text = "I love Java"

# # re.sub replaces matched pattern
# updated_text = re.sub(r"Java", "Python", text)

# print(updated_text)

# # Example 7️⃣: Split string using multiple delimiters

# text = "apple,banana;orange mango"

# # Split by comma, semicolon or space
# parts = re.split(r"[,\s;]+", text)

# print(parts)

# # Example 8️⃣: Validate Indian Mobile Number

# phone = "9876543210"

# # Indian numbers start with 6-9 and have 10 digits
# pattern = r"^[6-9]\d{9}$"

# if re.match(pattern, phone):
#     print("Valid Mobile Number")
# else:
#     print("Invalid Mobile Number")

# # Example 9️⃣: Extract capitalized words

# text = "Python Is Created By Guido Van Rossum"

# # \b ensures word boundary
# # [A-Z] first letter capital
# words = re.findall(r"\b[A-Z][a-z]*\b", text)

# print(words)

# # Example 🔟: Check string contains only alphabets

# text = "Python"

# # ^ and $ ensure full string match
# pattern = r"^[A-Za-z]+$"

# if re.match(pattern, text):
#     print("Only alphabets")
# else:
#     print("Contains other characters")




# # Print the maximum value.

# # input = 5
# # output = 10 25 3 99 45



# # Print word and count.
# # 5
# # apple
# # banana
# # apple
# # orange
# # banana


# # apple 2
# # banana 2
# # orange 1