
"""
Hints:
    Hint 1
        Use a stack of characters.
    Hint 2
        When you encounter an opening bracket, push it to the top of the stack.
    Hint 3
        When you encounter a closing bracket, check if the top of the stack was the 
        opening for it. If yes, pop it from the stack. Otherwise, return false.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # Need a list to implement stack and track opening brackets
        stack = []
        
        # Basic Stack Operation:
        """
        push:          stack.append(x)
        pop:           stack.pop()
        peek           stack[-1]
        Check Empty    if not stack:
        Length         len(stack)
        """
        
        # 1. Need to iterate through the string one string at a time to find the parantheses
        # 2. Utilize data structure stacks to track parantheses start: (,[, and {
        # 3. Next, we want to keep iterating and use stack operations to determine if it is a valid parentheses.
        
        # Dictionary to match the parenthese
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        # Loop through each char in string s
        for char in s:
            # If it's a closing bracket pop from stack if not empty, else assign dummy value
            if char in mapping:
                topStack = stack.pop() if stack else '#'
                
                # Check if the popped element matches expected opening bracket
                if mapping[char] != topStack:
                    return False
                
            else:
                # If it's an opening bracket, push to stack as hinted in hint 2
                stack.append(char)
                
        # If stack is empty, all brackets matched
        return not stack
                    

"""
if __name__ == "__main__":
    s = Solution()

    # Valid test cases
    print(s.isValid("()"))        # True
    print(s.isValid("()[]{}"))    # True
    print(s.isValid("{[()]}"))    # True

    # Invalid test cases
    print(s.isValid("(]"))        # False
    print(s.isValid("([)]"))      # False
    print(s.isValid("("))         # False
    print(s.isValid("]"))         # False
"""