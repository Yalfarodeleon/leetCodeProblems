# 001. Two Sum

**Difficulty:** Easy  
**Link:** [LeetCode Link](https://leetcode.com/problems/two-sum/)

## 📝 Problem

> Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to target.

## 💡 Approach

- Use a hash map to store numbers and their indices
- For each number, check if its complement exists in the map

## 🔍 Time Complexity

- **O(n)** – We traverse the list once

## 🧠 Space Complexity

- **O(n)** – We use a dictionary to store up to n elements

## 🧪 Edge Cases

- Duplicates (e.g., `[3,3]`, target `6`)
- Negative numbers
- Minimum array length
