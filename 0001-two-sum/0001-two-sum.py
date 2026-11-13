class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        count = defaultdict(lambda: -1)

        for i in range(len(nums)):
            if count[target - nums[i]] != -1:
                return [count[target - nums[i]], i]
            count[nums[i]] = i

        print(count)


            