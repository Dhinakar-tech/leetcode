class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        fullsize=set(range(1,n+1))
        numset=set(nums)
        missing=list(fullsize-numset)
        return missing

        