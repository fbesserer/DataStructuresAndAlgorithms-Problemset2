def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    heapsort(input_list)
    sum1 = 0
    sum2 = 0
    exponent1 = len(input_list) // 2 if len(input_list) % 2 != 0 else len(input_list) // 2 - 1
    exponent2 = len(input_list) // 2 - 1
    while input_list:
        sum1 += input_list.pop() * 10 ** exponent1
        if exponent2 >= 0:
            sum2 += input_list.pop() * 10 ** exponent2
        exponent1 -= 1
        exponent2 -= 1
    return sum1, sum2


def heapsort(arr):  # O(n log n)
    # convert the array into a max heap
    build_heap(arr)
    # swap head node with last node
    for swap in range(len(arr)-1, -1, -1):
        arr[0], arr[swap], = arr[swap], arr[0]
        heapify(arr, swap, 0)


def build_heap(arr):  # O(n log n)
    # go through every parent backwards and heapify it
    last_parent = (len(arr) - 1) // 2
    for parent in range(last_parent, -1, -1):
        heapify(arr, len(arr), parent)


def heapify(arr, arr_length, parent_idx):  # O(log n)
    while True:
        largest_idx = parent_idx
        left_child_idx = 2 * parent_idx + 1
        right_child_idx = 2 * parent_idx + 2

        if left_child_idx < arr_length and arr[left_child_idx] > arr[largest_idx]:
            largest_idx = left_child_idx
        if right_child_idx < arr_length and arr[right_child_idx] > arr[largest_idx]:
            largest_idx = right_child_idx

        if largest_idx == parent_idx:
            break
        else:
            arr[largest_idx], arr[parent_idx] = arr[parent_idx], arr[largest_idx]  # swap
            parent_idx = largest_idx


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_case = [1, 5, 3, 4]
rearrange_digits(test_case)

test_case = [[1, 2, 3, 4, 5], [542, 31]]
test_function(test_case)

test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

test_case = [[1, 5, 6, 2, 4, 9, 8], [9641, 852]]
test_function(test_case)

test_case = [[8], [8]]
test_function(test_case)

test_case = [[], []]
test_function(test_case)

# time complexity of heapsort: O(n log n)
# time complexity of building the sums: n/2
