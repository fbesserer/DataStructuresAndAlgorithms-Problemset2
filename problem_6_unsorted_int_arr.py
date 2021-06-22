## Example Test Case of Ten Integers
import random

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return
    min = ints[0]
    max = ints[0]
    # loop over vals and check if smaller than min or greater than max
    for int in ints:
        if int < min:
            min = int
        elif int > max:
            max = int

    return (min, max)


l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(1, 9)]  # a list containing 1 - 8
random.shuffle(l)
print ("Pass" if ((1, 8) == get_min_max(l)) else "Fail")

l = [i for i in range(2, 5)]  # a list containing 2 - 4
random.shuffle(l)
print ("Pass" if ((2, 4) == get_min_max(l)) else "Fail")

l = [i for i in range(-10, -1)]  # a list containing -10 - -1
random.shuffle(l)
print ("Pass" if ((-10, -2) == get_min_max(l)) else "Fail")

l = []  # an empty list
print ("Pass" if (None == get_min_max(l)) else "Fail")


# runtime = O(n) - single traversal
