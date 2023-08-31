class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if not roads: return 0
        flatten = list(chain.from_iterable(roads))
        helper = Counter(flatten)

        helper2 = []

        for k, v in helper.items():
            helper2.append([k, v])

        helper2.sort(key=lambda x: x[1])

        combos = []

        for i in range(len(helper2)):
            for j in range(len(helper2)):
                if i != j:
                    if [helper2[i][0], helper2[j][0]] in roads or [helper2[j][0], helper2[i][0]] in roads:
                        combos.append(helper2[i][1] + helper2[j][1] - 1)
                    else:
                        combos.append(helper2[i][1] + helper2[j][1])

        return max(combos)






