class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        return self.mergeSort(arr1, arr2)
        
    def mergeSort(self, arr: List, distinct: List) -> List:
        if len(arr) < 2:
            return arr

        mid = len(arr) // 2
        arr1, arr2 = arr[:mid], arr[mid:]
        left_sorted_side = self.mergeSort(arr1, distinct)
        right_sorted_side = self.mergeSort(arr2, distinct)

        return self.merge(left_sorted_side, right_sorted_side, distinct)

    def merge(self, first: List, second: List, distinct: List) -> List:
        final = []
        i, j = 0, 0
        
        # Create a mapping for arr2 order; use a large value for elements not in arr2
        order = {val: idx for idx, val in enumerate(distinct)}

        while i < len(first) and j < len(second):
            # Use .get() with a default value to handle elements not in arr2
            # We add the value itself (e.g., 1000 + value) to ensure ascending order for missing elements
            left_val = order.get(first[i], 2000 + first[i])
            right_val = order.get(second[j], 2000 + second[j])

            if left_val < right_val:
                final.append(first[i])
                i += 1
            else: 
                final.append(second[j])
                j += 1
                
        final.extend(first[i:])
        final.extend(second[j:])
        return final