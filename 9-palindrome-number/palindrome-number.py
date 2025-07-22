class Solution:
    def isPalindrome(self,x)->bool:
        a=str(x)
        x=a[::-1]
        if a==x:
            return True
        else:
            return False    
