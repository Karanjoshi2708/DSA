class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=set(nums)

        for i in nums:
            if i in a:
                a.remove(i)

            else:
                return True

        return False

        