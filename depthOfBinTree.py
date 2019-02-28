# Definition for a binary tree node.
class TreeNode(object):
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def find(root, tier):
            if not root:
                return 0
            if self.t < tier:
                self.t = tier
            find(root.left, tier+1)
            find(root.right, tier+1)
            
        self.t = 0
        find(root, 1)
        return self.t
