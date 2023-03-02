class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Since there are n+1 numbers and each number occurs between [1,n]
        # We can use the same array as our table that keep a record of all the numbers visited.
        # If the value at Index i is X, we will make the value at Index X negative.
        # If number X repeats, we can see that Index X is already negative

        # We can also find the missing number here in case there are n numbers and one duplicate and one missing.
        # Missing number would always be the index of positive number.
         for i in nums:
            index = (-i if i < 0  else i)
            if nums[index] < 0:
                return index
            nums[index] = -nums[index]