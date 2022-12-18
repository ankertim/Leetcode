# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        left = root.left
        right = root.right

        leftIsValidBST = self.isValidBST(left)
        rightIsValidBST = self.isValidBST(right)

        if leftIsValidBST and rightIsValidBST:
            if left != None:
                leftBool = left.val < root.val
            else:
                leftBool = True
            if right != None:
                rightBool = right.val > root.val
            else:
                rightBool = True
            return leftBool and rightBool
        else:
            return False
        

