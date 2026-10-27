class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers --> ascending order, 1-indexed (so +1)
        left = 0
        right = len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum > target:
                # decrement the right pointer
                right -= 1
            elif curr_sum < target:
                # increment left pointer
                left += 1
            else:
                # return the two numbers
                return [left+1, right+1]
        
        

