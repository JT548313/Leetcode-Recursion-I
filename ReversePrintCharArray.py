s = ["a", "b", "c", "d", "e"]


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        self.helper(i, j, s)

    def helper(self,i, j, s):
        if i > j:
            return
        self.helper(i+1, j-1, s)
        temp = s[i]
        s[i] = s[j]
        s[j] = temp


solution = Solution()
solution.reverseString(s)
print(s)
