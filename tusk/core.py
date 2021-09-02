# Implementation of binary search in python, taken from https://gist.github.com/JonathanSpeek/1f4c7c283c7c3c475ee13d57381765d8

def binary_search(a_list, item):
    """Performs iterative binary search to find the position of an integer in a given, sorted, list.
    a_list -- sorted list of integers
    item -- integer you are searching for the position of
    """

    first = 0
    last = len(a_list) - 1

    while first <= last:
        i = (first + last) // 2
        if a_list[i] == item:
            return i
        elif a_list[i] > item:
            last = i - 1
        elif a_list[i] < item:
            first = i + 1
        else:
            return -1
    return -1