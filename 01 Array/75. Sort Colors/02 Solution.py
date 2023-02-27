# Reference: https://www.youtube.com/watch?v=oaVa-9wmpns&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=3

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = mid = 0
        high = len(nums)-1
        print(nums)
        while(mid <= high):
            if(nums[mid] == 0):
                temp = nums[low]
                nums[low] = nums[mid]
                nums[mid] = temp
                low = low + 1
                mid = mid + 1
            elif(nums[mid] == 1):
                mid = mid + 1
            else:
                temp = nums[high]
                nums[high] = nums[mid]
                nums[mid] = temp
                high = high - 1