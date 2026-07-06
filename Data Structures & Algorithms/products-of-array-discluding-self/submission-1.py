class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # a = []
        # for i in range(len(nums)):

        #     mult = 1

        #     for j in range(i):
        #         mult *= nums[j]

            
        #     for j in range(i+1 , len(nums)):
        #         mult *= nums[j]

        #     a.append(mult)

        # return a


        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1 , -1 , -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result

        