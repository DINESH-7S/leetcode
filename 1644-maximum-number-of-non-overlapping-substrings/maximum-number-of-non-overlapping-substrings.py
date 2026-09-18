class Solution:
    def maxNumOfSubstrings(self, s: str):
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        # Find first and last occurrence
        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')
            first[c] = min(first[c], i)
            last[c] = i

        intervals = []

        # Build minimum valid interval for each character
        for c in range(26):
            if first[c] == n:
                continue

            start = first[c]
            end = last[c]
            valid = True

            i = start
            while i <= end:
                x = ord(s[i]) - ord('a')

                # This character appeared before our start
                if first[x] < start:
                    valid = False
                    break

                # Need to include all occurrences of x
                end = max(end, last[x])
                i += 1

            if valid:
                intervals.append((start, end))

        # Greedy: choose intervals ending earliest
        intervals.sort(key=lambda x: x[1])

        ans = []
        prev_end = -1

        for start, end in intervals:
            if start > prev_end:
                ans.append(s[start:end + 1])
                prev_end = end

        return ans