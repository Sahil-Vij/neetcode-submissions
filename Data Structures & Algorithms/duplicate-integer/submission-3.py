class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        selfish=set()
        for i in range(len(nums)):
            if nums[i] in selfish:
                return True
            else:
                selfish.add(nums[i])
        return False
            