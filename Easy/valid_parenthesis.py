class Solution:
    def isValid(self, s: str) -> bool:
            stack = []
            types = {
                '}': '{',
                ']': '[',
                ')': '(',
            }
            for c in s:
                if c in [')', ']', '}']:
                    if len(stack) != 0 and stack[-1] == types[c]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(c)
            if len(stack) != 0:
                return False
            else:
                return True