class Solution(object):
    def __init__(self):
        self.result = 1.0

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n > 0:
            self.result = self.result*x
            self.myPow(x, n-1)
        if n < 0:
            self.result = (self.result) * (1 / x)
            self.myPow(x, n+1)
        return self.result



s = Solution()
print(s.myPow(2.00, 0))