class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == 0 or num2 == 0:
            return "0"

        def pow(base, exp):
            if exp == 0:
                return 1
            else:
                result = 1
                for i in range(exp):
                    result = result * base
                return result

        num1_len = len(num1)
        int_num1 = 0
        for i in range(1, num1_len + 1):
            int_num1 = int_num1 + int(num1[-i]) * pow(10, i - 1)
        print(int_num1)
        num2_len = len(num2)
        result = 0
        for i in range(1, num2_len + 1):
            result = result + int_num1 * int(num2[-i]) * pow(10, i - 1)
        return str(result)