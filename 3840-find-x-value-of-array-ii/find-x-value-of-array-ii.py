class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        # Each node:
        # [product % k, cnt[0], cnt[1], ..., cnt[k-1]]
        #
        # cnt[r] = number of non-empty prefixes
        #          whose product % k == r

        size = 1
        while size < n:
            size *= 2

        tree = [[1] + [0] * k for _ in range(2 * size)]

        # Build leaves
        for i in range(n):
            v = nums[i] % k
            tree[size + i][0] = v
            tree[size + i][v + 1] = 1

        def merge(A, B):
            if A is None:
                return B
            if B is None:
                return A

            pa = A[0]

            res = [0] * (k + 1)

            # Product of whole segment
            res[0] = (A[0] * B[0]) % k

            # Prefixes entirely inside A
            for r in range(k):
                res[r + 1] += A[r + 1]

            # Prefixes consisting of all A + a prefix of B
            for r in range(k):
                new_r = (pa * r) % k
                res[new_r + 1] += B[r + 1]

            return res

        # Build tree
        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])

        def update(pos, value):
            idx = size + pos
            v = value % k

            tree[idx] = [v] + [0] * k
            tree[idx][v + 1] = 1

            idx //= 2

            while idx:
                tree[idx] = merge(tree[2 * idx], tree[2 * idx + 1])
                idx //= 2

        def query(l, r):
            # Query [l, r)
            left_res = None
            right_res = None

            l += size
            r += size

            while l < r:
                if l & 1:
                    left_res = merge(left_res, tree[l])
                    l += 1

                if r & 1:
                    r -= 1
                    right_res = merge(tree[r], right_res)

                l //= 2
                r //= 2

            return merge(left_res, right_res)

        ans = []

        for index, value, start, x in queries:

            # Persistent point update
            update(index, value)

            # All possible remaining arrays are prefixes
            # of nums[start:]
            node = query(start, n)

            ans.append(node[x + 1])

        return ans