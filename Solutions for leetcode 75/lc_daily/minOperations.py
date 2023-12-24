class Solution:
    def minOperations(self, s: str) -> int:
        count_0 = 0

        #for string starting with 0
        for i in range(len(s)):
            if(i%2 ==0 and s[i] !='0') or (i%2 == 1 and s[i] !='1'):
                count_0+=1

        count_1 = 0
        #for string starting with 1
        for i in range(len(s)):
            if(i%2 == 0 and s[i] !='1') or (i%2 == 1 and s[i] !='0'):
                count_1+=1
        return min(count_0, count_1)



        