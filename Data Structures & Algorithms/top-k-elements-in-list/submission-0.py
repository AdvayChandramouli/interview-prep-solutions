from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        
        '''
        index 0 --> [list of elems with count 0]
        index 1 --> [list of elems with count 1]
        ...
        repeat for n indices

        when we finish, select the top k indices (starting from back of the list) --> and return them as a list
        most # of indices has at most len(nums) elements therefore we can scan in linear time

        '''
        
        count = defaultdict(int)
        # initialize to have a list of n lists, given input has n elements
        freq = [[] for i in range(len(nums)+1)] # for each index from 0 to len(nums), this now gives us an empty list
        result = []

        for n in nums:
            count[n] += 1
        for key, val in count.items():
            freq[val].append(key)
        
        for i in range(len(nums), 0, -1):
            if len(freq[i]) == 0: # if this index has an empty list, continue
                continue
            else:
                # add the elements with that count;
                result.extend(n for n in freq[i])
                if len(result) == k:
                    break

        return result
