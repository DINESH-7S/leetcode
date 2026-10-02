class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(current, open, close):
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add '(' if we still have some left
            if open < n:
                backtrack(current + "(", open + 1, close)

            # Add ')' only if it won't make the string invalid
            if close < open:
                backtrack(current + ")", open, close + 1)

        backtrack("", 0, 0)

        return result