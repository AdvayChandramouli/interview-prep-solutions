class Solution:
    import re

    def isPalindrome(self, s: str) -> bool:
        # strip any whitespaces/special characters from input string
        # also convert all chars to lowercase
        
        print(f"Before cleaning S: {s}")
        s = s.lower().replace(" ", "")
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s)
        print(f"After cleaning S: {cleaned}")

        # one pointer starts at first char in string
        ptr1 = 0

        # second pointer starts at last char in the string
        ptr2 = len(cleaned) - 1

        while ptr1 < ptr2:
            if cleaned[ptr1] != cleaned[ptr2]:
                return False

            # Progress each pointer in opposite directions
            ptr1 += 1
            ptr2 -= 1
        
        # If we're out of the loop, that means they're pointing at the same char
        return True
