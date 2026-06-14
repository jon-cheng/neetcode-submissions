class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # where value:index
        for idx,val in enumerate(nums):
            complement = target-val

            if complement in seen:
                return [seen[complement], idx]
            else:
                seen[val]=idx
        
        return None

# Time complexity is O(n)
# Space complexity is O(n) due to the dict seen