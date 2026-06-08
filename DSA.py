# 1. Write a function that takes a list of numbers and returns only the even numbers.

# def get_even_numbers(numbers):
#     return [i for i in numbers if i%2==0]
# # Example
# print(get_even_numbers([1, 2, 3, 4, 5, 6]))
# # Expected output: [2, 4, 6]

# 2. Write a function that takes a string and returns a dictionary with each word and how many times it appears.
# def word_frequency(sentence):
#     words = sentence.split()
#     dic = {}

#     for word in words:
#         if word not in dic:
#             dic[word] = 1
#         else:
#             dic[word] += 1
#     return dic

# # Example
# print(word_frequency("the cat sat on the mat the cat"))
# Expected output: {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}



"""
Problem 3 — FizzBuzz
A classic interview problem. Write a function that takes a number n and prints:

"Fizz" if the number is divisible by 3
"Buzz" if the number is divisible by 5
"FizzBuzz" if divisible by both 3 and 5
The number itself if none of the above
"""

# def fizzbuzz(n):
#     for i in range(1, n + 1):
#         if i % 3 == 0 and i % 5 == 0:  # check this FIRST
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)

# fizzbuzz(15)



"""
Replace Elements With Greatest Element On Right Side
Easy
Topics
Company Tags
You are given an array arr, replace every element in that array with the greatest element among the elements to its right, 
and replace the last element with -1.

After doing so, return the array.

Example 1:

Input: arr = [2,4,5,3,1,2]

Output: [5,5,3,2,2,-1]

"""
# def replaceElement(arr):
#     output = []
#     for i in range(len(arr)):
#         if i == len(arr) - 1: # last digit
#             output.append(-1)
#         else:
#             output.append(max(arr[i + 1:]))
#     return output

# arr = [2,4,5,3,1,2]
# print(replaceElement(arr))


"""
🟢 Easy — Valid Parentheses
Problem:
Given a string s containing just the characters (, ), {, }, [, ], return True if the string is valid, False otherwise.
"""
# def valid_parenthese(s):
#     stack = []
#     matches= {")":"(", "}":"{", "]":"["}

#     for char in s:
#         if char in "({[":
#             stack.append(char)
#         elif char in ")}]":
#             if stack and stack[-1] == matches[char]:
#                 stack.pop()
#             else:
#                 return False
#     return len(stack) == 0


# print(valid_parenthese("(dfhdhfjkdf("))

"""
Problem:
Given an integer array nums, find the contiguous subarray which has the largest sum and return that sum.
Example 1:
Input:  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: [4, -1, 2, 1] has the largest sum = 6

# """
# def max_subarray(nums:list):
#     current_sum = 0
#     max_sum = float('-inf')
#     for num in nums:
#         current_sum = current_sum + num
#         max_sum = max(max_sum, current_sum)
#         if current_sum < 0: # yesma chai  k garirako xam vnya if current_sum less than 0 xa vnya teslai zero garayarw reset grya xa
#             current_sum = 0
#     return max_sum


# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(max_subarray(nums))

"""
Problem: Max Average Subarray
Given an integer array nums and an integer k, find the contiguous subarray of length k that has the maximum average value. Return that maximum average.
Example:
Input: nums = [1, 12, -5, -6, 50, 3], k = 4
Output: 12.75
Explanation: Subarray [12, -5, -6, 50] → average = 51/4 = 12.75
"""
# def Max_Avg_Sub(nums, k):
#     window_sum = sum(nums[:k])
#     max_sum = window_sum

#     for i in range(k, len(nums)):
#         window_sum += nums[i]
#         window_sum -= nums[i - k] # add new element on the right
#         max_sum = max(max_sum, window_sum) # remove old element on the left
#     return max_sum/k






# nums = [1, 12, -5, -6, 50, 3]
# k = 4
# print(Max_Avg_Sub(nums, k))


"""
Easy — Two Sum
Problem:
Given an array of integers nums and a target integer target, return the indices of the two numbers that add up to the target.
Example:
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9
Constraints:

Each input has exactly one solution
You cannot use the same element twice
"""
# def two_sum(nums, target):
#     result = []
#     for i in range(len(nums)):
#         for j in range(i + 1 ,len(nums)):
#             if nums[i] + nums[j] == target:
#                 result.append([i, j])
#     return result
        

# nums = [2, 7, 11, 15]
# target = 9
# print(two_sum(nums, target))


"""
 Easy — Contains Duplicate
Problem:
Given an integer array nums, return True if any value appears at least twice, and False if every element is distinct.
Example 1:
Input:  nums = [1, 2, 3, 1]
Output: True
Explanation: 1 appears twice
Example 2:
Input:  nums = [1, 2, 3, 4]
Output: False
Explanation: all elements are unique
"""
# def contain_duplucate(nums):
#     seen = set()
#     for i in range(len(nums)):
#         if nums[i] not in seen:
#             seen.add(nums[i])
#         else:
#             return True
#     return False

# nums = [1,2,3,4]
# print(contain_duplucate(nums))




"""
Easy — Best Time to Buy and Sell Stock
Problem:
You are given an array prices where prices[i] is the price of a stock on day i. 
You want to maximize your profit by choosing a single day to buy and a different day in the future to sell.
Return the maximum profit. If no profit is possible return 0.
"""

# # this is my code:
# def max_profit(prices):
#     min_price = float('inf')
#     max_profit = 0
#     for price in prices:
#         if price < min_price:
#             min_price = price
#         else:
#             max_profit = max(max_profit, price - min_price)
#     return max_profit

# This is from claude
# def max_profit(prices):
#     min_price = float("inf")
#     max_profit = 0
#     for price in prices:
#         min_price = min(min_price, price)
#         max_profit = max(max_profit, price - min_price)
#     return max_profit

# prices = [7, 1, 5, 3, 6, 4,10]
# print(max_profit(prices))




"""
🟢 Easy — Climbing Stairs
You were about to try this one. Here's the problem again:
Given n steps, you can climb 1 or 2 steps at a time. How many distinct ways can you reach the top?
n=2 → 2 ways
n=3 → 3 ways
n=5 → 8 ways

Give it a shot and paste your code! 💪🔥"""



# def Climbing_stairs(n):
#     if n <=2:
#         return n
    
#     prev2 = 1
#     prev1 = 2

#     for i in range(3, n + 1):
#         current = prev2 + prev1
#         prev2 = prev1
#         prev1 = current
#     return prev1

# n = 4
# print(Climbing_stairs(n))


"""
Next Up — Two Pointers 🔲
🟢 Easy — Valid Palindrome
Problem:
Given a string s, return True if it is a palindrome, False otherwise.
A palindrome reads the same forwards and backwards.
Example 1:
Input:  s = "racecar"
Output: True
"""

# def is_Palindrome(s):
#     left = 0
#     right = len(s) - 1

#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True

# print(is_Palindrome("racecar"))  # True
# print(is_Palindrome("hello"))    # False
# print(is_Palindrome("abba"))     # True


"""
Easy — Two Sum II (Sorted Array)
Problem:
Given a sorted array numbers and a target, return the indices of the two numbers that add up to target. Indices are 1-based (start from 1 not 0).
Example 1:
Input:  numbers = [2, 7, 11, 15], target = 9
Output: [1, 2]
Explanation: 2 + 7 = 9 → index 1 and index 2
"""

# def Two_sum(numbers, target):
#     output = []
    
#     for i in range(len(numbers)):
#         for j in range(i + 1, len(numbers)):
#             if numbers[i] + numbers[j] == target:
#                 output.append([i, j])
#     return output




# numbers = [2, 7, 11, 15]
# target = 9


# print(Two_sum(numbers, target))


# def two_sum(numbers, target):
#     left = 0
#     right = len(numbers) - 1

#     while left < right:
#         current_sum = numbers[left] + numbers[right]
#         if current_sum == target:
#             return [left + 1,  right + 1]
#         elif current_sum  > target:
#             right -= 1
#         else:
#             left += 1
#     return[]



# numbers = [2, 7, 11, 15]
# target = 9
# print(two_sum(numbers, target))


"""
🟢 Easy — Binary Search
Problem:
Given a sorted array nums and a target, return the index of target if it exists, otherwise return -1.
Example 1:
Input:  nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
Explanation: 9 is at index 4
"""
# def binary_search(nums, target):
#     left = 0
#     right = len(nums) - 1
#     while left <= right:
#         mid =(left + right) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid -1
#     return -1


# nums = [-1, 0, 9, 5, 12, 10]
# target = 9

# print(binary_search(nums, target))


# All patterns practice problems

# 1. Sliding window
"""
Max Consecutive Ones (Sliding Window)
Problem:
Given a binary array nums containing only 0s and 1s, return the maximum number of consecutive 1s.
Example 1:
Input:  nums = [1, 1, 0, 1, 1, 1]
Output: 3
Explanation: Last three 1s are the longest consecutive sequence
"""
# def Max_consecutive_ones(nums):
#     curren_count = 0
#     max_count = 0
    
#     for num in nums:
#         if num == 1:
#             curren_count += 1
#         else:
#             curren_count = 0
#         max_count = max(max_count, curren_count)
#     return max_count
 



# nums = [1, 1, 0, 1, 1, 1]
# print(Max_consecutive_ones(nums))


# 2. HashMap
"""
🟢 Easy — Ransom Note
Problem:
Given two strings ransomNote and magazine, return True if you can construct ransomNote using letters from magazine, False otherwise.
Each letter in magazine can only be used once.
Example 1:
Input:  ransomNote = "a", magazine = "b"
Output: False
"""


# def ransome_note(ransomNote, magazine):
#     count = {}


#     for char in magazine:
#         count[char] = count.get(char, 0) + 1 # counting pattern -- most important line! Yesma count.get(char, 0) == yes if char xa vnya 1 dinxa xaina vnya 0
    
#     for char in ransomNote:
#         if char not in count or count[char] == 0: # or mean kunai neh euta condition meet vaya pugxa
#             return False
#         count[char] -= 1
#     return True

# print(ransome_note("a", "b"))


# 3. Stack Pattern
"""
🟢 Easy — Min Stack (Stack Pattern)
Problem:
Design a stack that supports these operations in O(1) time:

push(val) — push element onto stack
pop() — remove top element
top() — get top element
getMin() — get minimum element in stack

Example:
MinStack minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin() → -3
minStack.pop()
minStack.top()    → 0
minStack.getMin() → -2
"""

# class Minstack:
#     def __init__(self):
#         self.stack = []
#         self.min_stack = []

#     def push(self, val):
#         self.stack.append(val)
#         if not self.min_stack or val <= self.min_stack[-1]:
#             self.min_stack.append(val)
#     def pop(self):
#         if self.stack[-1] == self.min_stack[-1]:
#             self.min_stack.pop()
#         self.stack.pop()

#     def top(self):
#         return self.stack[-1]
    
#     def getMin(self):
#         return self.min_stack[-1]
    




# minStack = Minstack()
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
# print(minStack.getMin())  # -3
# minStack.pop()
# print(minStack.top())     # 0
# print(minStack.getMin())  # -2


# 4. Binary search
"""
🟢 Easy — Search Insert Position (Binary Search)
Problem:
Given a sorted array nums and a target, return the index if target is found. If not, return the index where it would be inserted in order.
Example 1:
Input:  nums = [1, 3, 5, 6], target = 5
Output: 2
"""

# this is my solution
# def Search_insert_position(nums, target):
#     for i in range(len(nums)):
#         if nums[i] == target:
#             return nums[i]
#         else:
#             nums.insert(i + 1, target)
#             nums.sort()
#             return nums[i]
    
# nums = [1, 3, 5, 6]
# target = 7

# print(Search_insert_position(nums, target))

# def Search_insert_position(nums, target):
#     left = 0 # 1 round ma left 0 and depend on 1st loop, in 2nd round left will be different same goes to right also 
#     right = len(nums) - 1

#     while left <= right: # this loop will run every time once left and right get update
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return left



# nums = [1,3,5,6]
# target = 7
# print(Search_insert_position(nums, target))


"""
🟢 Easy — House Robber (Dynamic Programming)
Problem:
You are a robber planning to rob houses along a street. Each house has some money. You cannot rob two adjacent houses (alarm will trigger). Return the maximum amount you can rob.
Example 1:
Input:  nums = [1, 2, 3, 1]
Output: 4
Explanation: Rob house 1 (1) + house 3 (3) = 4
"""


def house_robber(nums):
    if len(nums) == 1: 
        return nums[0]
    
    prev2 = nums[0] # 1
    prev1 = max(nums[0], nums[1]) # (1.2) == 2

    for i in range(2, len(nums)):
        current = max(nums[i] + prev2, prev1)
        prev2 = prev1
        prev1 = current
    return prev1

print(house_robber([1, 2, 3, 1]))    # 4
print(house_robber([2, 7, 9, 3, 1])) # 12
