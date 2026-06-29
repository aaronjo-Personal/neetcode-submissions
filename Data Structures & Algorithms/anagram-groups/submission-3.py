class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for index, word in enumerate(strs):
            anagrams[word] = [word]

            for i in range(len(strs)):
                if index != i and sorted(word) == sorted(strs[i]):
                    anagrams[word].append(strs[i])
        # anagrams dict is k,v = str,List. But dupe Vs
        # Going to flip k,v then flip back, should dedupe
        # also need to convert to tuple to set as key

        dedupe = {tuple(sorted(v)): k for k, v in anagrams.items()}
        # sort the list, then convert to tuple so it can be a key
        # then as its forced to be key dict will dedupe
        # then just return a list of the keys
        return [list(pairs) for pairs in dedupe.keys()]
