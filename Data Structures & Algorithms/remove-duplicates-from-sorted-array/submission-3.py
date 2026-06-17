class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left=0
        right=1
        k=1
        # result=[nums[0]]
        while right < len(nums):
            if nums[right]!=nums[left]: # found a unique value
                k+=1
                # result.append(nums[right])
                left=left+1 # advance left to anchor on the new unique value
                nums[left]=nums[right]
            # as a default, advance the right index
            right=right+1

        return k
        
# Time complexity: O(n)
# Space complexity: O(1)