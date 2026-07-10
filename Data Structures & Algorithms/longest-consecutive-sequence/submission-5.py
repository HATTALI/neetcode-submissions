class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_nums = set(nums)

        res = 0

        for num in nums:
            curr = num
            length = 0
            while curr in new_nums:
                length += 1
                curr += 1
            res = max(length, res)
        return res
                