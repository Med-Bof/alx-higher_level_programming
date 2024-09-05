#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_List = []  # Initialize the new list outside of the loop

    for num in my_list:
        if num % 2 == 0:
            new_List.append(True)
        else:
            new_List.append(False)

    return new_List
