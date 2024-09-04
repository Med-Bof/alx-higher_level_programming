#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    element = -1
    while element >= -(len(my_list)):
        print("{:d}".format(my_list[element]))
        element -= 1
