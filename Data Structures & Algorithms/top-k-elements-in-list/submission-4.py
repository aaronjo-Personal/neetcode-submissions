class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        count = [[] for i in range(1, len(nums)+1)]
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        for key,v in freq.items():
            count[v-1].append(key)
    
        answer = []
        while len(answer) < k:
            if count[-1] == []:
                count.pop()
            else:
                answer.extend(count[-1])
                count.pop()
        return answer
