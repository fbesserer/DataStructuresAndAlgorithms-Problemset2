def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        min_nr = 0
        max_nr = number
        while max_nr - min_nr > 1:
            middle_nr = (min_nr + max_nr) // 2

            if middle_nr ** 2 == number:
                return middle_nr

            elif middle_nr ** 2 > number:
                max_nr = middle_nr

            elif middle_nr ** 2 < number:
                min_nr = middle_nr

        return min_nr


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (1 == sqrt(2)) else "Fail")
print ("Pass" if  (1 == sqrt(3)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (6 == sqrt(36)) else "Fail")
print ("Pass" if  (25 == sqrt(625)) else "Fail")
print ("Pass" if  (2568 == sqrt(6_594_624)) else "Fail")

# Binary Search O(log n)


