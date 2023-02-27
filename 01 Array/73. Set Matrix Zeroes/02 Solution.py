# References:
# https://www.youtube.com/watch?v=M65xBewcqcI&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=8
# https://www.youtube.com/watch?v=DHJsjnnRCNg

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_length = len(matrix)
        column_length = len(matrix[0])
        column_has_zero = False
        row_has_zero = False

        for i in range(column_length):
            if(matrix[0][i] == 0):
                column_has_zero = True
                break
        for i in range(row_length):
            if(matrix[i][0] == 0):
                row_has_zero = True
                break
        for i in range(1, row_length):
            for j in range(1, column_length):
                if(matrix[i][j] == 0):
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(column_length):
            if(matrix[0][i] == 0 and i != 0):
                for j in range(1,row_length):
                    matrix[j][i] = 0
        for i in range(row_length):
            if(matrix[i][0] == 0 and i != 0):
                for j in range(1, column_length):
                    matrix[i][j] = 0
        if column_has_zero == True:
            for i in range(column_length):
                matrix[0][i] = 0
        if row_has_zero == True:
            for i in range(row_length):
                matrix[i][0] = 0