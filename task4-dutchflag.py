def sort_012(input_list):  
    zeros, ones, twos = [], [], []
    for item in input_list:
        if item is 0:
            zeros.append(item)
        elif item is 1:
            ones.append(item)
        else:
            twos.append(item)

    return zeros + ones + twos

def test_function(test_case):
    sorted_array = sort_012(test_case)
   
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    test_function([0, 0, 2, 2, 2, 1])
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
    test_function([0, 1, 2])
    test_function([0])
    test_function([2])
    
