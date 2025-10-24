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

#---------------------------------------------------------------------------------------------# 
#find max from unsorted list

# a = [1, 4, 7, 12, 6, 8]

# max_val = a[0]  

# for i in range(1, len(a)):
#     if a[i] > max_val:
#         max_val = a[i]

# print(max_val)

#find min from unsorted list
# a = [1, 4, 7, 12, 6, 8]

# min = a[0]

# for i in range(0,len(a)):
#     if a[i] <= min:
#         min = a[i]
    
# print(min)

#find sum of all elemsts in a unsorted list

# a = [1, 4, 7, 12, 6, 8]

# sum = 0

# for i in range(0,len(a)):
#     sum += a[i]

# print(sum)

# Avg of all elements in a unsorted list

# a = [1, 4, 7, 12, 6, 8]

# sum = 0

# for i in range(0,len(a)):
#         sum += a[i]

# avg = sum / 2

# print(avg)
# --------------------------------------------------------------------------------#
# Count Vowels in a Word 📝
# Input: "python"
# Output: 1.
# Input: "education"
# Output: 5.

# Vowels = ["a","e","i","o","u"]
# word = []
# word = input("Enter Your Word: ")
# word = word.lower()

# count = 0
# for i in word:
#     for v in Vowels:
#         if i == v:
#             count += 1

# print(f"Your Word has {count} Vowels in It")
#------------------------------------------------------------------_________________________#
# #Factorial Calculator ✖️
# Input: 5
# Output: 120 (5*4*3*2*1).

# number = int(input("Enter your number for factorial: "))


# factorial = 1


# for i in range(1, number + 1):
#     factorial *= i

# print(f"The factorial of {number} is {factorial}")

#Reverse array 

# arr = [1, 2, 3, 4, 6, 8]
# brr = []


# for i in range(len(arr)-1, -1, -1):
#     brr.append(arr[i])

# print(brr)  
# ---------------------------------------------------------------#

#Enter a number in a sorted list

# arr = [2,4,6,12,18,22]
# num = 8


# for i in range(len(arr)):
#     if num < arr[i]:
#         arr.insert(i, num)
#         break
# else:
#     arr.append(num)  

# print(arr) 
# --------------------------------------------------------------#

# Check if list is sorted 


# arr = [1, 4, 5, 3, 2]

# for i in range(0, len(arr) - 1):  # Note: -1 here!
#     if arr[i] > arr[i + 1]:
#         print("Not sorted")
#         break
# else:
#     print("Sorted")  

#-----------------------------------------------------------------------------------#

# -ve on left side +ve on right side

# arr = [-1,2,4,6,-2,-4,5,-3]


# negative = []
# positive = []
# final_Array = []

# for i in range(0 ,len(arr)):
#     if arr[i] < 0 :
#         negative.append(arr[i])
#     else : 
#         positive.append(arr[i])

# final_Array = negative + positive

# print(final_Array)

# --------------------------------------------------------------------------#

# Second Largest Number in List

# Input: [10, 20, 4, 45, 99]

# Output: 45.
# (Without using sorted() directly — try loops!)

# arr = [10, 20, 4, 45, 99]
# n = len(arr)

# # Bubble sort to sort the array
# for i in range(n):
#     for j in range(0, n-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]

# print("Sorted array:", arr)  # [4, 10, 20, 45, 99]

# # Second largest is the second last element
# second_largest = arr[-2]
# print("Second largest number:", second_largest)  # Output: 45

#------------------------------------------------------------------------------------------------#

# Write a program to insert an element at the end of a list.
# Example: [1,2,3], insert 4 → [1,2,3,4].

# arr = [1,2,3]

# arr.append(4)

# print(arr)

#----------------------------------------------#

# Delete an element from a list by value.
# Example: [10,20,30], delete 20 → [10,30].


# arr = [10,20,30] 

# arr.remove(20)

# print(arr)

#-----------------------------------------------------#

# Find the sum of all elements in an array without using sum().

# arr =[1,3,5,7,12,3]

# sum = 0

# for i in arr:
#     sum += i 

# print(sum) 


# ----------------------------------------------------------- #

# Write a program to reverse a list using a loop (not [::-1]).

# listt = ["D","O","G"]

# newlist = []
# n = len(listt) 
# for i in range(n-1 ,-1, -1):
#     newlist.append(listt[i])

# result = ' '.join(newlist)
# print(result)

#-------------------------------------------------------------------------------_#

# Implement Linear Search:

# Input: [10, 30, 50, 70], search 50.

# Output: Found at index 2.

# If not found, print "Not found".

# arr = [10, 30, 50, 70]
# target = 50
# n = len(arr)
# found = False

# i = 0
# while i < n:
#     if arr[i] == target:
#         print(f"Found at index {i}")
#         found = True
#         break  
#     i += 1  

# if not found:
#     print("Not found")

#----------------------------------------------------------------------------------__#

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# class Solution:
#     def twoSum(self, nums, target):
#         n = len(nums)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]  
#         return []  


# nums = [2, 7, 11, 15]
# target = 9
# solution = Solution()
# result = solution.twoSum(nums, target)
# print(result)  
                    
#Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).


# class Solution(object):
#     def removeDuplicates(self, nums):
#         n = len(nums)
#         j = 1
#         for i in range(1,n):
#                 if nums[i] != nums[i-1]:
#                    nums[j] = nums[i]
#                    j += 1
        
#         return j
    

# nums = [0,0,1,1,1,2,2,3,3,4]

# solution = Solution()
# result = solution.removeDuplicates(nums)
# print(result) 
                

# ---------------------------------------------------------------------------------------# 
# 
# Best Time to Buy and Sell Stock II 
#You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.

# Example 2:

# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.

# Example 3:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.



# class Solution(object):
#     def maxProfit(self, prices):
#         n = len(prices)
#         Max_profit = 0
#         for i in range(0,n-1):
#             if prices[i] < prices[i+1]:
#                 Max_profit += prices[i+1] - prices[i]     
               

#         return Max_profit 




# prices =[7,1,5,3,6,4]
# solution = Solution()
# result = solution.maxProfit(prices)
# print(result) 

#------------------------------------------------------------------------------------------#

# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.


# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# class Solution(object):
#     def rotate(self, nums, k):
#         n = len(nums)
#         k = k % n  

#          # here if K = nums.insert(0, x) is O(n) (because shifting all elements to the right).

#             # nums.pop(-1) is O(1).

#             # So each loop = O(n).

#             # Total = O(n × k).

#             # n (length of nums) can be up to 100,000.

#              # k can also be up to 100,000.

#             # Worst case = 100,000 × 100,000 = 10^10 operations → far too slow, time limit exceeded
#         # for i in range(k):
#         #     nums.insert(0, nums[-1])
#         #     nums.pop(-1)
#         # print(nums)
#         temp = nums[-k:]      
#         rest = nums[:-k]       
#         nums[:] = temp + rest 

#         print(nums)
            
                
# nums = [-1,-100,3,99]
# k = 2
# solution = Solution()
# solution.rotate(nums,k)

#------------------------------------------------------------------------------------------#
#                                        Contains Duplicate
#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.


# class Solution(object):
#     def containsDuplicate(self, nums):
#         nums.sort() #for large array's
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i-1]:
#                 return True
#         return False

                
       

# nums = [1,2,3,4]
# solution = Solution()
# results=solution.containsDuplicate(nums)
# print(results)

        
#------------------------------------------------------------------------------------------#
#                                       Single Number
#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# #Example 1:

# Input: nums = [2,2,1]

# Output: 1

# Example 2:

# Input: nums = [4,1,2,1,2]

# Output: 4

# class Solution(object):
#     def singleNumber(self, nums):
#         nums.sort()
#         n = len(nums)
#         i = 0
        
#         while i < n - 1:     
#             if nums[i] != nums[i+1]:
#                 return nums[i]
#             i += 2           
        
#         return nums[-1]      
        

# nums =  [2,2,1]
# solution = Solution()
# print(solution.singleNumber(nums))  
#------------------------------------------------------------------------------------------#
#                                  Intersection of Two Arrays II
#Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# class Solution(object):
#     def intersect(self, nums1, nums2):
#         intersection = []
       
#         for i in range(0,len(nums1)):
#             for j in range(0,len(nums2)):
#                 if nums1[i] == nums2[j]:
                    
#                     intersection.append(nums1[i]) 
#                     nums2.pop(j)
#                     break
                     
        
#         return intersection
        
# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
# solution = Solution()
# print(solution.intersect(nums1,nums2))  
                  
#------------------------------------------------------------------------------------------#
#                                       Plus One
#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

 

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].


# class Solution(object):
#     def plusOne(self, digits):
#          number = int("".join(map(str, digits))) 
#          number = number + 1 
#          digits = list(map(int, str(number)))
         
#          return digits 
# digits = [1, 2, 3]
# solution = Solution()
# print(solution.plusOne(digits)) 
        
#------------------------------------------------------------------------------------------#
#                                             Move Zeroes

# Given an integer array nums, move all 0's to the end of it while maintaining the relative
#  order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# class Solution(object):
#     def moveZeroes(self, nums):
#         j = 0  # index for next non-zero
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[j] = nums[i]
#                 j += 1

#         # fill remaining with zeros
#         for k in range(j, len(nums)):
#             nums[k] = 0

#         return nums

# nums = [0,0,1]
# solution = Solution()
# print(solution.moveZeroes(nums))  # [1,3,12,0,0] 
#------------------------------------------------------------------------------------------#
#                                      Maximum Subarray

#Given an integer array nums, find the  with the largest sum, and return its sum.


# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
                                   
# class Solution:
#     def maxSubArray(self, nums):
#         maxSub, curSum = nums[0], 0
#         for num in nums:
#             if curSum < 0:
#                 curSum = 0
#             curSum += num
#             maxSub = max(maxSub, curSum)
#         return maxSub

   
#                          Pattern
# Example 1:
# Input: N = 3
# Output: 
# * * *
# * * *
# * * *

# m = input("Give n: ")
# m = int(m)

# for i in range(m):
#     for j in range(m):
#         print("*", end="")  # Print star without newline
#     print()  # Print newline after each row


# Input Format: N = 3
# Result: 
# * 
# * * 
# * * *
       

# n = input("Give N: ")
# n = int(n)

# for i in range(1,n+1):
#       print("*" * i )

# Input Format: N = 3
# Result: 
# 1
# 1 2 
# 1 2 3


# n = input("Give N: ")
# n = int(n)
# for i in range(1, n+1):
#     for j in range(1, i+1):  # Change: j goes from 1 to i+1
#         print(j, end=" ")     # Added space for better formatting
#     print()

# Input Format: N = 6
# Result:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6


# n = input("Give N: ")
# n = int(n)

# for i in range(1,n+1):
#     print(f"{i}" * i)


# Input Format: N = 3
# Result: 
# * * *
# * * 
# *


# n = input("Give N: ")
# n = int(n)

# for i in range(n,0,-1):
#       print("*" * i )

# Input Format: N = 3
# Result: 
# 1 2 3
# 1 2
# 1

# n = input("Give N: ")
# n = int(n)
# for i in range(n,0,-1):
#     for j in range(1, i+1):  # Change: j goes from 1 to i+1
#         print(j, end=" ")     # Added space for better formatting
#     print()

# Input Format: N = 3
# Result: 
#   *  
#  *** 
# ***** 


# n = int(input("Enter number of rows: "))

# for i in range(1, n+1):
#     # Print leading spaces
#     spaces = n - i
#     print(" " * spaces, end="")
    
#     # Print stars
#     stars = 2 * i - 1
#     print("*" * stars)


# Input Format: N = 3
# Result: 
# *****  
#  ***
#   *   

# n = int(input("Enter no of Rows: "))

# for i in range(n,0,-1):
#     spaces = n - i
#     print(" " * spaces, end="")


#     # Print stars
#     stars = 2 * i - 1
#     print("*" * stars)


# Input Format: N = 3
# Result: 
#   *  
#  ***
# ***** 
# *****  
#  ***

# n = int(input("Enter number of rows: "))

# for i in range(1, n+1):
#     if i <= n:
#         # Print leading spaces
#         spaces = n - i
#         print(" " * spaces, end="")
        
#         # Print stars
#         stars = 2 * i - 1
#         print("*" * stars)
# else :
#     for i in range(n,0,-1):
#         spaces = n - i
#         print(" " * spaces, end="")


#         # Print stars
#         stars = 2 * i - 1
#         print("*" * stars)

# Print 1 to N using Recursion


# def recursion(x,n):
#         if x <=n:
#             print(x)
#             recursion(x+1,n)
#         else: return

# n = int(input("What's The Limit: "))
# x = 1
# call = recursion(x,n)

# Hashing

# arr = [1,2,5,6,3,2,2,1]
# length=len(arr)

# max_val = max(arr)
# hash_1 = [0] * (max_val + 1) 

# for i in arr:
#     hash_1[i] +=1

# print(arr)
# n = int(input("Enter Which Number you want to see!: "))

# if n in arr:
#     print(hash_1[n])
# else:print("Number not present in list")


# s = ['a','e','a','a','f','r','e','f']

# h = [0] * 26
# for i in s:
#     ascii_value = ord(i)
#     Index = ascii_value - 97 
#     h[Index] += 1
# print(s)
# n = input("Frequency of which Character: ")

# if n in s:
#     Value = ord(n)
#     Indexx = Value - 97
#     print(h[Indexx])
# else: print("The Character Not Present in List")


# Count frequency of each element in the array  [AzDsa]

# Example 1:
# Input: arr[] = {10,5,10,15,10,5};
# Output: 10 3 
#         5  2 
#         15 1

# Explanation: 10 occurs 3 times in the array
# 	      5 occurs 2 times in the array
#               15 occurs 1 time in the array


# num = [2,2,3,4,4,2]


# max_val = max(num)
# h = [0] * (max_val + 1)

# for i in num:
#     h[i] +=1


# for j in range(0,len(h)):
#     if h[j] == 0:
#         continue
#     else: print(f"{j} {h[j]}")


# Find the highest/lowest frequency element  AZ dsa


# num = [2,2,3,4,4,2]

# max_val = max(num)
# h = [0] * (max_val + 1)


# for i in num:
#     h[i] += 1

# max_freq = 0
# max_element = 0

# for j in range(len(h)):
#     if h[j] > max_freq:
#         max_freq = h[j]
#         max_element = j


# min_freq = max(h) + 1  
# min_element = 0

# for k in range(len(h)):
#     if h[k] > 0 and h[k] < min_freq:  
#         min_freq = h[k]
#         min_element = k

# print(f"Highest Element: {max_element}, Highest Frequency: {max_freq}")
# print(f"Lowest Element: {min_element}, Lowest Frequency: {min_freq}")

# Selection Sort Algorithm A2Z DSA
# Example 1:
# Input: N = 6, array[] = {13,46,24,52,20,9}
# Output: 9,13,20,24,46,52
# Explanation: After sorting the array is: 9, 13, 20, 24, 46, 52

# nums = [13,46,24,52,20,9]


# for i in range(1,len(nums)):
#     for j in range (0,len(nums)-1):
#         if nums[i] < nums[j]:
#             Temp = nums[j]
#             nums[j] = nums[i]
#             nums[i] = Temp
# print(nums)


# Bubble Sort 
#                        n = 6  , n -2 = 4
#       0  1  2  3  4  5  
# nums = [13,46,24,52,20,9]

# n =len(nums)
# for i in range(n-2,-1,-1):
#     for j in range(0,i+1):
#         if nums[j]>nums[j+1]:
#             nums[j],nums[j+1] = nums[j+1],nums[j]

# print(nums)

# Insertion Sort       
            
# Example 1:
# Input: N = 6, array[] = {13,46,24,52,20,9}
# Output: 9,13,20,24,46,52

# def insertion_sort(nums):
#     n = len(nums)
    
#     # Start from second element (index 1)
#     for i in range(1, n):
#         key = nums[i]  # Current element to be inserted
#         j = i - 1      # Last index of sorted portion
        
#         # Move elements greater than key one position right
#         while j >= 0 and nums[j] > key:
#             nums[j + 1] = nums[j]  # Shift right
#             j -= 1
        
#         # Insert key at correct position
#         nums[j + 1] = key
    
#     return nums

# Test with your example
# nums = [13, 46, 24, 52, 20, 9]
# print("Original:", nums)
# result = insertion_sort(nums)
# print("Sorted:", result)

# def mergeSort(arr):
#   if len(arr) <= 1:
#     return arr

#   mid = len(arr) // 2
#   leftHalf = arr[:mid]
#   rightHalf = arr[mid:]

#   sortedLeft = mergeSort(leftHalf)
#   sortedRight = mergeSort(rightHalf)

#   return merge(sortedLeft, sortedRight)

# def merge(left, right):
#   result = []
#   i = j = 0

#   while i < len(left) and j < len(right):
#     if left[i] < right[j]:
#       result.append(left[i])
#       i += 1
#     else:
#       result.append(right[j])
#       j += 1

#   result.extend(left[i:])
#   result.extend(right[j:])

#   return result

# mylist = [3, 7, 6, -10, 15, 23.5, 55, -13]
# mysortedlist = mergeSort(mylist)
# print("Sorted array:", mysortedlist) 


# Bubble Sort  recursively
# def bubble_sort_recursive(nums, n=None):
#         n = len(nums)
    
#     if n <= 1:
#         return nums
       
#     swapped = False
#     for i in range(n-1):
#         if nums[i] > nums[i+1]:
#             nums[i], nums[i+1] = nums[i+1], nums[i]
#             swapped = True    
    
#     return bubble_sort_recursive(nums, n-1)


# nums = [13,46,24,52,20,9]
# result = bubble_sort_recursive(nums)
# print(result) 



                                            # #Arrays  A2Z 


# Find the Largest element in an array
# xample 1:
# Input: arr[] = {2,5,1,3,0};
# Output: 5
# Explanation: 5 is the largest element in the array. 

# Example2: 
# Input: arr[] = {8,10,5,7,9};
# Output: 10
# Explanation: 10 is the largest element in the array. 

#Brute Force and luckily the optimal too Cheers!
# def LargestElement(nums):

#     largestelement = nums[0]
#     n = len(nums)
#     i = 0
#     while i < n:
#         if nums[i] > largestelement:
#             largestelement = nums[i]

#         i +=1
#     return largestelement 

# nums =[2,1,5,3,0]
# print(LargestElement(nums))


# Find Second Smallest and Second Largest Element in an array
# Example 1:
# Input: [1,2,4,7,7,5]
# Output: Second Smallest : 2
# 	Second Largest : 5


# def Secondlargest(nums):
#     if len(nums) < 2:
#         return None 

#     n = len(nums)
#     largest = float("-inf")
#     Slargest = float("-inf")
#     for i in range(0,n):
#         if nums[i] > largest:
#             Slargest = largest
#             largest = nums[i]
#         elif nums[i] > Slargest and nums[i] != largest:
#             Slargest = nums[i]    
#     return Slargest


# nums = [1,2,4,7,7,5]
# print(Secondlargest(nums))

# Check if an Array is Sorted

# Example 1:
# Input: N = 5, array[] = {1,2,3,4,5}
# Output: True.
# def check(nums):
#     n = len(nums)
#     break_count = 0
    
#     for i in range(n):
#         if nums[i] > nums[(i + 1) % n]:
#             break_count += 1
    
#     return break_count <= 1


# Remove Duplicates in-place from Sorted Array


# class Solution(object):
#     def removeDuplicates(self, nums):
#         if not nums:
#             return 0
        
#         i = 0  # Slow pointer
        
#         # Read Explination to better Understand
#         for j in range(1, len(nums)):  # Fast pointer

#             if nums[j] != nums[i]:  #are they unique?

#                 i += 1  # When we find nums[j] != nums[i], it means: nums[i] = the last unique element we placed, We need to place nums[j] at the NEXT position after i

#                 nums[i] = nums[j]  # Place unique element there
        
#         return i + 1

# # Test
# solver = Solution()
# nums = [0,0,1,1,1,2,2,3,3,4]
# k = solver.removeDuplicates(nums)
# print(f"New length: {k}")
# print(f"Modified array: {nums[:k]}")


# class Solution(object):
#     def rotate(self, nums, k):
#         n = len(nums)
#         k = k % n   # why modulos? , it removes the useless complete rotations and keeps only what actually matters!
#         temp = nums[-k:]    # Slice the list from The k   
#         rest = nums[:-k]    # Slice the list to k
#         nums[:] = temp + rest  # merge the slices

#         print(nums)
            
                
# nums = [-1,-100,3,99]
# k = 2
# solution = Solution()
# solution.rotate(nums,k)


# #optimal:-  
#         n=len(nums)
#         k=k%n # why modulos? , it removes the useless complete rotations and keeps only what actually matters!
#         nums[:] = nums[-k:] + nums[:-k]
#         return nums
            


# class Solution(object):
#     def missingNumber(self, nums):
#         n = len(nums)
#         # complete_set = set(range(n + 1))  # {0,1,2,3}
#         # nums_set = set(nums)              # {0,1,3}
#         missing = set(range(n + 1)) - set(nums) # {2}
#         return list(missing)[0]           # 2

#  Max Consecutive Ones

# class Solution(object):
#     def findMaxConsecutiveOnes(self, nums):
#         max_count = 0
#         current_count = 0
        
#         for num in nums:
#             if num == 1:
#                 current_count += 1
#                 max_count = max(max_count, current_count)
#             else:
#                 current_count = 0  # Reset when we hit 0
                
#         return max_count

# class Solution(object):
#     def singleNumber(self, nums):
#         nums.sort()
#         n = len(nums)
#         i = 0
        
#         while i < n - 1:     
#             if nums[i] != nums[i+1]:
#                 return nums[i]
#             i += 2           
        
#         return nums[-1]      
        

# def longestSubarrayWithSumK(arr, k):
#     n = len(arr)
#     max_length = 0
    
#     for i in range(n):
#         current_sum = 0
#         for j in range(i, n):
#             current_sum += arr[j]  # Add current element to running sum
            
#             if current_sum == k:
#                 max_length = max(max_length, j - i + 1)
    
#     return max_length


# 2sum:- 
 

# class Solution:
#     def twoSum(self, nums, target):
#         n = len(nums)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]  
#         return []  

# Sort colors


# #Not Optimal O(n2); --
# class Solution(object):
#     def sortColors(self, nums):
#         n = len(nums)
#         count = [0]*3
        
#         # Counting occurrences of 0, 1, 2
#         for num in nums:
#             count[num] += 1
        
#         # Overwrite nums using the counters
#         idx = 0
#         for i in range(3):
#             for j in range(count[i]):
#                 nums[idx] = i
#                 idx += 1


# # Optimal :- 

# class Solution(object):
#     def sortColors(self, nums):
#         count = [0]*3
        
#         # Counting occurrences of 0, 1, 2
#         for num in nums:
#             count[num] += 1

#         R,W,B = count # Unpacking

#         nums[:R] = [0] * R
#         nums[R:R+W] = [1] * W
#         nums[R+W:] = [2] * B
 

# class Solution(object):
#    def majorityElement(self, nums):
#     count = {}  # Empty dictionary
    
#     # Count each number
#     for num in nums:
#         if num in count:
#             count[num] += 1      # Increment if exists
#         else:
#             count[num] = 1       # Initialize if new
    
#     # Find number with highest count
#     max_count = 0
#     result = nums[0]
    
#     for item, key in count.items():
#         if key > max_count:
#             max_count = key
#             result = item
    
#     return result

    
# nums = [2,2,1,1,1,2,2]
# solution = Solution()
# result = solution.majorityElement(nums)
# print(result)

# class Solution(object):
#     def maxProfit(self, prices):
#         min_price = float('inf')
#         max_profit = 0
        
#         for price in prices:
#             if price < min_price:
#                 min_price = price  # update min price so far
#             else:
#                 profit = price - min_price
#                 if profit > max_profit:
#                     max_profit = profit  # update max profit
          
#         return max_profit



# nums = [7,1,5,3,6,4]
# solution = Solution()
# result = solution.maxProfit(nums)
# print(result)

# class Solution(object):
#     def rearrangeArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         # the index for the array will be categorized in odd and even .
#         array = [0] * len(nums)
#         even_idx, odd_idx = 0, 1

#         for num in nums:
#             if num > 0:
#                 array[even_idx] = num
#                 even_idx += 2
#             else:
#                 array[odd_idx] = num
#                 odd_idx += 2

#         return array
    
# nums = [3,1,-2,-5,2,-4]
# solution = Solution()
# result = solution.rearrangeArray(nums)
# print(result)


# find Cpnsective elemts
# Input: [100, 200, 1, 3, 2, 4]

# class Solution(object):
#     def longestConsecutive(self, nums):
#         if not nums:  # empty list check
#             return 0
        
#         nums.sort()
#         max_count = 1
#         count = 1
        
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i-1]:  # skip duplicates
#                 continue
#             elif nums[i] == nums[i-1] + 1:  # consecutive
#                 count += 1
#             else:  # sequence broken
#                 max_count = max(max_count, count)
#                 count = 1
                
#         max_count = max(max_count, count)
#         return max_count


# nums = [100, 200, 1, 3, 2, 4]
# solution = Solution()
# result = solution.longestConsecutive(nums)
# print(result)               '''


# Set Matrix Zeroes

# class Solution(object):
#     def setZeroes(self, matrix):
#         if not matrix or not matrix[0]:
#             return
#         m, n = len(matrix), len(matrix[0])
#         first_row_zero = any(matrix[0][j] == 0 for j in range(n))
#         first_col_zero = any(matrix[i][0] == 0 for i in range(m))

#         # Mark zeros in first row and column
#         for i in range(1, m):
#             for j in range(1, n):
#                 if matrix[i][j] == 0:
#                     matrix[i][0] = 0
#                     matrix[0][j] = 0

#         # Zero rows based on marks
#         for i in range(1, m):
#             if matrix[i][0] == 0:
#                 for j in range(1, n):
#                     matrix[i][j] = 0

#         # Zero columns based on marks
#         for j in range(1, n):
#             if matrix[0][j] == 0:
#                 for i in range(1, m):
#                     matrix[i][j] = 0

#         # Zero first row and first column if needed
#         if first_row_zero:
#             for j in range(n):
#                 matrix[0][j] = 0
#         if first_col_zero:
#             for i in range(m):
#                 matrix[i][0] = 0

# row addition one row at a time
# matrix = [
#  [1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]
# ]
# sum= 0
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         sum += matrix[i][j]
#     print (sum)
#     sum = 0

# coloum adddition one at a time 

# matrix = [
#  [1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]
# ]
# sum= 0
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         sum += matrix[j][i]
        
#     print (sum)
#     sum = 0

# matrix = [
#  [1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]
# ]

# # Find max in each row
# for i in range(len(matrix)):
#     row_max = matrix[i][0]  # start with first element in the row
#     for j in range(len(matrix[0])):
#         if matrix[i][j] > row_max:
#             row_max = matrix[i][j]
#     print(f"Max Value in Row {i}: {row_max}")

# print()  # just to separate row and column output

# # Find max in each column
# for m in range(len(matrix[0])):
#     col_max = matrix[0][m]  # start with first element in the column
#     for n in range(len(matrix)):
#         if matrix[n][m] > col_max:
#             col_max = matrix[n][m]
#     print(f"Max Value in Col {m}: {col_max}")

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# class Solution(object):
#     def setZeroes(self, matrix):
#         row = set()
#         col = set()
        
#         # Step 1: Find all rows and columns with a zero
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if matrix[i][j] == 0:
#                     row.add(i)
#                     col.add(j)
        
#         # Step 2: Zero out the rows and columns
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if i in row or j in col:   # see here only i  will at first postion for that row (i,j) here i is at first only for this row i.e (2,1) 
#                     matrix[i][j] = 0


# matrix =[[5,1,9,11],
#          [2,4,8,10],
#          [13,3,6,7],
#          [15,14,12,16]]

# n,m = len(matrix),len(matrix[0])

# for i in range(n):
#     for j in range(i+1, m):  # upper triangle only
#         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# for row in matrix:
#             row.reverse()

# print(matrix)

# class Solution(object):
#     def spiralOrder(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: List[int]
#         """
#         result = []
#         if not matrix: return result

#         top, bottom = 0, len(matrix)-1
#         left, right = 0, len(matrix[0])-1

#         while left <= right and top <= bottom:
#             for j in range(left, right+1):
#                 result.append(matrix[top][j])
#             top += 1

#             for i in range(top, bottom+1):
#                 result.append(matrix[i][right])
#             right -= 1

#             if top <= bottom:
#                 for j in range(right, left-1, -1):
#                     result.append(matrix[bottom][j])
#                 bottom -= 1

#             if left <= right:
#                 for i in range(bottom, top-1, -1):
#                     result.append(matrix[i][left])
#                 left += 1

#         return result
# class Solution(object):
#     def findMaxConsecutiveOnes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         c_count = p_count = 0
#         for i in range(len(nums)):
#             if nums[i] == 1:
#                 c_count += 1
#                 p_count = max(c_count,p_count)
#             else : c_count = 0
#         return max(p_count,c_count)