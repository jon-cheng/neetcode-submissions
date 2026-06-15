"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events=self.get_events(intervals)
        n=0
        max_count=0 # running max over time
        # keep a tally of current local max
        for event in events:
            n+=event[1] 

            max_count=max(n,max_count) #update to current max 
        return max_count

    def get_events(self,intervals):
        """
        Get a list of tuples of events [(event,+1 or -1),...]
        """
        events=[]
        for interval in intervals:
            events.append((interval.start,1))
            events.append((interval.end,-1))
        
        events=sorted(events)
        return events


# Time complexity: O(n log(n))
# Space comlexity: O(n)