class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        a = []
        for i in range(len(nums)):

            mult = 1

            for j in range(i):
                mult *= nums[j]

            
            for j in range(i+1 , len(nums)):
                mult *= nums[j]

            a.append(mult)

        return a

        