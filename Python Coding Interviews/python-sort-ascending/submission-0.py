from typing import List

def insertion_sort(arr: List):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr

def sort_words(words: List[str]) -> List[str]:
    return insertion_sort(words)

def sort_numbers(numbers: List[int]) -> List[int]:
    return insertion_sort(numbers)

def sort_decimals(numbers: List[float]) -> List[float]:
    return insertion_sort(numbers)






# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))
