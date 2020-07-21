def rotated_array_search(input_list, number):
   
    if not isinstance(input_list, list):
        return -1

    if len(input_list) == 0:
        return -1

    left_idx = 0
    right_idx = len(input_list) - 1

    while right_idx > left_idx + 1:
        middle_idx = (right_idx + left_idx) // 2

        middle_value = input_list[middle_idx]

        
        if middle_value == number:
            return middle_idx

      
        if input_list[left_idx] < middle_value < input_list[right_idx]:
            if number > middle_value:
                left_idx = middle_idx
            else:
                right_idx = middle_idx
       
        elif middle_value > input_list[left_idx] and middle_value > input_list[right_idx]:
            if input_list[left_idx] <= number < middle_value:
                right_idx = middle_idx
            else:
                left_idx = middle_idx
        
        elif middle_value < input_list[left_idx] and middle_value < input_list[right_idx]:
            if middle_value < number <= input_list[right_idx]:
                left_idx = middle_idx
            else:
                right_idx = middle_idx

    
    if input_list[left_idx] == number:
        return left_idx
    elif input_list[right_idx] == number:
        return right_idx
    else:
        return -1


def linear_search(input_list, number):
    for idx, element in enumerate(input_list):
        if element == number:
            return idx
    return -1


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


