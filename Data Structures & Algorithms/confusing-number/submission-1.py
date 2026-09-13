class Solution:
    def confusingNumber(self, n: int) -> bool:
        mapping = {
            "0" : "0",
            "1" : "1",
            "6" : "9",
            "8" : "8",
            "9" : "6"
        }
        copy = str(n)[::-1]
        invalid = ['2', '3', '4', '5', '7']
        if any(elem in invalid for elem in copy):
            return False

        copy = "".join(mapping[char] for char in copy)
        
        return n != int(copy)