class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        (x1, y1), (x2, y2), (x3, y3) = points

        if len(set(map(tuple, points))) < 3:
            
            return False
        return (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1)