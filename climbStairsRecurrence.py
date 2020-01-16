class Solution(object):
    cache = {}
    def climbStairs(self, n):

        if n in self.cache:
            return self.cache[n]

        if n <= 2:
            return n

        """
        :type n: int
        :rtype: int
        """

        result = self.climbStairs(n-1) + self.climbStairs(n-2)

        self.cache[n] = result
        return result

s =Solution()
print(s.climbStairs(8))