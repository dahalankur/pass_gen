####################################
#      pass_gen.py                 #
#    A simple password generator   #
#    Ankur Dahal                   #
####################################
import sys
import random


character = ['UPPERCASE', 'LOWERCASE', 'SYMBOLS', 'DIGITS']
lower_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '[', '}', ']', '~', '.']
digits = [str(digit) for digit in range(10)]
    

def main(args):
    valid = (len(args) == 2) and args[1].isdigit()
    if not valid:
        print("usage: pass_gen password_length")
        exit()

    length = int(args[1])
    if not validLength(length):
        print("Invalid password length entered. Length should be between 8 and 30.")
        exit()
    
    password = ""
    for _ in range(length):
        random_char = random.choice(character)
        if random_char == 'UPPERCASE':
            password += random.choice(upper_a)
        elif random_char == 'LOWERCASE':
            password += random.choice(lower_a)
        elif random_char == 'SYMBOLS':
            password += random.choice(symbols)
        else:
            password += random.choice(digits)
    
    print(password)
    

# Returns true if length is between 8 and 30 inclusive
def validLength(length):
    return 8 <= length <= 30


if __name__ == "__main__":
    main(sys.argv)