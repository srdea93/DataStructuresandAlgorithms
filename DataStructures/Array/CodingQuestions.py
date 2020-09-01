# ----------------------------- Problem 1: Reverse a String -----------------------------
# 1) actually reverse the string array using a for loop into a new string (not in place)
# 2) use python index slice (in place)


def reverse_string_not_in_place(string): # O(n)
    if type(string) is not str or len(string) < 1 or string is None:
        return None
    elif len(string) == 1:
        return string
    else:
        rstring = []
        for i in range(len(string), 0, -1):
            # account for the index and len being off by 1
            rstring.append(string[i-1])
        return ''.join(rstring)


def reverse_string_in_place(string): # O(n) - I think
    if type(string) is not str or len(string) < 1 or string is None:
        return None
    elif len(string) == 1:
        return string
    else:
        rstring = string[::-1]
        return rstring

# ----------------------------- Test Problem 1: Reverse a String -----------------------------
string = "Vinnie"
print(reverse_string_not_in_place(string))
print(reverse_string_in_place(string))


# ----------------------------- Problem 2: Merge Two Sorted Arrays -----------------------------
# inputs: array1, array2
# output: merged sorted array
# uses 2 pointers to traverse each array, at each iteration the pointers compare and whichever is less is added to the
# merged list and that pointer is incremented until it reaches the end. Then, whichever pointer is not at the end
# continues to iterate up and adds the rest of that array to the merged list

def merge_sorted_array_not_in_place(array1, array2):
    array1_index = 0
    array2_index = 0
    merged_array = []

    while array1_index < len(array1) and array2_index < len(array2): #O(n + m)
        if array1[array1_index] <= array2[array2_index]:
            merged_array.append(array1[array1_index])
            array1_index += 1
        else:
            merged_array.append(array2[array2_index])
            array2_index += 1
    # add the rest of array2
    if array1_index == len(array1):
        while array2_index < len(array2): # O(n)
            merged_array.append(array2[array2_index])
            array2_index += 1
    # add the rest of array1
    else:
        while array1_index < len(array1): # O(m)
            merged_array.append(array1[array1_index])
            array1_index += 1
    return merged_array

# uses two pointers to compare. If value @ array2 pointer is < value @ array1 pointer, array2 value is inserted
# at array 1 pointer value, array1 pointer + 1, array2 pointer +1
def merge_sorted_array_in_place(array1, array2):
    array1_index = 0
    array2_index = 0

    while array1_index < len(array1) and array2_index < len(array2): # O(n + m)
        if array1[array1_index] > array2[array2_index]:
            array1.insert(array1_index, array2[array2_index])
            array1_index += 1
            array2_index += 1
        else:
            array1_index += 1
    if array1_index == len(array1):
        while array2_index < len(array2): # O(n)
            array1.append(array2[array2_index])
            array2_index += 1
    return array1

# ----------------------------- Test Problem 2: Merge Two Sorted Arrays -----------------------------
array1 = [1,2,5,7,8,9,13]
array2 = [2,4,6,8,12]
print(merge_sorted_array_not_in_place(array1, array2))
print(merge_sorted_array_in_place(array1, array2))

# Further Practice
# X Two Sum - https://leetcode.com/problems/two-sum/description/
# X Maximum Subarray - https://leetcode.com/problems/maximum-subarray/description/
# X Move Zeroes - https://leetcode.com/problems/move-zeroes/description/
# X Contains Duplicates - https://leetcode.com/problems/contains-duplicate/description/
# X Rotate Arrays -  https://leetcode.com/problems/rotate-array/description/ - Try with size O(1) eventually
