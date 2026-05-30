# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
        
#         if len(s) != len(t):
#             return False

#         track = {}
#         for c in s:
#             track[c] = 0
        
#         for c in t:
#             try:
#                 if track[c] == 0:
#                     pass
#             except KeyError:
#                 return False

#         return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Initialize a dictionary with all alphabet letters set to 0
        track = {chr(i + ord('a')): 0 for i in range(26)} # this makes dict set length and input size doestnt chnage space needed.
        
        # Count the frequency of characters in s
        for c in s:
            track[c] += 1
        
        # Check if characters in t match the frequency in the track
        for c in t:
            track[c] -= 1
            if track[c] < 0:
                return False
        
        # All frequencies should be 0 if t is a valid anagram of s
        return True
