class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        what: you need to find the gcd of the two strings, and then take subset of any string

        why: because if the gcd is the greatest common divisor that divides both the strings and gives zero as the remainder and that would be the answet

        how: need to add both the strings and see if s1+s2 == s2+s1, this is because both s1 and s2 are made of repeating the gcd. if they are not equal then not the answer
        """
        if(str1+str2 == str2+str1):
            ans = gcd(len(str1), len(str2))
            return str1[0:ans]
        else:
            return ""
        

    def gcd(a, b):

        while(b % a != 0):
            b = a
            a = b%a
        return a




        