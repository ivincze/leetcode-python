import math

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # Negative number is never a palindrome:
        if x < 0:
            return False

        # Zero is a palindrome:
        elif x == 0:
            return True

        else:
            # Calculate the length of the input:
            length = int(math.floor(math.log10(x))) + 1

            # Variable to store the right half of x as result of shifts to right,
            # using it as a stack to reverse the order of digits:
            stack_num = 0;

            # Push the least significant digit of x into stack_num from right and
            # shift x to right until reaching to the middle:
            for i in range(1, length // 2 + 1):
                # Get the least significant digit:
                lsd = x % 10
                # Push it into stack_num from right:
                stack_num = stack_num * 10 + lsd
                # Shift x to right by 1 digit:
                x = x // 10

            # If length of x was odd: skip the middle digit by one more right shift
            if length % 2 != 0:
                x = x // 10

            # Compare the rest in x with stack_num:
            return x == stack_num


# Test cases:
print("Actual: " + str(Solution().isPalindrome(121)) + ", Expected: True")
print("Actual: " + str(Solution().isPalindrome(-121)) + ", Expected: False")
print("Actual: " + str(Solution().isPalindrome(10)) + ", Expected: False")
