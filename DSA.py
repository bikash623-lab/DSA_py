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
You are given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

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