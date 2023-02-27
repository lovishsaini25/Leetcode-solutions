class Solution:
    def calculatePermutation(n, r):
        num = 1
        denum = 1
        for i in range(min(n-r, r)):
            num = (n-i) * num
            denum = denum * (i+1)
        return int(num / denum)
    def generate(self, numRows: int) -> List[List[int]]:        
        result = []
        for i in range(numRows):
            temp = [1] * (i+1)
            temp[0] = temp[i] = 1
            if(i >= 2):
                for j in range(1, i):
                    temp[j] = Solution.calculatePermutation(i, j)
            result.append(temp)
        return result