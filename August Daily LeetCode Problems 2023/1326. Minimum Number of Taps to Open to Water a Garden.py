class Solution:
    def minTaps(self, n, ranges):
        min_pos = 0
        max_pos = 0
        count = 0

        while max_pos < n:
            for i in range(len(ranges)):
                if i - ranges[i] <= min_pos and i + ranges[i] >= max_pos:
                    max_pos = i + ranges[i]

            if max_pos == min_pos:
                return -1

            count += 1
            min_pos = max_pos

        return count
