"""
Write a function that that takes a positive integer as a
parameter. The function should return the sum of all the
multiples of 3 and/or 5 less than (but not equal to) the
number passed in
"""
def sum_of_multiples(num):

    # result = 0
    # for x in range(3, num, 3):
    #     if x % 5 != 0:
    #         result += x
    # for x in range(5, num, 5):
    #     result += x

    # multiples = []
    # for x in range(num):
    #     if x % 3 == 0 or x % 5 == 0:
    #         multiples.append(x)
    # result = sum(multiples)

    return sum([x for x in range(num) if x % 3 == 0 or x % 5 == 0])


def test_sum_of_multiples_solution():
    assert sum_of_multiples(10) == 23
    assert sum_of_multiples(20) == 78
    assert sum_of_multiples(0) == 0
    assert sum_of_multiples(1) == 0
    assert sum_of_multiples(200) == 9168
    assert sum_of_multiples(64) == 933