class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = self.mergeSort(heights)
        expected = heights
        count = 0
        for i in range(len(heights)):
            if sorted_heights[i] != expected[i]:
                count += 1
        return count
        

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