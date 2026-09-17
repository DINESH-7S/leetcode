class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)

        # best[i] = shortest valid subarray
        # within arr[0:i]
        best = [float('inf')] * (n + 1)

        prefix = 0
        seen = {0: -1}
        ans = float('inf')

        for i in range(n):
            prefix += arr[i]

            # Carry forward the previous best
            best[i + 1] = best[i]

            if prefix - target in seen:
                j = seen[prefix - target]

                # Current subarray is arr[j+1 ... i]
                length = i - j

                # Previous subarray must end before j+1
                if best[j + 1] != float('inf'):
                    ans = min(ans, length + best[j + 1])

                # Current subarray can be the best ending here
                best[i + 1] = min(best[i + 1], length)

            seen[prefix] = i

        return -1 if ans == float('inf') else ans