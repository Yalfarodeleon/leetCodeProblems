# LeetCode Problem #020 - [Valid Parentheses]

**Difficulty:** [Easy]  
**Link:** [LeetCode URL](https://leetcode.com/problems/valid-parentheses/)

---

## 📝 Problem

> Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1.Open brackets must be closed by the same type of brackets.
2.Open brackets must be closed in the correct order.
3.Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

---

## 💡 Approach

- We use a **stack** to keep track of opening brackets as we iterate through the string.
- When we see a **closing bracket**, we:
  - Check if the stack is empty (no opener to match → invalid).
  - Pop from the stack and compare it to the expected opening bracket using a **dictionary (hash map)**.
- The dictionary helps match each closing bracket to its corresponding opener in **O(1)** time.
- At the end, if the stack is empty, the string is valid.

---

## 🔍 Time and Space Complexity

| Metric | Complexity | Notes |
|--------|------------|-------|
| 🕒 Time   | O(n)       | We traverse the string once |
| 🧠 Space  | O(n)       | In the worst case, we store all open brackets in the stack |

---

## ✅ Test Cases

| Input     | Output | Explanation                            |
|-----------|--------|----------------------------------------|
| `"()"`    | `True` | Balanced pair                          |
| `"()[]{}"`| `True` | All valid, sequential pairs            |
| `"(]"`    | `False`| Closing `]` doesn't match opening `(`  |
| `"([])"`  | `True` | Properly nested and closed             |
| `"("`     | `False`| Opening bracket without closing        |
| `"]"`     | `False`| Closing bracket without opening        |
| `"([)]"`  | `False`| Correct characters but wrong order     |

---

## 🧠 Notes & Learnings

- Learned how to implement a **stack** using Python lists with `append()` and `pop()`.
- Reinforced use of a **dictionary** for efficient bracket matching instead of long `if-else` chains.
- Practiced checking edge cases like unmatched openers or closers.
- `return not stack` at the end is a smart Pythonic way to check if everything matched.
- I now understand how the stack data structure enables **Last-In First-Out (LIFO)** logic, which is perfect for matching open/close pairs in order.

---
