class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0: return 0

        def isValidPair(threshold):
            validPair, i = 0, 0
            while i < len(nums)-1:
                if abs(nums[i]-nums[i+1]) <= threshold:
                    validPair+=1
                    i+=2
                else: i+=1
                if validPair == p: return True
            return False

        l, r = 0, 10**9
        res = 10**9

        nums.sort()

        while l<=r:
            mid = (l+r)//2
            if isValidPair(mid):
                res = mid
                r = mid - 1
            else: l = mid + 1
        return res