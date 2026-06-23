from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sorted_array = self.mergeSort(nums)
        return sorted_array[len(sorted_array) // 2]


    def mergeSort(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums

        mid = len(nums) // 2
        nums1, nums2 = nums[:mid], nums[mid:]

        left_sorted = self.mergeSort(nums1)
        right_sorted = self.mergeSort(nums2)

        return self.merge(left_sorted, right_sorted)


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

        