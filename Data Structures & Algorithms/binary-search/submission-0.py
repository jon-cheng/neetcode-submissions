class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1

        while left<=right:
            # split the array into left and right subarrays:
            # establish midpoint in order to perform split
            mid=(left+right)//2 # mid is the current query index, round down to nearest int

            if nums[mid] == target:
                # found target, done, record the current index
                return mid

            elif target > nums[mid]: # if target is bigger than the current query number
                # take the right array, so update the left bound
                left = mid + 1 # Guarantees left moves past mid 
            
            elif target < nums[mid]: # if target is smaller than the current query number, update the right bound
                right = mid - 1 # Guarantees right moves past mid

        return -1
        