class Solution:
    def braceExpansionII(self, expression: str):

        def union(A, B):
            return A | B

        def concat(A, B):
            return {a + b for a in A for b in B}

        def parse_expr(i):
            # Parse expressions separated by commas
            res, i = parse_term(i)

            while i < len(expression) and expression[i] == ',':
                i += 1
                nxt, i = parse_term(i)
                res = union(res, nxt)

            return res, i

        def parse_term(i):
            # Parse consecutive factors
            res = {""}

            while i < len(expression) and expression[i] not in '},':
                factor, i = parse_factor(i)
                res = concat(res, factor)

            return res, i

        def parse_factor(i):
            if expression[i] == '{':
                res, i = parse_expr(i + 1)
                return res, i + 1

            return {expression[i]}, i + 1

        result, _ = parse_expr(0)

        return sorted(result)