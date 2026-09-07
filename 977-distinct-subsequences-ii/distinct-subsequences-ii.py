class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        # dp[i] = number of distinct subsequences ending with chr(i + 'a')
        dp = [0] * 26

        for c in s:
            index = ord(c) - ord('a')

            # Every existing subsequence + the character itself
            dp[index] = (sum(dp) + 1) % MOD

        return sum(dp) % MOD