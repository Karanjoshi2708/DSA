# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Algo : fast and slow pointer
        #        if cycle then fast and slow always meet

        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True

        return False


        # 2     with using hashset

        # sett = set()
        # curr = head
        # while curr:
        #     if curr in sett:
        #         return True
        #     sett.add(curr)
        #     curr = curr.next
        
        # return False

            
        