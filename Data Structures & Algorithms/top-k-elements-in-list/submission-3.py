class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
 
        # invert dict K,v to list of tuples 

        inverted_sorted = sorted([(v,k) for k,v in count.items()])

        return [nums[1] for nums in inverted_sorted[-k:]]
