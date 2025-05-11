class Solution:
    def countEven(self, num: int) -> int:
        

        count = 0
        for i in range(2,num+1):
            if len(str(i)) > 1:
                c = 0
                for k in str(i):
                    c += int(k)
                if c % 2 == 0:
                    count += 1

            else:
                if i % 2 == 0:
                    count += 1
        return count