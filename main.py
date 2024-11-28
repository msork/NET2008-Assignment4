# Modified code from https://www.geeksforgeeks.org/create-a-random-password-generator-using-python/

import string
import random

# Getting password length
length = int(random.randint(2,20))

# Declare variables
isDigit = False
isLetter = False
isSpecial = False

characterList = ""

# Getting character set for password
# Make the character set truly random by running a random amount of times
runTimes = int(random.randint(1,20))

for i in range(runTimes):
    choice = random.randint(1,3)

    if (choice == 1):
        if (isDigit):
            # Remove digits to possible characters
            characterList = characterList.replace(string.digits, "")
            isDigit = False
        else:
            # Add digits to possible characters
            characterList += string.digits
            isDigit = True
    elif (choice == 2):
        if (isLetter):
            # Remove letters to possible characters
            characterList = characterList.replace(string.ascii_letters, "")
            isLetter = False
        else:
            # Add letters to possible characters
            characterList += string.ascii_letters
            isLetter = True
    elif (choice == 3):
        if (isSpecial):
            # Remove special characters from possible characters
            characterList = characterList.replace(string.punctuation, "")
            isSpecial = False
        else:
            # Add special characters to possible characters
            characterList += string.punctuation
            isSpecial = True

# If characterList is empty, choose something
if (characterList):
    pass
else:
    choice = int(random.randint(1, 3))
    if (choice == 1):
        characterList += string.digits
    elif (choice == 2):
        characterList += string.ascii_letters
    elif (choice == 3):
        characterList += string.punctuation

password = []

for i in range(length):
    # Picking a random character from our character list
    randomchar = random.choice(characterList)

    # Append a random character to password
    password.append(randomchar)

# Print password as a string
print("The random password is " + "".join(password))
