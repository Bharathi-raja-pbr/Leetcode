'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
   def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

     #convert the linked list into a number
     def getnum(head):
        num=0
        power=0
        t=head
        while t:
            num+=t.val*(10**power)
            power+=1
            t=t.next
        return num
       
     #operation performed
     
     def sum(l1,l2):
        val1=getnum(l1)
        val2=getnum(l2)
        ans=str(val1+val2)

        dummy=ListNode(0)
        head=dummy
        for x in ans[::-1]:
            head.next=ListNode(int(x))
            head=head.next
        return dummy.next

     return sum(l1,l2)
    
    
