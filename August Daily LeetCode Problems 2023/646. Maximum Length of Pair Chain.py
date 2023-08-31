import math
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        ans = 0
        prevEnd = -math.inf

        def get_second(pair):
            return pair[1]

        pairs.sort(key=get_second)

        for s, e in pairs:
            if s > prevEnd:
                ans += 1
                prevEnd = e

        return ans
