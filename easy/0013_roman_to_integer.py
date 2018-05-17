class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        single_digits = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        double_digits = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        # Return value, we keep adding to it as parsing the input string:
        num = 0

        # Used to remember the previous character while iterating over the string:
        prev_char = ''

        for i, current_char in enumerate(s):

            # Combine current and previous characters to check for double digits:
            possible_double_digit = prev_char + current_char

            # If current and previous characters form a valid double digit:
            if possible_double_digit in double_digits.keys():

                # Add the value of the double digit to num:
                num += double_digits[possible_double_digit]
                # Set prev_char to empty string: not to consider current_char as start of another double digit
                prev_char = ''

            else:

                # If prev_char is a valid single digit:
                if prev_char in single_digits.keys():

                    # Add the value of the prev_char's single digit to num:
                    num += single_digits[prev_char]

                # If prev_char is an invalid single digit: throw error
                elif prev_char != '' and prev_char not in single_digits.keys():

                    print("Invalid Roman digit: " + prev_char)
                    return None

                # For characters before the last one:
                if i < len(s) - 1:

                    # Set prev_char to current_char:
                    # to remember when checking for possible double digit in next iteration
                    prev_char = current_char

                # Check the last character explicitly as it would not be handled as prev_char at all:
                elif current_char in single_digits.keys():

                    # Add the value of the current_char's single digit to num:
                    num += single_digits[current_char]

                # If current_char is an invalid single digit: throw error
                else:
                    print("Invalid Roman digit: " + current_char)
                    return None

        return num


# Test cases:
print("Actual: " + str(Solution().romanToInt("III")) + ", Expected: 3")
print("Actual: " + str(Solution().romanToInt("IV")) + ", Expected: 4")
print("Actual: " + str(Solution().romanToInt("IX")) + ", Expected: 9")
print("Actual: " + str(Solution().romanToInt("LVIII")) + ", Expected: 58")
print("Actual: " + str(Solution().romanToInt("MCMXCIV")) + ", Expected: 1994")
print("Actual: " + str(Solution().romanToInt("ZSG")) + ", Expected: None (Invalid Roman digit: Z)")
print("Actual: " + str(Solution().romanToInt("MCMXCIVK")) + ", Expected: None (Invalid Roman digit: K)")
