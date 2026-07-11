class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {"(": ")", "{": "}", "[": "]"}
        s = list(s)
        if len(s) % 2 != 0:
            return False

        stack = []

        for v in s:
            if v in pairs:
                stack.append(v)
            else:
                try:
                    if pairs[stack[-1]] != v:
                        return False
                except IndexError:
                    return False
                else:
                    stack.pop()

        return True if not stack else False