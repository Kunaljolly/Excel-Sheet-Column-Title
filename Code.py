from string import ascii_uppercase

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        d = {k+1:v for k,v in enumerate(ascii_uppercase)}
        t = ""
        while columnNumber > 0:
            columnNumber, remainder = divmod(columnNumber - 1, 26)
            t = d[remainder + 1] + t
        return t
