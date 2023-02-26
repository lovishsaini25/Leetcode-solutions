# More optimized using O(m + n) space
# We create a row and column array that contains whether in a particular row or column, a zero value is present
# Later, we traverse the row and column array to check the indexes where there is a Zero value.
# We mark all the zeroes in our original array wherever there is a zero in a row/column array

# Time complexity (for a N * M matrix): O(N* M + N * M) --> because we traverse the array twice ---> O(N * M)
# Space complexity(for a N * M matrix): O(N) + O(M)



class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = ['No'] * len(matrix)
        c= ['No'] * len(matrix[0])
        for i, vr in enumerate(matrix):
            for j, v in enumerate(vr):
                if(v == 0):
                    r[i] = 0
                    c[j] = 0
        
        for i in range(len(r)):
            for j in range(len(c)):
                if c[j] == 0 or r[i] == 0:
                    matrix[i][j] = 0
        print(matrix)