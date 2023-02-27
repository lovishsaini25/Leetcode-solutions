# Reference: https://www.youtube.com/watch?v=w_KEocd__20&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=7

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = nums[0]
        sum = 0
        for i in range(len(nums)):
            sum = sum + nums[i]
            if sum > max:
                max = sum
            if sum < 0:
                sum = 0        
        return max