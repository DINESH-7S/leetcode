class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        diff.sort(reverse=True)
        diff.append(0)

        n = len(diff)
        for i in range(n - 1):
            need = (diff[i] - diff[i + 1]) * (i + 1)

            if k >= need:
                k -= need
            else:
                level = diff[i] - k // (i + 1)
                rem = k % (i + 1)

                ans = rem * (level - 1) ** 2
                ans += (i + 1 - rem) * level ** 2

                for j in range(i + 1, n - 1):
                    ans += diff[j] ** 2

                return ans

        return 0