class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #Check if the list has more than one element
        if len(nums) < 2:
            return nums

        #Get the midpoint of the list
        midpoint = len(nums) // 2
        #Split the list in half
        list1, list2 = nums[:midpoint], nums[midpoint:]

        #Do this recursively to sort the lists
        left_side_sorted = self.sortArray(list1)
        right_side_sorted = self.sortArray(list2)

        #Merge the final sorted lists from the left and right side together(Also used during the recursive calls)
        return self.merge(left_side_sorted, right_side_sorted)
    
    def merge(self, first: List[int], second: List[int]) -> List[int]:
        #Create an array that will hold the final solutions
        final = []
        #Create variables to keep track of the indexes
        i, j = 0, 0

        #Loop through both sorted lists using a while loop
        while i < len(first) and j < len(second):
            #compare the items at the indexes of i and j
            if first[i] <= second[j]:
                #append the smaller or equal ones to the final list
                final.append(first[i])
                #Increment i to move to the next index
                i += 1
            else:
                #append the smaller or equal one to the final list(if its the second list with a smaller item)
                final.append(second[j])
                #Increment j to move to the next index
                j += 1
        
        #If there any left overs after the loop ended from either list, append them to the final list
        final.extend(first[i:])
        final.extend(second[j:])

        #return the final merged list
        return final


        