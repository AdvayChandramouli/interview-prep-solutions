class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Worst Case: return empty list
        sol = []
        nums.sort()

        base = 0
        for i in range(len(nums) - 2):
            # increment only if AFTER first iteration AND 2 consecutive ints are the same
            if i > 0 and nums[i] == nums[i - 1]:
                base += 1
                continue

            # Treat this as a TwoSum with 2 pointers, on a smaller subarray
            left = base + 1
            right = len(nums) - 1

            while left < right:
                target = 0 - nums[base]
                curr_sum = nums[left] + nums[right]

                if curr_sum > target:
                    right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    sol.append([nums[base], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            base += 1    

        return sol