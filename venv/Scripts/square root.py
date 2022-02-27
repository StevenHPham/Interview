import math
"""
Problem Statement:

Given a range of numbers, return the sum of all
perfect squares inclusive


"""

def perfect_square(start, end):
    """
    :param n: the high range of the perfect square
    :return: a HashMap of the root and the square
    """

    return {x:x*x for x in range(round(math.sqrt(start)),math.floor(math.sqrt(end))+1)}



def sum_of_square(start,end):
    """
    :param start: this variable indicates the start of the range
    :param end: this variable indicates the end of the range
    :return: the sum of the perfect squares
    """

    dictionary = perfect_square(start,end)


    return sum(list(dictionary))


print(sum_of_square(37,87))




"""
Second Pass
Optimized by removing perfect_square
"""

def sum_of_square2(start,end):
    """
    :param start: this variable indicates the start of the range
    :param end: this variable indicates the end of the range
    :return: the sum of the perfect squares
    """

    dictionary = {x:x*x for x in range(round(math.sqrt(start)),
                                       math.floor(math.sqrt(end))+1)}


    return sum(list(dictionary))