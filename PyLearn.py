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





 