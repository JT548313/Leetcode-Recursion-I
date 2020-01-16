class Solution(object):

    def fib(self, N):
        cache = {}
        """
        :type N: int
        :rtype: int
        """
        if N in cache:
            return cache[N]

        if N < 2:
            return N
        else:
            result = self.fib(N-1) + self.fib(N-2)

        cache[N] = result
        return result

s = Solution()
print(s.fib(12))

