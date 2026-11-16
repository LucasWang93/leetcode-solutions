class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        return self.binarySearch(nums, l, r, target)
    def binarySearch(self, nums, l, r, target):
        if l > r:
            return -1
        m = l + (r - l) // 2
        if target < nums[m]:
            r = m - 1
        elif target > nums[m]:
            l = m + 1
        else:
            return m
        return self.binarySearch(nums, l, r, target)

        