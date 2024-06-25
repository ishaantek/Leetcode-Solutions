import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(math.sqrt(c))

        while l <= r:
            a2 = l*l
            b2 = r*r
            if (a2 + b2 == c):
                return True
            if (a2 + b2 <= c):
                l += 1
            if (a2 + b2 >= c):
                r -= 1
        return False