class Solution:
    def canCross(self, stones: List[int]) -> bool:
        d = {stones[i] : i for i in range(len(stones))}
        @lru_cache(None)
        def dfs(i,k):
            if k<1:
                return False
            if i==len(stones)-1:
                return True
            if stones[i]+k not in d:
                return False
            x = d[stones[i]+k]
            return dfs(x,k-1) or dfs(x,k) or dfs(x,k+1)
        return dfs(0,1)