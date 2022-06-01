class Solution:
    def is_go_outside(self, x:int):
        # go outside than return 0
        if x > pow(2, 31)-1:
            return True
        elif x < pow(-2, 31)-1:
            return True
        elif x == 0:
            return True
    
    def reverse(self, x: int) -> int:
        if self.is_go_outside(x) is True:
            return 0
        # isNegative = True when x is negative
        isNegative = False
        if x < 0:
            isNegative = True
            x = abs(x)
        # reverse
        box = list()
        while x != 0:
            temp = x%10
            x = int(x/10)
            box.append(temp)
        ans = str()
        for idx, value in enumerate(box):
            ans += str(value)
        ans = int(ans)
        if isNegative is True:
            ans = -ans
        if self.is_go_outside(ans) is True:
            return 0
        return ans