# Reference
# https://www.youtube.com/watch?v=LuLCLgMElus&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=9

class Solution:
    def nextPermutation(self, num: List[int]) -> None:
        """
        Do not return anything, modify num in-place instead.
        """
        index = len(num)-1
        for i in range(len(num)-1, -1, -1):
            if len(num) == 1:
                break
            else:
                if(num[i] > num[i-1]):
                    index = i-1
                    break
        if index >= 0:    
            for i in range(len(num)-1, index-1, -1):
                if len(num) == 1:
                    break
                if(num[index] < num[i]):
                    temp = num[index]
                    num[index] = num[i]
                    num[i] = temp
                    for i in range(1, ((len(num)-index)//2 if (len(num)-index) % 2 == 0 else (len(num)-index)//2 + 1)):
                        temp = num[i+index]
                        num[i+index] = num[len(num)-i]
                        num[len(num)-i] = temp
                    break
        else:
            for i in range(len(num)//2):
                temp = num[i]
                num[i] = num[len(num)-i-1]
                num[len(num)-i-1] = temp