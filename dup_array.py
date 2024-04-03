from typing import List


class Solution:

    def findDuplicates(self, nums: List[int]) -> List[int]:
        repeated = []
        nums = sorted(nums)
        x = 0
        while x < len(nums) - 1:
            if nums[x] == nums[x + 1] and nums[x] not in repeated:
                repeated.append(nums[x])
                x += 2
            else:
                x += 1
        return repeated


s = Solution()

nums = [4, 3, 2, 7, 8, 2, 3, 1]


output = s.findDuplicates(nums)
print(output)
