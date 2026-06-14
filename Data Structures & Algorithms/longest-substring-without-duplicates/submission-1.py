# use a sliding window that moves left to right

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set=set() # keep track of the 
        left=0
        max_len=0

        for right in range(len(s)):
            while s[right] in char_set: # in the case that a duplicate is found, which could take several iterations in while loop to resolve
                char_set.remove(s[left]) # remove leftmost char
                left+=1 #increment the left bound
            char_set.add(s[right]) # grow the substring rightward
            max_len=max(max_len,right-left+1) # record only the highest length up to now
        return max_len

# Time complexity: O(n)
# Space complexity: O(1) where n is only as long as possible ASCII chars, 128

# def length_of_longest_substring(s):
#     max_len = 0

#     for i in range(len(s)): # let i be the index of the whole input string s
#         seen=set() # specific set of seen chars in each substring
#         for j in range(i,len(s)): # grow substring from i
#             if s[j] in seen:
#                 break
#             seen.add(s[j]) #add to the set if not seen
#             max_len=max(max_len, j-i+1)
    
#     return max_len
        