# Strong Password Detection - Write a function that uses regular expressions to make sure the password
# string it is passed is strong. A strong password is defined as one that is at least eight characters long,
# contains both uppercase and lowercase characters, and has at least one digit. You may need to test the
# string against multiple regex patterns to validate its strength.

import re

# > 7 chars, 1 U, 1 l, 1 #
def TestPassword(password):
    mo = numberRegex.search(password)
    if mo is None:
        print("No numbers in the password")
        return False
    mo = ucRegex.search(password)
    if mo is None:
        print("No UpperCase character in the password")
        return False
    mo = lcRegex.search(password)
    if mo is None:
        print("No LowerCase character in the password")
        return False
    mo = spacesRegex.search(password)
    if mo is not None:
        print("There are spaces are in the password")
        return False
    if len(password) > 7 :
        print("Password is " + str(len(password)) + " characters long, it must be at least 8")
        return False
    return True


# Variables
passedRequirements = False
gotGoodPassword = False
password = ""

# regexes
numberRegex = re.compile(r'\d')
lcRegex = re.compile(r'[a-z]')
ucRegex = re.compile(r'[A-Z]')
spacesRegex = re.compile(r'[\s]')

# Main Program
while not passedRequirements:
    password = input("Enter a password: ")
    passedRequirements = TestPassword(password)

print("Password '" + password + "' is good!")
