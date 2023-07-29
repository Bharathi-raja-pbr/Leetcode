'''
Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
'''
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        for i in range(len(lst)):
            if i == left-1:
                lst[i:right] = lst[i:right][::-1]
        a = ListNode(0)
        temp = a
        for i in lst:
            temp.next = ListNode(i)
            temp = temp.next
        return a.next
