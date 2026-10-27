class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Initialize to be a very small number
        max_area = -1e99

        # initialize 2 pointers
        left = 0
        right = len(heights) - 1

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            curr_area = height * width

            # Check if it improves area
            if curr_area > max_area:
                max_area = curr_area
            
            # Adjust the pointer, away from the smaller of the values at each pointer index
            if min(heights[left], heights[right]) == heights[left]:
                left += 1
            elif min(heights[left], heights[right]) == heights[right]:
                right -= 1
            
        return max_area
