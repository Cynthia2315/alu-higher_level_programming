#!/usr/bin/python3
# secure a function that retrives an element from a list like in C
def element_at(my_list, idx):
    if idx < 0:
        return "None"
    elif idx >= len(my_list):
        return "None"
    else:
        return my_list[idx]
