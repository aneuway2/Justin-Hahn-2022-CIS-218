"""WEEK 3 LAB
Justin Hahn
"""


userString =input('enter any string')

VOWEL_COUNT = 0
UPPERCASE_COUNT = 0
LOWERCASE_COUNT = 0
SPACE_COUNT = 0
PUNCTUATION_COUNT = 0

for c in userString:
    if c in "AEIOUaeiou":
        print (c, "is a vowel")
        VOWEL_COUNT += 1

    if "A" <= c <= "Z":
        print (c, "is uppercase")
        UPPERCASE_COUNT += 1

    if "a" <= c <= "z":
        print (c, "is lowercase")
        LOWERCASE_COUNT += 1

    if c in " ":
        print (c, "is a space")
        SPACE_COUNT += 1

    if c in ",.:/?!@#$%&":
        print (c, "is punctuation")
        PUNCTUATION_COUNT += 1

print(f'There were {VOWEL_COUNT} vowels')
print(f'There were {UPPERCASE_COUNT} uppercase letters')
print(f'There were {LOWERCASE_COUNT} lowercase letters')
print(f'There were {SPACE_COUNT} spaces')
print(f'There were {PUNCTUATION_COUNT} punctuation')
