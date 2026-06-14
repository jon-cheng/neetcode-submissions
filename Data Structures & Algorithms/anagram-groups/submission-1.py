from collections import defaultdict

class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # groups is a dict of {anagram_id:count}
    def groupAnagrams(self, strs:List[str])-> List[List[str]]: 
        groups=defaultdict(list)
        for s in strs: # we have to iterate thru the whole list of input strs O(n)
            # get signature should be a tuple
            # counts is a per-anagram signature of letter counts, encoded by index pos
            counts = [0]*26 # initialize
            for char in s:
                idx = ord(char)-ord('a')
                # populate at respective pos with count
                # if not seen before
                counts[idx]+=1

            # convert counts to be a tuple for hashability serving as a signature in the 
            counts_tuple = tuple(counts)

            # if counts_tuple in groups.keys():
                # if already in the groups keys, populate with the current string s
            groups[counts_tuple].append(s)

        return list(groups.values())
        