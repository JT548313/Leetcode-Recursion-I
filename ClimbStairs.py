import math

class Solution(object):
    result = 0
    def climbStairs(self, n):

        if n < 2:
            return n

        y = int(n / 2)

        """
        :type n: int
        :rtype: int
        """

        def iterateTwoSteps(y):
            if y == 0:
                self.result = self.result + 1
                return self.result

            iterateTwoSteps(y - 1)

            x = math.factorial(n - y)
            x1 = math.factorial(n - 2 * y)
            x3 = math.factorial(y)

            r = (x / (x3 * x1))
            self.result = self.result + r
            return self.result

        return iterateTwoSteps(y)


s = Solution()
print(int(s.climbStairs(8)))