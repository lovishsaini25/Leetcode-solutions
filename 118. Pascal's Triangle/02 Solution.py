class Solution:
    def generate(self, numRows: int) -> List[List[int]]:        
        result = []
        for i in range(numRows):
            temp = [1] * (i+1)
            temp[0] = temp[i] = 1
            if(i >= 2):
                for j in range(1, i):
                    temp[j] = temp[i- j] = result[i-1][j-1] + result[i-1][j]
            result.append(temp)
        return result