def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    idx = 0
    for digit in input_list[:]:
        if digit == 0:
            input_list.pop(idx)  # O(n)
            input_list.insert(0, digit)  # O(n)
            idx += 1
        elif digit == 2:
            input_list.pop(idx)  # O(n)
            input_list.append(digit)  # O(1)
        else:
            idx += 1
    return input_list


def sort_012_1(input_list):
    # time complexity O(n) due to no expensive insert() and pop() functions, space O(n)
    arr0 = []
    arr1 = []
    arr2 = []
    for digit in input_list:
        if digit == 0:
            arr0.append(digit)
        elif digit == 2:
            arr2.append(digit)
        else:
            arr1.append(digit)
    return arr0 + arr1 + arr2


def three_pointer_approach(input_list):
    low_pointer = 0
    mid_pointer = 0
    high_pointer = len(input_list) - 1
    while mid_pointer <= high_pointer:
        if input_list[mid_pointer] < 1:
            input_list[mid_pointer], input_list[low_pointer] = input_list[low_pointer], input_list[mid_pointer]
            mid_pointer += 1
            low_pointer += 1
        elif input_list[mid_pointer] == 1:
            mid_pointer += 1
        else:
            input_list[mid_pointer], input_list[high_pointer] = input_list[high_pointer], input_list[mid_pointer]
            high_pointer -= 1
    return input_list


def test_function(test_case):
    sorted_array = three_pointer_approach(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


print(three_pointer_approach([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]))
# test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
# test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
# test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
# test_function([2, 2, 2, 2, 2, 2, 2])
# test_function([1, 1, 1, 1, 1, 1])
# test_function([0, 0, 0, 0, 0, 0])
# test_function([])

# runtime = worst case O(n²) - single traversal