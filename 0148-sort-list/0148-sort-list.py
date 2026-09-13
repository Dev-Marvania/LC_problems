# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l1 = [] 
        cur = head
        while cur is not None:
            l1.append(cur.val)
            cur = cur.next
        l1.sort() 
        cur = head
        for value in l1:
            cur.val = value
            cur = cur.next
        return head
        