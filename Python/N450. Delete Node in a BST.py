# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max = None
        self.parent = None
        self.deleteNodeIsLeftSon = False

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        node = self.findNode(root, key)

        # can't fine node
        if node is False:
            return root

        # node is leaf
        if node.left is None and node.right is None:
            node = None
            return root

        # find max value of leftSubTree
        maxValue = self.getMaxValueOfLeftSubTree(node.left)

        # delete node don't have left sub tree
        if maxValue is False:
            if self.deleteNodeIsLeftSon is True:
                self.parent.left = node.right
            else:
                self.parent.right = node.right
        else:
            node.val = maxValue
        return root

    def findNode(self, root, key):
        if root is None:
            return False
        if key == root.val:
            return root
        if key < root.val:
            self.parent = root
            self.deleteNodeIsLeftSon = True
            return self.findNode(root.left, key)
        else:
            self.parent = root
            self.deleteNodeIsLeftSon = False
            return self.findNode(root.right, key)
    
    def getMaxValueOfLeftSubTree(self, root):
        # delete node don't have left sub tree
        if root is None:
            return False

        rightNode = root.right
        if rightNode.right is None:
            # find max node
            root.right = rightNode.left
            return rightNode.val
        else:
            self.getMaxValueOfLeftSubTree(root.right)