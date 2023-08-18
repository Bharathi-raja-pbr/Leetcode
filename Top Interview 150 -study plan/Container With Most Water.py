class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        i=0
        size=len(height)-1
        while i<size:
            diff=size-i
            min_height=min(height[i],height[size])
            max_area=max(max_area,min_height*diff)

            if height[i]<height[size]:
                i+=1
            else :
                size-=1
        return max_area
