class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = dict()
        len_s = len(s)
        max_cnt = 0
        i = 0
        while i < len_s:
            for j in range(i, len_s):
                if s[j] not in letters:
                    letters[s[j]] = j
                else:
                    max_cnt = max(len(letters), max_cnt)
                    i = letters[s[j]] + 1
                    letters = {}
        return max_cnt