# 992. Subarrays with K Different Integers
# Hard
# Topics
# Companies
# Given an integer array nums and an integer k, return the number of good subarrays of nums.
#
# A good array is an array where the number of different integers in that array is exactly k.
#
# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.
#
"""
 Hash map of the stuff first to the keep count of the number

 sliding window
"""
from itertools import combinations


class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        comb = combinations(nums, k)

        for c in list(comb):
            print(c)

        return len(list(comb))

        pass


s = Solution()
output = s.subarraysWithKDistinct([1, 2, 1, 2, 3], 2)
print(output)
