# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.leaf_node_depth = []

    def maxDepth(self, root):
        depth = 0
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return depth
        self.leafNodeDepth(root, depth+1)
        return max(self.leaf_node_depth)

    def leafNodeDepth(self, root, depth):
        if root.left is None and root.right is None:
            self.leaf_node_depth.append(depth)

        if root.left is not None:
            self.leafNodeDepth(root.left, depth + 1)

        if root.right is not None:
            self.leafNodeDepth(root.right, depth + 1)


root = TreeNode(3)
t1 = TreeNode(9)
t2 = TreeNode(20)
root.left = t1
root.right = t2

t3 = TreeNode(15)
t4 = TreeNode(7)

t2.left = t3
t2.right = t4

s = Solution()
print(s.maxDepth(root))
