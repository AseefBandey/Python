# import random 
# def get_input():
#     player = input("Chose Between Rock,Paper,Sissors :")

#     inputs = ['Rock','Paper','Sissors']

#     computer = random.choice(inputs)

#     return player,computer

# def game(player,computer):
#     if player == computer:
#         print('Its a Tie')
#     elif player == 'Rock':
#         if computer == 'Sissors':
#             print('Rock smashes Sissors! You Win')
#         elif computer == 'Paper':
#             print('Paper Covers Rock! You loose')

#     elif player == 'Sissors':
#         if computer == 'Paper':
#             print('Sissors cuts Paper! You Win')
#         elif computer == 'Rock':
#             print('Rock smashes Sissors! You loose')

#     elif player == 'Paper':
#         if computer == 'Rock':
#             print('Paper covers Rock! You Win')
#         elif computer == 'Sissors':
#             print('Sissors cuts Paper! You loose')
    

# player, computer = get_input()   # unpack values :--- When a function returns multiple values in Python, it actually returns a tuple. Unpacking means splitting that tuple into separate variables. Here Above it return Player and computer, which isnt in scope here line 33 there fore we unpack the tuple and assign them to player and computer *Respectively*
# print(f"You chose: {player}, Computer chose: {computer}")
# game(player, computer)

# print 
# Elements row by row



# # print by Colum
# array = [[1,2,3],[4,5,6],[7,8,9]]


# for col in range(3):
#     for row in range(3):
#         print(array[row][col], end=" ")
        
#     print()

#"Hello <name>, you will be <age+1> years old next year!"

# arr = [10, 20, 30, 40, 50, 60]

# for i in arr:
#     if i == 50:
#         a = 1
#     else:
#         b = 0

# if a == 1:
#     print("Found")
# elif b == 0:
#     print("Not found") 

# arr = [2, 4, 6, 8]

# arr.append(10)

# print(arr)

# sum = 0

# for i in arr:
#     sum += i 
# print(sum)

arr = [10, 20, 30, 40, 30, 50]

[print(i) for i in arr] 
