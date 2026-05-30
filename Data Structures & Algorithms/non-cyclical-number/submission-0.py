class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {n:'1'}
        while n != 1:
            SumOfSquares = 0
            for c in str(n):
                SumOfSquares += int(c) ** 2
            if SumOfSquares in seen:
                return False
            else:
                n = SumOfSquares
                seen[n] = 1
        return True