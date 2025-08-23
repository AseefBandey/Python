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

# arr = [10, 20, 30, 40, 30, 50]

# [print(i) for i in arr] 

# ---------------------------------------------------------------------------

# Matrix Calculator

# Take two matrices from the user.

# Perform addition, subtraction, multiplication, transpose.

# Learn how broadcasting works.

#                    WITHOUT RECURSION
# def binary_search_iterative(arr, target):
#     low = 0
#     high = len(arr) - 1
#     print(len(arr)) # 7

#     while low <= high:     
#         mid = (low + high) // 2   

#         if arr[mid] == target:
#             return mid   
#         elif arr[mid] < target:
#             low = mid + 1   
#         else:
#             high = mid - 1  

#     return -1  


# # Example
#     #  0   1   2   3   4   5   6 
# arr = [5, 10, 15, 20, 25, 30, 35]
# target = 12
# print("Index:", binary_search_iterative(arr, target))

# def binary_search_recursive(arr, target, low, high):
#     if low > high:  # base case: not found
#         return -1

#     mid = (low + high) // 2   
#         return mid
#     elif arr[mid] < target:
#         return binary_search_recur

#     if arr[mid] == target:
#         return mid
#     elif arr[mid] < target:
#         return binary_search_recursive(arr, target, mid + 1, high)
#     elif arr[mid] > target:
#         return binary_search_recursive(arr, target, low, mid - 1)


# # Example
#     #  0   1   2   3   4   5   6 
# arr = [5, 10, 15, 20, 25, 30, 35]
# target = 35
# print("Index:", binary_search_recursive(arr, target, 0, len(arr)-1))

# Write a function to perform linear search in an array.
# Input: arr = [5, 10, 15, 20, 25], key = 20
# Output: 3 (index of 20)

# def linear_search(arr, key):
#     for i in range(0, len(arr)):  
#         if key == arr[i]:
#             return i 
#     return -1

# arr = [5, 10, 15, 20, 25]
# key = 20

# print(f"index: {linear_search(arr, key)}")

# Use binary search (iterative) to find the index of 42 in:
# arr = [10, 22, 30, 35, 40, 42, 55, 60]
# Output: 5

# def BinarySearch(arr,key):
#         low = 0
#         high = len(arr) -1 
#         while low <= high:
                
#                 mid = (low + high) // 2 

#                 if arr [mid] == key :
#                         return mid 
#                 elif arr [mid] < key :
#                         low = mid + 1
#                 elif arr [mid] > key :
#                         high = mid - 1
#         return -1 

# arr = [10, 22, 30, 35, 40, 42, 55, 60] 

# key = 42 

# print(f"Index {BinarySearch(arr,key)}")

# Given a sorted list of strings, use binary search (recursive) to find the word "dog".
# arr = ["ant", "bat", "cat", "dog", "elephant", "fox"]
# Output: 3

# def BinarySearch(arr,key):
#         low = 0
#         high = len(arr) -1 
#         while low <= high:
                
#                 mid = (low + high) // 2 

#                 if arr [mid] == key :
#                         return mid 
#                 elif arr [mid] < key :
#                         low = mid + 1
#                 elif arr [mid] > key :
#                         high = mid - 1
#         return -1 


# arr = ["ant", "bat", "cat", "dog", "elephant", "fox"]

# key = "dog" 

# print(f"Index {BinarySearch(arr,key)}")

# ------------------------------------------------------------------------------------------

# Example: arr = [1, 5, 7, 5, 9, 5], key = 5
# Output: [1, 3, 5]

# def linear_search(arr, key):
#     a = [] 
#     for i in range(0, len(arr)):  
#         if key == arr[i]:
#             a.append(i) 
#     return a

# arr = [1, 5, 7, 5, 9, 5]
# key = 5
# print(f"index: {linear_search(arr, key)}")

#Modify binary search to return the first occurrence of a number in a sorted array with duplicates.
#Example: arr = [2, 4, 4, 4, 6, 8], key = 4
# Output: 1

# def find_first_occurrence(arr, key):
#     low = 0
#     high = len(arr) - 1
#     result = -1  
    
#     while low <= high:
#         mid = (low + high) // 2
        
#         if arr[mid] == key:
#             result = mid  
#             high = mid - 1  
#         elif arr[mid] < key:
#             low = mid + 1
#         else:  
#             high = mid - 1
    
#     return result

# arr = [2, 4, 4, 4, 6, 8]
# key = 4
# print(f"First occurrence of {key}: {find_first_occurrence(arr, key)}")

# You are asked to build a simple simulator of the Magic 8 Ball toy. The user types a Yes/No question (like "Will I become good at Python?"), 
# and the program gives a random response from a fixed set of answers.

# import random
# question = input("What is Your Question, \nExample of a question:Will I become good at Python? \n")

# answer =["Yes", "No", "Maybe", "ahhh!idk,Probbaly nooo"]

# Output = random.choice(answer)

# if len(question) > 5 :
#     print(Output)
# else: print("Ask a Proper Question")

# Coin Toss Game 🪙

# Computer flips coin → Heads or Tails.

# User guesses before flip.

# import random

# userguess = input("Pick 1 or 2 ;  1.Heads or 2.Tails: ")
# UserGuess = userguess.strip().capitalize()

# choices = {1: "Heads", 2: "Tails"}
# CPU_choice = random.choice(list(choices.values()))

# # Convert user input to match the format
# if UserGuess == "1":
#     user_choice = "Heads"
# elif UserGuess == "2":
#     user_choice = "Tails"
# else:
#     user_choice = UserGuess  # if user typed "Heads" or "Tails" directly

# if CPU_choice == user_choice:
#     print("You won!")
# else:
#     print("You lose!")

# print(f"Your call: {user_choice}, and it is: {CPU_choice}")

