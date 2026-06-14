from collections import defaultdict

class Solution:
    def get_freq(self,nums): # must iterate thru all elements of array nums, O(n)
        freq_dict=defaultdict(int)
        for num in nums:
            freq_dict[num]+=1
        return freq_dict

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict=self.get_freq(nums)
        top_K_items = [i[0] for i in sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)[:k]] # sorting costs O(mlog(m)), m being unique items (m<n), slicing top K is O(K)
        return top_K_items

        # Brute force:
    # Iterate thru all elements of nums, building up frequency dict
    

    

        