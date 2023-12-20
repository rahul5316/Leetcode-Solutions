class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        mx = 0
        for i in candies:
            if(mx < i):
                mx = i
        ans = []

        for i in candies:
            if(extraCandies+ i >= mx):
                ans.append(True)
            else:
                ans.append(False)
        return ans
        