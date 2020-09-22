# Algorithm for factorial multiplication
# -------------------------------- Recursive --------------------------------
def recursive_factorial(num):
    # base case
    if num <= 1:
        return 1
    # recursive case
    return (num*recursive_factorial(num-1))


def fib_recursive(num):
    if num == 0:
        return 0
    elif num <= 2:
        return 1
    return fib_recursive(num-1)+fib_recursive(num-2)


def reverse_string_recursive(string):
    if len(string) == 0:
        return string
    return reverse_string_recursive(string[1:]) + string[0]


# -------------------------------- Iterative --------------------------------
def iterative_factorial(num):
    total = 1
    while num > 1:
        total = total*num
        num -= 1
    return total


def fib_iterative(num):
    fib_arr = [0 for x in range(num+1)]
    fib_arr[0] = 0
    fib_arr[1] = 1
    for index in range(2, num+1):
        fib_arr[index] = fib_arr[index-2] + fib_arr[index-1]
    return fib_arr[num]


# -------------------------------- Test --------------------------------
num = 8

print(f"num = {num}")
print(f"recursive factorial = {recursive_factorial(num)}")
print(f"iterative factorial = {iterative_factorial(num)}")
print(f"recursive fibonacci = {fib_recursive(num)}")
print(f"iterative fibonacci = {fib_iterative(num)}")

string = "hello"

print(f"reverse string recursive = {reverse_string_recursive(string)}")

