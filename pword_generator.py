import random

# Default password length 
pword_length = 5

# Types of characters
uppercase_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
lowercase_letters = 'qwertyuiopasdfghjklzxcvbnm'
digits = '1234567890'
special_characters = '!@#$%^&*'

# Default characters allowed
uppercase_is_allowed = False
lowercase_is_allowed = True
digits_is_allowed = False
special_characters_is_allowed = False

# Options
print('Type [1] to generate a new password')
print('Type [2] to modify the password length')
print('Type [3] to modify the types of characters')
print('Type [4] to exit')

# Input
user_input = ''

# Function for coloring digits in blue and special_characters in pink like in Bitwarden XD
def color_pword(pword, digits, special_characters):
    BLUE = '\033[94m'
    PINK = '\033[95m'
    RESET = '\033[0m'

    colored_pword = ''

    for char in pword:
        if char in digits:
            colored_pword += BLUE + char + RESET
        elif char in special_characters:
            colored_pword += PINK + char + RESET
        else:
            colored_pword += char

    return colored_pword

while user_input != '4':
    user_input = input('\nYour choice: ')

    if user_input == '1':
        # The generated password
        pword = []
        
        # Characters allowed
        characters_allowed = ''

        # The number of items to return 
        k = random.randint(1, round(pword_length*0.2))

        if uppercase_is_allowed:
            pword += random.choices(uppercase_letters, k=k)
            characters_allowed += uppercase_letters

        if lowercase_is_allowed:
            pword += random.choices(lowercase_letters, k=k)
            characters_allowed += lowercase_letters

        if digits_is_allowed:
            pword += random.choices(digits, k=k)
            characters_allowed += digits

        if special_characters_is_allowed:
            pword += random.choices(special_characters, k=k)
            characters_allowed += special_characters

        # If all characters allowed are False then lowercase_letters are the default value
        if characters_allowed == '':
            pword = random.choices(lowercase_letters, k=pword_length)
        else:
            # Complete the rest 
            while len(pword) < pword_length:
                pword.append(random.choice(characters_allowed))

            # Mix the order
            random.shuffle(pword)

        # Convert list to string 
        pword = ''.join(pword)

        colored_pword = color_pword(
            pword,
            digits,
            special_characters
        )
        
        print('\nThe generated password:', colored_pword)
        
    elif user_input == '2':
        # Must be superior or equal to 5
        pword_length = 0

        while int(pword_length) < 5 or int(pword_length) > 128:
            pword_length = int(input('\nPassword length (5 ≤ length ≤ 128): '))
    elif user_input == '3':
        # Uppercase letters option
        yes_or_no = input('\nDo you want to allow (A-Z)? [Y/n]: ')

        if yes_or_no == 'Y' or yes_or_no == 'y':
            uppercase_is_allowed = True
        elif yes_or_no == 'N' or yes_or_no == 'n':
            uppercase_is_allowed = False
        else:
            print('Invalid command')
        
        # Lowercase letters option
        yes_or_no = input('Do you want to allow (a-z)? [Y/n]: ')

        if yes_or_no == 'Y' or yes_or_no == 'y':
            lowercase_is_allowed = True
        elif yes_or_no == 'N' or yes_or_no == 'n':
            lowercase_is_allowed = False
        else:
            print('Invalid command')

        # Digits option
        yes_or_no = input('Do you want to allow (0-9)? [Y/n]: ')

        if yes_or_no == 'Y' or yes_or_no == 'y':
            digits_is_allowed = True
        elif yes_or_no == 'N' or yes_or_no == 'n':
            digits_is_allowed = False
        else:
            print('Invalid command')

        # Special characters option
        yes_or_no = input('Do you want to allow (!@#$%^&*)? [Y/n]: ')

        if yes_or_no == 'Y' or yes_or_no == 'y':
            special_characters_is_allowed = True
        elif yes_or_no == 'N' or yes_or_no == 'n':
            special_characters_is_allowed = False
        else:
            print('Invalid command')
    elif user_input == '4':
        print('\nHave a nice day!\n')
    else:
        print('Invalid command')