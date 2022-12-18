# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.level = list()
        self.result = list()
        self.firstTime = True

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = list()
        if root is None:
            return list()

        queue.append(root)
        queue.append('flag')
        return self.clearQueue(queue)

    def clearQueue(self, queue):
        node = queue.pop(0)
        if (node != 'flag'):
            self.level.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        else :
            self.result.append(self.level)
            # stop condition
            if len(queue) == 0:
                return self.result
            # level done
            queue.append('flag')
            self.level = list()

        return self.clearQueue(queue)