class Solution:

    def encode(self, strs: List[str]) -> str:
        #["karan","joshi"]
        # 5#karan5#joshi

        result = ""

        for i in strs:
            result += str(len(i)) + "#" + i

        return result

    def decode(self, s: str) -> List[str]:

        result = []
        i=0

        while i < len(s):
            j=i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])  # bacause of double digit length 
            result.append(s[j+1 : j+1+length])
            i = j + 1 + length

        return result

            
