from functools import cache


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod=10**9+7
        @cache
        def fn(i,x):
            if i==goal:
                return x==n

            ans=0
            if x<n:
                ans+=(n-x)*fn(i+1,x+1)

            if k<x:
                ans+=(x-k)*fn(i+1,x)

            return ans%mod

        return fn(0,0)