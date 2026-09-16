class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        
        N = n + k - 1
        R = 2 * k

        
        fact = [1] * (N + 1)
        for i in range(1, N + 1):
            fact[i] = fact[i - 1] * i % MOD

        
        def mod_inverse(x):
            return pow(x, MOD - 2, MOD)

        numerator = fact[N]
        denominator = fact[R] * fact[N - R] % MOD

        return numerator * mod_inverse(denominator) % MOD