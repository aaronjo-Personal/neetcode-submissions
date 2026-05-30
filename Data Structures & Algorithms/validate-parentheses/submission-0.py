class Solution:
    def isValid(self, s: str):
        stack = []
        Parentheses = {
                "{": "}",
                "(": ")",
                "[": "]"
        } 


        for char in s:
            if char in Parentheses.keys():
                stack.append(char)
            elif char in Parentheses.values():
                if (len(stack)) == 0 or Parentheses[stack[-1]] != char:
                    return False
                stack.pop()
                
        return len(stack) == 0

