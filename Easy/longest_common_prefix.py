class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        max_common_prefix = ""
        if len(strs[0]) != 0:
            common_prefix = strs[0][0]
            processed = True
            max_len = len(strs[0])
        else:
            return ""
        while processed:
            for word in strs:
                if not word.startswith(common_prefix):
                    processed = False
                    break
            if processed:
                max_common_prefix = common_prefix
            else:
                break
            if i + 1 < max_len:
                i += 1
                common_prefix += strs[0][i]
            else:
                processed = False
        return max_common_prefix
