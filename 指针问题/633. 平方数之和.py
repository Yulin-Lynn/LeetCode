class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i, j = 0, int(c**0.5)
        while i <= j:
            if i*i+j*j == c:
                return True
            elif i*i+j*j < c:
                i += 1
            else:
                j -= 1
        return False