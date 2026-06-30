class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums_length = len(nums) - 1
        sorted_nums = self.mergeSort(nums)
        return (sorted_nums[nums_length] * sorted_nums[nums_length - 1]) - (sorted_nums[0] * sorted_nums[1])

    def mergeSort(self, nums: List[int]):
        if len(nums) < 2:
            return nums

        mid = len(nums) // 2
        nums1, nums2 = nums[:mid], nums[mid:]
        
        left_side = self.mergeSort(nums1)
        right_side = self.mergeSort(nums2)

        return self.merge(left_side, right_side)

    def merge(self, first: List[int], second: List[int]) -> List[int]:
        final = []
        i, j = 0, 0

        while i < len(first) and j < len(second):
            if first[i] < second[j]:
                final.append(first[i])
                i += 1
            else:
                final.append(second[j])
                j += 1

        final.extend(first[i:])
        final.extend(second[j:])
        return final 
