from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # We know that S&t are lowercase; 
        # Length: anagrams must be same length;
        flag = True

        if len(s) != len(t):
            return False
        else:
            # initialize 2 default dicts to work as frequency maps
            s_chars = defaultdict(int)
            t_chars = defaultdict(int)

            # given both strings are now the same length:
            for i in range(len(s)):
                
                s_chars[s[i]] += 1
                t_chars[t[i]] += 1

            # if both strings of same length have different number of unique characters, return false
            if len(s_chars) != len(t_chars):
                return False
            else:
                for char in s_chars:
                    if char in t_chars and s_chars[char] == t_chars[char]:
                        flag = True
                    else:
                        flag = False
                        break
            
        
        return flag

        
