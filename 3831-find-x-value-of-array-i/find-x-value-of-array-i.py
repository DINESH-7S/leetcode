class Solution:
    def resultArray(self, nums, k):
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k
            r = num % k

            # Start a new subarray with just num
            new_dp[r] += 1

            # Extend previous subarrays
            for old_r in range(k):
                new_r = (old_r * r) % k
                new_dp[new_r] += dp[old_r]

            # Add all subarrays ending here to the answer
            for x in range(k):
                ans[x] += new_dp[x]

            dp = new_dp

        return ans