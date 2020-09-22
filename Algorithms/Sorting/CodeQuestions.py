# -------------------------------- Basic Sort Implementations --------------------------------
# largest item "bubbles" up to the top
def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                # swap
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

# find smallest item and move it to the lowest index, repeat
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        # swap once it has found the lowest value and index
        array[i], array[min_index] = array[min_index], array[i]
    return array


# efficient for when a list is "almost" sorted (i.e. good for insertions made after a sort has been done to re-sort)
# works well with small data sets
def insertion_sort(array):
    # Traverse through 1 to len(arr)
    for i in range(1, len(array)):
        key = array[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


# -------------------------------- Divide and Conquer Sort Implementations --------------------------------
# O(nlogn), stable - elements that are the same will keep same order in an array
def merge(left, right):
    merged_array=[]
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged_array.append(left[left_index])
            left_index += 1
        else:
            merged_array.append(right[right_index])
            right_index += 1
    if left_index < len(left):
        while left_index < len(left):
            merged_array.append(left[left_index])
            left_index += 1
    if right_index < len(right):
        while right_index < len(right):
            merged_array.append(right[right_index])
            right_index += 1

    # print(f"merged array = {merged_array}")
    return merged_array


def merge_sort(array):
    if len(array) <= 1:
        return array
    middle = len(array)//2
    left = array[:middle]
    right = array[middle:]
    # print(f"left = {left}")
    # print(f"right = {right}")
    # recursive divide and conquer
    return merge(merge_sort(left), merge_sort(right))


# Uses a pivoting technique to break array into smaller arrays to be used with divide and conquer
# on avg, best sorting algorithm (time) like merge sort. Less memory space required that merge sort.
# can have a worst case of O(n^2), however
def quick_sort(array):
    pass



# -------------------------------- Testing --------------------------------
array = [99, 44, 6, 2, 1, 5, 63, 87, 293, 4, 0]
print(f"bubble sort = {bubble_sort(array)}")

array = [99, 44, 6, 2, 1, 5, 63, 87, 293, 4, 0]
print(f"selection sort = {selection_sort(array)}")

array = [99, 44, 6, 2, 1, 5, 63, 87, 293, 4, 0]
print(f"insertion sort = {insertion_sort(array)}")

array = [99, 44, 6, 2, 1, 5, 63, 87, 293, 4, 0]
print(f"merge sort = {merge_sort(array)}")
