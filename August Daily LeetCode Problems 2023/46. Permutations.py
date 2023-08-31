class Solution:

    def findAllPermutations(self, nums, ans, visiteMap, ds):

        if len(ds) == len(nums):
            ans.append(ds[:])
            return

        for i in range(len(nums)):

            if visiteMap[i] == False:
                visiteMap[i] = True
                ds.append(nums[i])
                self.findAllPermutations(nums, ans, visiteMap, ds)
                ds.remove(nums[i])
                visiteMap[i] = False

        print(visiteMap)

    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        visiteMap = [False] * len(nums)
        ds = []

        self.findAllPermutations(nums, ans, visiteMap, ds)

        return ans


# optimized Approch
class Solution:

    def swap(self, i, index, nums):
        temp = nums[i]
        nums[i] = nums[index]
        nums[index] = temp

    def findAllPermutations(self, index, nums, ans):

        if index == len(nums):
            ds = []
            for i in range(len(nums)):
                ds.append(nums[i])

            ans.append(ds)
            return

        for i in range(index, len(nums)):
            self.swap(i, index, nums)
            self.findAllPermutations(index + 1, nums, ans)
            self.swap(i, index, nums)

    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        self.findAllPermutations(0, nums, ans)

        return ans
