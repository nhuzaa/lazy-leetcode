from typing import List


def maxArea(height: List[int]) -> int:

    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        width = right - left

        cur_ht = min(height[left], height[right])
        cur_ar = width * cur_ht

        max_area = max(max_area, cur_ar)

        # move the
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

output = maxArea(height)

print("output", output)
