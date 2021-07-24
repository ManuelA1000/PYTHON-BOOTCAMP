"""
Use Python script to generate a random password of 8 characters. Each time the program is run, a new password will be generated randomly. The passwords generated will be 8 characters long and will have to include the following characters in any order:

2 uppercase letters from A to Z,
2 lowercase letters from a to z,
2 digits from 0 to 9,
2 punctuation signs such as !, ?, “, # etc.
Hint: To solve this challenge we will have to generate random characters and to do so we will need to use the ASCII code.

ASCII Code: The ASCII code, is a code for representing English characters as numbers, with each character assigned a number from 0 to 127. For example, the ASCII code for uppercase M is 77. The extended ASCII code contains 256 characters (using numbers from 0 to 255).
"""
import random
import string

# invoking corresponding string functions
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digit = string.digits
symbols = string.punctuation

# randomly generating values and joining them
test = random.sample(lower, 2) + random.sample(upper, 2) + random.sample(digit, 2) + random.sample(symbols, 2)

# joining the values to form one random password
password = "".join(test)

# randomly picking a password from the sample
final = random.sample(password, 8)
print(password)
