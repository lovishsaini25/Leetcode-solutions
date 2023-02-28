class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort()
        comparator = intervals[0]
        result = []
        index = 0
        for i in range(1, len(intervals)):
            if(comparator[1] >= intervals[i][0]):
                comparator = [comparator[0], max(comparator[1], intervals[i][1])]
            else:
                result.append(comparator)
                comparator = intervals[i]
            if i == len(intervals)-1:
                result.append(comparator)
        
        return result