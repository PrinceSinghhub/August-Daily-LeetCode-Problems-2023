class Solution:
    def searchMatrix(self, mat, target):

        n = len(mat)
        m = len(mat[0])

        low = 0
        hig = (n * m) - 1

        while low <= hig:
            mid = low + (hig - low) // 2

            row = mid // m
            coll = mid % m

            if mat[row][coll] == target:
                return True

            if mat[row][coll] > target:
                hig = mid - 1

            else:
                low = mid + 1

        return False


