# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):

        def f(arr):
            # Base conditions
            if len(arr) < 1:
                return [None]
            if len(arr) == 1:
                return [TreeNode(arr[0])]

            ret = []
            for i, item in enumerate(arr):
                leftTrees = f(arr[0:i])
                rightTrees = f(arr[i + 1:])

                for lt in leftTrees:
                    for rt in rightTrees:
                        r = TreeNode(arr[i])
                        r.left = lt
                        r.right = rt
                        ret.append(r)
            return ret

        return f(list(range(1, n + 1)))