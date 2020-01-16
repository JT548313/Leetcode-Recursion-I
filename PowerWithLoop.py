class Solution(object):
    def __init__(self):
        self.result = 1.0

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        while (n > 0):
            self.result = self.result * x
            n = n - 1

        while (n > 0):
            self.result = (self.result) * (1 / x)
            n = n +1
        return self.result



s = Solution()
print(s.myPow(2.00, 0))