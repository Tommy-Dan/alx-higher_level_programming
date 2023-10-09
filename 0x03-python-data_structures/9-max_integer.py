#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    large = my_list[0]
    for l in range(len(my_list)):
        if my_list[l] > large:
            large = my_list[l]

    return (large)
