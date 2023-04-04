class Solution:

    def romanToInt(self, s: str) -> int:
        res = 0
        pre = ""
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for k,v in enumerate(s):
            if pre is not "" and pre < d.get(v):
                res = res - (pre * 2)
            res = res + d.get(v)
            pre = d.get(v)

        return res