class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        if len(s)!=len(t):
            return False

        a=[]
        b=[]
        for i in s:
            a.append(i)
        
        for i in t:
            b.append(i)


        for i in a:
            if i in b:
                b.remove(i)


        if len(b)==0:
            return True

        return False


            

        