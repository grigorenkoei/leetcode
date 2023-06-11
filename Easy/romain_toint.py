class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        s = s[::-1]
        integer_num = numerals[s[0]]

        for i in range(1, len(s)):
            if numerals[s[i]] >= numerals[s[i - 1]]:
                integer_num += numerals[s[i]]
            else:
                integer_num -= numerals[s[i]]

        return integer_num