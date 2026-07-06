class Solution:
    def isPalindrome(self, s: str) -> bool:

        # a = []
        # for i in s:
        #     if i.isalnum():
        #         a.append(i.lower())

        # return a==a[::-1]


        l , r = 0 , len(s)-1


        while l < r :
            while l < r and not self.alphanum(s[l]):
                l +=1
            while r>l and not self.alphanum(s[r]):
                r -=1

            if s[l].lower() != s[r].lower():
                return False

            l +=1
            r -=1
        
        return True




    def alphanum(self, c):
        return (ord("A")<=ord(c) and ord(c)<=ord("Z")  or
                ord("a")<=ord(c) and ord(c)<=ord("z")  or
                ord("0")<=ord(c) and ord(c)<=ord("9")  )
        