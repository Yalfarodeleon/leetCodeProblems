
"""
    Hints:

"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # Need a list to implement stack
        stack = []
        
        # Basic Stack Operation:
        """
        push:          stack.append(x)
        pop:           stack.pop()
        peek/Top       stack[-1]
        Check Empty    if not stack:
        Length         len(stack)
        """