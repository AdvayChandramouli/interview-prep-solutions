class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        result = []

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in hmap.keys():
                # add the indice
                result = [hmap[diff], i]
            else:
                hmap[nums[i]] = hmap.get(nums[i], i)

        return result