class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        x_copy = x
        str_num = ""
        while x > 0:
            str_num += str(x % 10)
            x = x // 10

        if len(str_num) and int(str_num) == x_copy:
            return True
        else:
            return False