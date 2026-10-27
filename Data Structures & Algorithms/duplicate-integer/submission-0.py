class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elems = set()
        for n in nums:
            if n in elems:
                return True
            else:
                elems.add(n)
        
        return False