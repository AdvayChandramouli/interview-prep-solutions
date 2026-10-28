class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "]":"[",
            "}":"{",
            ")":"("
        }
        
        stack = []
        for char in s:
            if char in pairs:
                if stack and stack[-1] == pairs[char]:
                    # if these 2 elements match, pop from stack
                    stack.pop()
                else:
                    # stack is either Empty OR the element doesn't close the pair
                    return False
            else:
                # open parantheses
                stack.append(char)
        
        return True if not stack else False

