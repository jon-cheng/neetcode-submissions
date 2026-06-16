# Intuition: we first need to sort the nums
# This is like running a three-nested loop, but instead we are iterating over a single dimension, and then performing a two-pointer against the remaining two elements
# Fix one element, calculate a target, and then find the target from the remaining two elements
# num + (remaining) = 0, let target=remaining
# We must add guards to not add duplicate triplets

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
    
        results=[]

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: # detect backward-looking duplicates, use i>0 to guard against indices of -1 which is wrong
                continue

            target = -nums[i] # this comes from nums[i] + target = 0, with target being the sum of 2 remaining elements 
            # run while loop two pointer

            left=i+1
            right=len(nums)-1

            while left<right:
                # case where we find the target
                if nums[left] + nums[right] == target:
                    # return [nums[i], nums[left], nums[right]]
                    # must also move the left and right to sweep to find other triplets?
                    results.append([nums[i], nums[left], nums[right]])
                    left+=1 # we must advance the index to explore other triplets
                    right-=1
                    # guard to remove duplicate
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        
        return results 
    
    # Time complexity: O(n^2)
    # Space complexity: O(1), O(n) if you count the output size (but usually doesnt count)
        