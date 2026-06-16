class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #create a dict for the original names and heights
        mapped_dict = dict(zip(heights, names))
        #sort the list of heights and put that list aside
        sorted_heights = self.quick_sort(heights, 0, len(heights) - 1)
        #list that will store the new sorted names
        new_names = []
        #iterate over sorted list(step, stop) in -1 because we are doing it in descending order
        for i in range(len(sorted_heights)-1, -1, -1):
            #Get the current highest height value in our sorted list
            target_height = sorted_heights[i]
            #Use it to map to the name in our dictionary and append the name to our new_names list
            new_names.append(mapped_dict[target_height])
        return new_names


    def quick_sort(self, nums, low, high):
        if low < high:
            #Get the index of the perfectly placed pivot
            middle = self.partition(nums, low, high)
            #Left side of the perfectly placed pivot
            self.quick_sort(nums, low, middle -1)
            #Right side of the perfectly placed pivot
            self.quick_sort(nums, middle + 1, high)
        return nums

    def partition(self, nums, low, high):
        #Set the pivot to the item at index high
        pivot = nums[high]
        i = low - 1

        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        #After all the swapping has taken place and we reach the end of the list, swap the pivot value with the value at i+1
        nums[i+1], nums[high] = nums[high], nums[i+1]
        #return the index of the perfectly placed old pivot, this will be our dividing point
        return i+1

        