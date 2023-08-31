class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = collections.deque()
        for i, num in enumerate(nums):

            while window and num >= nums[window[-1]]:
                window.pop()

            window.append(i)

            if i >= k - 1:
                res.append(nums[window[0]])

            if i - window[0] + 1 == k:
                window.popleft()

        return res