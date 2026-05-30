class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        MaxWater = 0
        for i in range(len(heights)):
            j=i+1
            while j < len(heights):
                
                print(f"height of box: {min(heights[j], heights[i])} distance between box: {j-i}, area: {min(heights[j], heights[i]) * (j-i)}")
                if min(heights[j], heights[i]) * (j-i) > MaxWater:
                    MaxWater = min(heights[j], heights[i]) * (j-i)
                j+=1
        return MaxWater