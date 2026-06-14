class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # check if neighboring elements are equal
        nums.sort()

        for idx,num in enumerate(nums):
            # compare the next element
            if idx < len(nums)-1:
                if num == nums[idx+1]:
                    # duplicate detected
                    return True
        
        return False

    # has O(nlog(n)) due to the sort, better than brute force approach, which will exhaustively checks whole array
            