"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4



Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums contains distinct values sorted in ascending order.
    -104 <= target <= 104

"""

# 64 ms
def search_insert_position_1(nums: list[int], target: int) -> int:
    i = 0
    while i < len(nums):
        if nums[i] == target:
            return i
        elif nums[i] < target:
            i += 1
        elif nums[i] > target:
            return i
    return len(nums)


# 56 ms
def search_insert_position_2(nums: list[int], target: int) -> int:
    for i, value in enumerate(nums):
        if value == target:
            return i
        elif nums[i] > target:
            return i
    return len(nums)


if __name__ == '__main__':
    nums = [1,3,5,6,7,8,9,10,11,13]
    target = 15
    result = search_insert_position_2(nums, target)
    print(result)