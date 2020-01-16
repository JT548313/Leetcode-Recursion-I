# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.memo = {}

    def generateTrees(self, n):
        if n == 0:
            return []
        return self.helper(1, n)

    def helper(self, lower, upper):
        if (lower, upper) not in self.memo:
            if lower > upper:
                return [None]

            out = []
            for top_val in range(lower, upper+1):
                for left_tree in self.helper(lower, top_val - 1):
                    for right_tree in self.helper(top_val + 1, upper):
                        head = TreeNode(top_val)
                        head.left = left_tree
                        head.right = right_tree
                        out.append(head)

            self.memo[(lower, upper)] = out

        return self.memo[(lower, upper)]

s = Solution()
print(s.generateTrees(3))