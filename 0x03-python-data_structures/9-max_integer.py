#!/usr/bin/python3
def max_integer(my_list=[]):
    a = 0
    if my_list == []:
        return None
    else:
        for i in my_list:
            a = my_list[0]
            if a < i:
                a = i
        return a
