class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        from collections import Counter

        count = 0
        freq = Counter(nums)

        for val in freq.values():
            count += (val * (val - 1)) // 2 

        return count
