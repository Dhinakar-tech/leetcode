from collections import defaultdict
from fractions import Fraction

class Solution:
    def interchangeableRectangles(self, rectangles):
        ratio_map = defaultdict(int)
        count = 0

        for w, h in rectangles:
            ratio = Fraction(w, h)
            count += ratio_map[ratio]
            ratio_map[ratio] += 1

        return count
