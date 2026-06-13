class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_length = len(nums)
        set_nums_length = len(set(nums))
        if nums_length == set_nums_length:
            return False
        return True
        