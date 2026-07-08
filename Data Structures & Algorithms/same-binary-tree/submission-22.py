# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
         # if not p and not q:
        #     return True

        # if not p or not q:
        #     return False

        # if p.val != q.val:
        #     return False

        # return (self.isSameTree(p.left , q.left) and
        # self.isSameTree(p.right , q.right))


        if not p and not q:
            return True

        if not p or not q:
            return False

        stk1 = [p]
        stk2 = [q]

        while stk1 and stk2:
            node1 = stk1.pop()
            node2 = stk2.pop()

            if node1.val != node2.val:
                return False

            if (not node1.left) != (not node2.left):
                return False

            else:
                if node1.left and node2.left:
                    stk1.append(node1.left)
                    stk2.append(node2.left)

            if (not node1.right) != (not node2.right):
                return False

            else:
                if  node1.right and node2.right:
                    stk1.append(node1.right)
                    stk2.append(node2.right)


        return True if not stk1 and not stk2 else False 

            
        