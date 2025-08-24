
import random 

def get_input():
    inputs = ['rock', 'paper', 'scissors']
    
    while True:
        player = input("Choose between Rock, Paper, Scissors: ").strip().lower()
        if player in inputs:
            break
        print("Invalid choice. Please try again.")
    
    computer = random.choice(inputs)
    return player, computer

def game(player, computer):
    print(f"You chose: {player.capitalize()}, Computer chose: {computer.capitalize()}")
    
    if player == computer:
        print('It\'s a Tie!')
    elif player == 'rock':
        if computer == 'scissors':
            print('Rock smashes Scissors! You Win!')
        else:  # computer == 'paper'
            print('Paper covers Rock! You Lose!')
    elif player == 'scissors':
        if computer == 'paper':
            print('Scissors cuts Paper! You Win!')
        else:  # computer == 'rock'
            print('Rock smashes Scissors! You Lose!')
    elif player == 'paper':
        if computer == 'rock':
            print('Paper covers Rock! You Win!')
        else:  # computer == 'scissors'
            print('Scissors cuts Paper! You Lose!')

# Play the game
player, computer = get_input()
game(player, computer)