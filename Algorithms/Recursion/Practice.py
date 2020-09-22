# -------------------------------- Implementation --------------------------------
# given an array of integers, find all distinct combinations of a given length k
def distinct_combos(array, k, return_arr):
    if len(array) == k:
        return_arr.append(array)
        return return_arr
    return distinct_combos(array[1:], k, return_arr)


def string_permuations(string):
    if len(string) == 0:
        return string
    



# -------------------------------- Testing --------------------------------
array = [1, 2, 4, 1, 2, 1, 5]
k = 3
return_arr = []
print(f"distinct combos = {distinct_combos(array, k, return_arr)}")