'''
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

 

Example 1:

Input: left = 5, right = 7
Output: 4
Example 2:

Input: left = 0, right = 0
Output: 0
Example 3:

Input: left = 1, right = 2147483647
Output: 0

'''

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left==0:
            return 0 
             
        shift = 0
        # find the common MSB bits.
        while left != right:
            
            left,right=left >> 1,right >> 1
        
            shift += 1
            if left==0:
                return 0
        return left << shift
