import collections
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = [[-v, k] for k, v in collections.Counter(s).items()]
        heapq.heapify(heap)
        ans = ""

        while len(heap) > 1:
            a, ak = heapq.heappop(heap)
            b, bk = heapq.heappop(heap)
            ans += ak + bk
            a, b = -a, -b
            if a - 1 > 0:
                heapq.heappush(heap, [-(a - 1), ak])
            if b - 1 > 0:
                heapq.heappush(heap, [-(b - 1), bk])

        if not heap:
            return ans
        if -heap[0][0] > 1:
            return ""
        return ans + heap[0][1]


