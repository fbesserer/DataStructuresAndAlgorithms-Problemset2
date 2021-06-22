def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    start_idx = 0
    end_idx = len(input_list) - 1

    while start_idx <= end_idx:
        mid_idx = (end_idx - start_idx) // 2 + start_idx

        if number == input_list[mid_idx]:
            return mid_idx

        if input_list[start_idx] <= input_list[mid_idx]:  # pivot point on the right side
            if input_list[start_idx] <= number < input_list[mid_idx]:
                end_idx = mid_idx - 1  # left side
            else:
                start_idx = mid_idx + 1  # right side
        else:  # pivot point left
            if input_list[mid_idx] < number <= input_list[end_idx]:
                start_idx = mid_idx + 1  # right side
            else:
                end_idx = mid_idx - 1  # left side
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


arr = [3,4,6,15,625,13468,0,1,2]
arr1 = [13468,4,6,15,625,626,627,628,630]
arr2 = [4,6,15,625,626,627,628,1,2,3]
arr3 = [3,5,37,41,80,85, 91,1]

test_function([arr, 13468]) # pass
test_function([arr1, 13468]) # pass
test_function([arr, 6]) # pass
test_function([arr1, 6]) # pass
test_function([arr, 4]) # pass
test_function([arr1, 4]) # pass
test_function([arr, 10]) # pass
test_function([arr1, 10]) # pass
test_function([arr, 630]) # pass
test_function([arr1, 630]) # pass
test_function([arr, 0]) # pass
test_function([arr1, 0]) # pass

for i in range(100):
    result = rotated_array_search(arr3, i)
    if result != -1:
        print(f"Wert {i} in Array an Index :{result}")


