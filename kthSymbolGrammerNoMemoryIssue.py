class Solution(object):

    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 0:
            return 0

        l = K
        if K % 2 != 0:
            l = l + 1

        x = self.kthGrammar(N - 1, l / 2)
        if K % 2 != 0:
            return x

        return (x + 1) % 2

s = Solution()
print(s.kthGrammar(3, 3))