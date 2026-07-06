class Solution:
    def isPalindrome(self, s: str) -> bool:

        a = []
        for i in s:
            i=i.lower()
            if (97<=ord(i) and ord(i) <=122)  or (48<=ord(i) and ord(i) <=57):
                a.append(i)

        return a==a[::-1]

        