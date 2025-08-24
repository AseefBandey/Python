import random
import string

def generatepassword(P_length):
    if P_length < 8:
        return "Password length must be at least 8 characters"
    
    alphabets = list(string.ascii_letters)
    characters = list(string.punctuation)
    numbers = list(string.digits)
    
    # Ensure at least one of each type
    password = [
        random.choice(alphabets),
        random.choice(characters),
        random.choice(numbers)
    ]
    
    # Fill the rest with random characters from all pools
    all_chars = alphabets + characters + numbers
    password += random.choices(all_chars, k=P_length-3)
    
    # Shuffle the password to mix the characters
    random.shuffle(password)
    
    return ''.join(password)

P_length = int(input("Enter Length of Your Password (min 8): "))
print(f"Your Password is: {generatepassword(P_length)}")
