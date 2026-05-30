class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = {}
        for words in strs:
            sortedString = ''.join(sorted(words))
            if sortedString not in final:
                final[sortedString] = [words]
            else:
                final[sortedString].append(words)

        return (list(final.values()))
        