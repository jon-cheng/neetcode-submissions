class Solution:
    # The requirement of O(1) requires we don't store some intermediate data structure like a dict or list
    # We can use a two pointer solution, continually narrowing down the i and j indices
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1

        while left<right:
            if numbers[left] + numbers[right] > target:
                # move right pointer leftward
                right = right - 1
            elif numbers[left] + numbers[right] < target:
                # move left pointer rightward
                left = left + 1
            else:
                # done - and store the indices, adjust to 1-based indexing
                return [left+1,right+1]
            
        print("No valid pair found")
        return None

# Time complexity: O(n)
# Space complexity: O(1), per requirement

# # Brute Force Solution:
# # generate a dict to store values so we can look up if complement is present

# def get_indices(nums,target):

#     values_dict={} # values_dict with value(num),index(position in nums array) - but what about if there repeat values - collisions in dict keys?
#     for idx,num in enumerate(nums):
#         complement = target-num
#         if complement in values_dict:
#             # done - fetch index of the complement
#             return (values_dict[complement]+1,idx+1) # index corresponding to the val complement in values_dict and the current index, return 1-based indices
#         else:
#             values_dict[num]=idx
#             # keep going storing the new value-idx 
    
#     return None

# # Maybe non-optimal solution because nums is pre-sorted? 
# # Time: O(n)
# # Space: O(n)

    
        