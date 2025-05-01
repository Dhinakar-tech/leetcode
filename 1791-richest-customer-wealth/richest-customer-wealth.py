class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        lst=[]
        for i in accounts:
            lst.append(sum(i))
        return max(lst)