# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # pre = None
        # curr = head

        # while curr:
        #     nxt = curr.next
        #     curr.next = pre
        #     pre = curr
        #     curr = nxt
        # return pre


        # 2 - recursively

        if not head:
            return None

        new_head = head
        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return new_head 
            
        