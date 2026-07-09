class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # count={}

        # for i , num in enumerate(nums):
        #     diff = target - num

        #     if diff in count:
        #         return [count[diff],i]

        #     count[num] = i


        # return


        # Pair each number with its original index
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        indexed_nums.sort()  # Sorts by the number value
        
        l = 0
        r = len(nums) - 1
        
        while l < r:
            current_sum = indexed_nums[l][0] + indexed_nums[r][0]
            if current_sum == target:
                return sorted([indexed_nums[l][1], indexed_nums[r][1]])
            elif current_sum < target:
                l += 1
            else:
                r -= 1

      



        
        