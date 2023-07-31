'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

'''
class Solution:
    def isValid(self, s: str) -> bool:
        lis=['1']
        valid=']})'
        valid1='{(['
        for x in s:
            if x in valid1:
                lis.append(x)
            elif x in valid:
                if lis[-1]=='(' and x==')':
                    lis.pop()
                elif lis[-1]=='{' and x=='}':
                    lis.pop()
                elif lis[-1]=='[' and x==']':
                    lis.pop()
                else:
                    lis.append(x)
        if len(lis)==1:
            return True
        else:
            return False
        
