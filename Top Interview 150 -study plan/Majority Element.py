'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
'''
#time efficient but not space efficient
from collections import Counter  
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)//2
        a=Counter(nums)
        for i in a:
           if a[i] >n:
               return i
#time and space efficient
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)//2
        return nums[n]
