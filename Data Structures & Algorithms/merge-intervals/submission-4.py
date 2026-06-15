class Solution:
    def merge_two_intervals(self,u:List[int],v:List[int]):
        if not (u[1]<v[0] or v[1]<u[0]):
            return [min(u[0],v[0]),max(u[1],v[1])]
        else:
            return None

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() # must sort the intervals first

        # proceed to merge intervals one-by-one in the elements of intervals

        result=[intervals[0]]
        for interval in intervals[1:]:
            # determine whether to merge or to add a new element to the master list:
            # compare the current updated interval vs the query interval within intervals List
            # is overlapping?
            # if yes -> merge 
            # if no -> add the query interval as a nonoverlapping interval
            if self.merge_two_intervals(interval,result[-1]) is not None:
                # detected overlap, so let's merge the two, return a new interval list
                result[-1] = self.merge_two_intervals(interval,result[-1])
            else:
                # cannot merge, instead append the non-overlapping interval
                result.append(interval)
        
        return result
    
    # Time complexity: O(nlog(n)) with n being the number of intervals
    # Space complexity: O(n)