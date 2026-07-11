class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         # multiply all items in array then return sum // n
         # 0's fuck this...

        # simple way copy of list pop elem multiply list
        length = len(nums)

        result = [1] * length
        for i in range(length):
            for elem in nums[:i] + nums[i + 1 :]:
                result[i] *= elem

        return result