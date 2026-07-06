class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # d = {}

        # for i in nums:
        #     d[i]=d.get(i,0) + 1

        # # sorting by values 
        # d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

        # # using slicing
        # return list(d.keys())[:k]

        a = [[] for i in range(len(nums)+1)]

        d ={}

        result = []


        for i in nums:
            d[i]=d.get(i,0) + 1

        # bucket sort : take frequency or count as index
        #               and number as value 
        for n , c in d.items():
            a[c].append(n)

        
        for i in range(len(a)-1 , 0 , -1):
            for j in a[i]:
                result.append(j)
                if len(result)==k:
                    return result


        


            


        




        

                

            

        
            

            

