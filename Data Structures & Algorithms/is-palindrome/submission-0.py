class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0 # left index
        right=len(s)-1 # right index
        while left<right:
            left_char=s[left].lower()
            right_char=s[right].lower()

            # check is alphanumeric
            if not left_char.isalnum():
                left=left+1
                continue

            if not right_char.isalnum():
                right=right-1
                continue
            
            # check for equality:
            if left_char!=right_char:
                return False
            
            # move onto the next pair to compare 
            left=left+1
            right=right-1
        
        return True
        