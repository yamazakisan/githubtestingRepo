from typing import List

def partition(numbers:List[int], low:int, high:int)->int:
    i = low - 1
    pivot = numbers[high]
    for j in range (low,high):
        if numbers[j] <= pivot:
            i += 1
            numbers[i] ,numbers[j] = numbers[j],numbers[i]
    numbers[i+1] ,numbers[high] = numbers[high],numbers[i+1]
    return i+1

def marge(numbers: List[int]) -> None:
    if len(numbers) = 1:
        return numbers
    middle = len(numbers)/2
    left = marge(numbers(:middle))
    right = marge(middle:)
    
    i = j = 0
    for     　




    _quicksort(numbers,0,len(numbers)-1)
    return numbers
     

if __name__ == '__main__':
    nums = [4,1,5,8,0,34,9,2]
    print(quick(nums))