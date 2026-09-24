class Solution:
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            digit_sum = sum(int(d) for d in str(nums[i]))

            if digit_sum == i:
                return i

        return -1