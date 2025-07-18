class Solution:
    def isThree(self, n: int) -> bool:
        import math

        root = int(math.sqrt(n))
        if root * root != n:
            return False  
        for i in range(2, int(math.sqrt(root)) + 1):
            if root % i == 0:
                return False
        return root > 1

        
        