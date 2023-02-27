class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = {}
        d[0] = d[1] = d[2] = 0
        for i in nums:
            d[i] = d.get(i) + 1
        index = 0
        for value, count in d.items():
            for i in range(count):
                i = index + i
                nums[i] = value
            index = index + count