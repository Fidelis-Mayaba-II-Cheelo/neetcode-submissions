import statistics
import numpy as np

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        #convert the strings into lists
        s_list = list(s)
        t_list = list(t)
        #sort both arrays
        s_list_sorted = self.mergeSort(s_list)
        t_list_sorted = self.mergeSort(t_list)
        #Convert them into numpy arrays
        s_list_np = np.array(s_list_sorted)
        t_list_np = np.array(t_list_sorted)
        #if they are not the same return false
        return np.array_equal(s_list_np, t_list_np)


    def mergeSort(self, arr: List) -> List:
        if len(arr) < 2:
            return arr
        
        #Divide the array in half
        mid = len(arr) // 2
        arr1, arr2 = arr[:mid], arr[mid:]

        left_sorted = self.mergeSort(arr1)
        right_sorted = self.mergeSort(arr2)

        return self.merge(left_sorted, right_sorted)


    def merge(self, first: List, second: List) -> List:
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

        


        