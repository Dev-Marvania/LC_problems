# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
            
        odd_p = head
        even_p = head.next
        temp = head.next

        while odd_p and even_p and odd_p.next and even_p.next:
            odd_p.next = even_p.next
            odd_p = odd_p.next
            even_p.next = odd_p.next
            even_p = even_p.next
        odd_p.next = temp
        return head