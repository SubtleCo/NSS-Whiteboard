"""

Write a function that takes a string of comma separated numbers
and returns the highest and lowest number as a dictionary.

"""

def highest(number_list):
    number_list.sort()
    return number_list[-1]

def lowest(number_list):
    number_list.sort()
    return number_list[0]

def highest_and_lowest(string_o_numbers):
    number_string_list = string_o_numbers.split()
    int_map = map(int, number_string_list)
    number_list = list(int_map)
    # return {
    #     'highest': max(number_list),
    #     'lowest': min(number_list)
    # }
    return {
        'highest': highest(number_list),
        'lowest': lowest(number_list)
    }

def test_highest_and_lowest_solution():
    assert highest_and_lowest('5 4 3 9 7 23') == { 'highest': 23, 'lowest': 3 }
    assert highest_and_lowest('4 5 29 54 4 0 -214 542 -64 1 -3 6 -6') == { 'highest': 542, 'lowest': -214 }
    assert highest_and_lowest('1 -1') == { 'highest': 1, 'lowest': -1 }
    assert highest_and_lowest('42') == { 'highest': 42, 'lowest': 42 }
    assert highest_and_lowest('2189 3105 476 2849 1619 1816 1785 1037 3266 187 446 3032 1743 2940 535 1677 2176 968 176 2078 2404 2867') == { 'highest': 3266, 'lowest': 176 }

