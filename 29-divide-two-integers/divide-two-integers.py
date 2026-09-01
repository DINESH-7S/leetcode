class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # Handle overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        # Determine whether result should be negative
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive numbers
        a = abs(dividend)
        b = abs(divisor)

        result = 0

        while a >= b:

            # Find the largest doubled divisor <= dividend
            value = b
            multiple = 1

            while value + value <= a:
                value += value
                multiple += multiple

            # Subtract it
            a -= value
            result += multiple

        return -result if negative else result