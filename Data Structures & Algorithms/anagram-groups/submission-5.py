class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # d = defaultdict(list)

        # for i in strs:
        #     count = [0]*26

        #     for c in i:
        #         count[ord(c)-ord("a")] +=1

        #     d[tuple(count)].append(i)


        # return list(d.values())

        d = defaultdict()

        for i in strs:

            ss = sorted(i)

            if tuple(ss) not in d:
                d[tuple(ss)] = []
                
            d[tuple(ss)].append(i)

        return list(d.values())



    






        
