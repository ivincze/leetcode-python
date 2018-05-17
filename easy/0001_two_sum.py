class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Dictionary to store num->index mapping:
        dict = {}

        # Iterate over the list only once:
        # - if we haven't found a proper pair for the current number yet (check in dict): store its num->index mapping
        # - if we found proper pair already (exists in dict): return indices

        for idx, num in enumerate(nums):

            # For the current number we're looking for another number with this value:
            complement = target - num

            if complement in dict.keys():
                return [dict[complement], idx]
            else:
                dict[num] = idx

        return None


# Test cases:
print("Actual: " + str(Solution().twoSum([2, 7, 11, 15], 9)) + ", Expected: [0, 1]")
