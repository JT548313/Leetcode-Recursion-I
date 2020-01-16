class Solution(object):
    def __init__(self):
        temp = []

    def generateGrammar(self, N):
        if N == 0:
            return [0]

        if N == 1:
            self.temp = [0,1]

        if N > 1:
            self.temp = self.generateGrammar(N - 1)
            length = len(self.temp)
            self.temp.extend(self.temp[int(length/2):length])
            self.temp.extend(self.temp[0:int(length/2)])
        return self.temp

    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """

        if N == 0 or K == 0 or K > pow(2, N) - 1:
            return None

        result = self.generateGrammar(N)
        return result[K-1]

s = Solution()
print(s.kthGrammar(3, 3))
