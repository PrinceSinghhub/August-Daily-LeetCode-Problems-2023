class Solution:

    def Tabulation_Methode(self, row, coll, dp, maze):

        for i in range(row):
            for j in range(coll):

                if maze[i][j] == 1:
                    dp[i][j] = 0
                    continue

                if i == 0 and j == 0:
                    dp[i][j] = 1
                    continue

                up = 0
                left = 0

                if i > 0:
                    up = dp[i - 1][j]

                if j > 0:
                    left = dp[i][j - 1]

                dp[i][j] = up + left
        print(dp)
        return dp[row - 1][coll - 1]

    def uniquePathsWithObstacles(self, maze):

        r = len(maze)
        c = len(maze[0])

        dp = []

        for i in range(r):
            col = [-1] * c
            dp.append(col)

        # print(dp)

        ans = self.Tabulation_Methode(r, c, dp, maze)
        return ans
