# Jumbled Word Game 🔤

# Program picks a word (e.g., "python").

# Shuffles letters ("tonyph").
# User tries to guess the correct word.

import random

all_words = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
    "jujube", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince",
    "raspberry", "strawberry", "tangerine", "ugli", "vanilla", "watermelon", "xigua",
    "yuzu", "zucchini", "apricot", "blackberry", "blueberry", "cantaloupe", "clementine"
]

pick_random = random.choice(all_words) 

print(pick_random)

string_list = list(pick_random)

random.shuffle(string_list)
shuffled_string = ''.join(string_list)

print(f"The word is : {shuffled_string}")

User_guess = input("Guess the Word:")

if User_guess == pick_random:
    print("You Gussed Right")
else : 
    print("You Guessed Wrong")


