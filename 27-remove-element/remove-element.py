class Solution:
    def removeElement(self, nums, val):
        k = 0  # Count of elements not equal to val
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
