class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count=0
        s=len(nums)
        for i in range(s):
            for j in range(i+1 , s):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    count = count+ 1
        return count            
        