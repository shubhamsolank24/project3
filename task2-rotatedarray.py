from algorithms import linear_search, binary_search


def rotated_array_search(input_list, number):
   
    if not input_list:
        return -1

    pivot_idx = find_pivot(input_list, 0, len(input_list) - 1)  
    if pivot_idx == len(input_list) - 1:
        return binary_search(input_list, 0, len(input_list) - 1, number)  
    elif input_list[0] <= number <= input_list[pivot_idx]:
        input_list = input_list[:pivot_idx + 1]
        return binary_search(input_list, 0, len(input_list) - 1, number) 
    elif number > input_list[-1]:
        return -1
    else:
        input_list = input_list[pivot_idx + 1:]
        return pivot_idx + 1 + binary_search(input_list, 0, len(input_list) - 1, number)  


def find_pivot(array, left_idx, right_idx):
    if right_idx == left_idx:
        return left_idx  # right_idx

    mid_idx = (left_idx + right_idx) // 2

    left = array[left_idx]
    mid = array[mid_idx]

    if mid > array[mid_idx + 1]: 
        return mid_idx
    if mid < array[mid_idx - 1]: 
        return mid_idx - 1

    if left > mid:  
        return find_pivot(array, left_idx, mid_idx)
    
    return find_pivot(array, mid_idx + 1, right_idx)  


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

print("Calling function with non-rotated array: [1, 2, 3, 4], target value = 3")
test_function([[1, 2, 3, 4], 3])

print("Calling function with rotated array: [6, 7, 8, 9, 10, 1, 2, 3, 4], target value = 1")
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])

print("Calling function with non-list input: 10, target value = 5")
test_function([[], 5])

print("Calling function with array: [6, 7, 8, 9, 10, 1, 2, 3, 4], non-exist target value = 5")
test_function([[6, 7, 8, 1, 2, 3, 4], 5])

print("Calling function with empty array: [], target value = 5")
test_function([[], 5])


