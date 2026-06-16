class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Run a variation of binary search
        # Intuition: divide input array into two subarrays, check if left or right subarray is sorted
        # We can only run binary search on the sorted array, so continue on that
        # Within the sorted subarray, find if target is within range, if so, continue narrowing down there
        # If not a sorted array, go to the other half array
        # If target is out of range in the subarray, go to the other half
        # total of 4 possibilities other than directly finding the target

        left=0
        right=len(nums)-1

        while left<=right:
            # 
            mid=(left+right)//2  # take floor

            # best case: already found the target
            if nums[mid] == target:
                # done, store mid
                return mid
            if nums[left]<=nums[mid]: # sorted side is on left side
                # if target is in range, run the binary search on this range
                if nums[left]<=target<nums[mid]:
                    # continue to search this array, by narrowing down the range
                    # define new mid
                    right = mid - 1            
                else:
                    # go to the other side
                    left = mid + 1
            else: # sorted side is on right side
                if nums[mid]<target<=nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

# time complexity: O(log n) 
# space complexity: O(1)
        