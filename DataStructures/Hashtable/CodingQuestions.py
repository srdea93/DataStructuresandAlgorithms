# ----------------------------- Problem 1: Find First Recurring Character -----------------------------
# Given an array = [2,5,1,2,3,5,1,2,4]:
# should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]
# should return 1

# Given an array [2,3,4,5]
# should return None


def first_recurring_char(input_list):
    characters = {}
    for character in input_list:
        if character not in characters:
            characters[character] = 1
        else:
            return character
    return None

# ----------------------------- Test Problem 1: Find First Recurring Character -----------------------------
test1=[2,5,1,2,3,5,1,2,4]
test2=[2,1,1,2,3,5,1,2,4]
test3=[2,3,4,5]
tests = [test1,test2,test3]

for test in tests:
    print(first_recurring_char(test))


