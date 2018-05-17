import math


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        # Perform with positive value:
        num = abs(x)
        rev = 0

        # Stop when num becomes 0:
        while num > 0:
            # Shift rev to left by 1 digit:
            rev *= 10
            # Add least significant digit of num to rev:
            rev += (num % 10)
            # Shift num to right by 1 digit:
            num = int(num / 10)

        # Set sign according to the input (x):
        if x < 0:
            rev = rev * -1

        # Check for reverse integer overflow:
        max_val = math.pow(2, 31)
        if (rev < -1 * max_val) or (rev > max_val - 1):
            return 0

        return rev


# Test cases:
print("Actual: " + str(Solution().reverse(123)) + ", Expected: 321")
print("Actual: " + str(Solution().reverse(-123)) + ", Expected: -321")
print("Actual: " + str(Solution().reverse(120)) + ", Expected: 21")
