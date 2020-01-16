class Solution(object):
    global_list = []

    def generate(self, i):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if i == 0:
            return self.global_list

        self.generate(i-1)

        local_list = []
        j = 1
        while j<=i:
            if j == 1 or j == i:
                local_list.append(1)
            else:
                local_list.append(self.global_list[i - 2][j - 2] + self.global_list[i - 2][j-1])
            j = j + 1

        self.global_list.append(local_list)
        return self.global_list

s = Solution()
print(s.generate(5))