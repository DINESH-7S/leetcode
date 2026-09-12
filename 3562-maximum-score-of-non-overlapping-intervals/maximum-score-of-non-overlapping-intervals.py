from typing import List
from functools import lru_cache
from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:

        # (start, end, weight, original_index)
        intervals = sorted(
            (l, r, w, i)
            for i, (l, r, w) in enumerate(intervals)
        )

        n = len(intervals)

        @lru_cache(None)
        def dp(i, remaining):
            # returns:
            # (maximum_weight, tuple_of_original_indices)

            if i == n or remaining == 0:
                return (0, ())

            # Option 1: Skip current interval
            skip_weight, skip_indices = dp(i + 1, remaining)

            # Option 2: Take current interval
            l, r, weight, original_index = intervals[i]

            # Find first interval with start > current end
            # start == end is STILL overlapping
            j = bisect_right(intervals, (r, float("inf")))

            next_weight, next_indices = dp(j, remaining - 1)

            take_weight = weight + next_weight

            # Keep answer indices sorted
            take_indices = tuple(
                sorted((original_index,) + next_indices)
            )

            # Choose higher weight
            if take_weight > skip_weight:
                return (take_weight, take_indices)

            if take_weight < skip_weight:
                return (skip_weight, skip_indices)

            # Same weight → lexicographically smaller answer
            if take_indices < skip_indices:
                return (take_weight, take_indices)

            return (skip_weight, skip_indices)

        return list(dp(0, 4)[1])