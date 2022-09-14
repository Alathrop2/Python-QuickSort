

def quick_sort(integers):
    # Your code here.
    length = len(integers)
    if length <= 1:
        return integers
    else:
      # the .pop() is selecting a rando, number in the array, and setting it as the pivot point
        pivot = integers.pop()
    numbers_greater = []
    numbers_lower = []
    # this for loop is selecting the pivot point and moving the remaining numbers into arrays depending on if they are larger or smaller than the pivot number
    for number in integers:
        if number > pivot:
            numbers_greater.append(number)

        else:
            numbers_lower.append(number)
    return quick_sort(numbers_lower) + [pivot] + quick_sort(numbers_greater)


print(quick_sort([5, 6, 2, 1, 3, 4, 9, 8, 30, 55, 60, 70, 85, 90, 68]))


pass
