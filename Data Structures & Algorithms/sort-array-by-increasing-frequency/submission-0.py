from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        self.counts = Counter(nums)
        return self.MergeSort(nums)

    def MergeSort(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums

        mid = len(nums) // 2
        nums1, nums2 = nums[:mid], nums[mid:]
        left_sorted = self.MergeSort(nums1)
        right_sorted = self.MergeSort(nums2)

        return self.merge(left_sorted, right_sorted)

    def merge(self, first, second):
        final = []
        i, j = 0, 0

        while i < len(first) and j < len(second):
            f1, f2 = self.counts[first[i]], self.counts[second[j]]
            
            # Condition 1: Left item has lower frequency (comes first)
            if f1 < f2:
                final.append(first[i])
                i += 1
            # Condition 2: Right item has lower frequency (comes first)
            elif f1 > f2:
                final.append(second[j])
                j += 1
            # Condition 3: Frequencies are equal, break tie by larger value (descending)
            else:
                if first[i] >= second[j]:
                    final.append(first[i])
                    i += 1
                else:
                    final.append(second[j])
                    j += 1

        final.extend(first[i:])
        final.extend(second[j:])

        return final

        


        