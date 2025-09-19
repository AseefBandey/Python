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

#--------------------------------------------------------------------------#

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# nums1 = [1,2]

# nums2 = [3,4]

# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         nums3 = nums1 + nums2  
#         nums3.sort()
#         n = len(nums3)
#         if n % 2 == 0:
#             mid1 = nums3[n//2 - 1]   
#             mid2 = nums3[n//2]       
#             return (mid1 + mid2) / 2.0
#         else:
#             return nums3[n//2]

# solution = Solution()
# result = solution.findMedianSortedArrays(nums1,nums2)
# print(result)        
        
#------------------------------Top-interview-questions-easy-----------------------------------------#

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
#   
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

# class Solution:
#     def twoSum(self, nums, target):
#         n = len(nums)
#         for i in range(n):
#             for j in range(1, n):
               
#                 if nums[i] + nums[j] == target:
#                     return [i, j]  
#         return []  


# nums = [1,2,1,3]
# target = 6
# solution = Solution()
# result = solution.twoSum(nums, target)
# print(result)  
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




