"""
LeetCode Problem #: 001
Title: Two Sum
Difficulty: [Easy]
URL: https://leetcode.com/problems/two-sum/

📝 Problem:
Given an array of integers `nums` and an integer `target`, return the indices 
of the two numbers such that they add up to target.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        seen = {} # This dictionary will store numbers we have seen so far and their indexes.

        for i, num in enumerate(nums):        # enumerate gives both index (i) and value (num)
            complement = target - num         # This is the number we need to reach the target
            if complement in seen:            # Check if that needed number was already seen
                return [seen[complement], i]  # Return the index of the complement and current number
            seen[num] = i                     # Otherwise, store the current number and its index in the dictionary.