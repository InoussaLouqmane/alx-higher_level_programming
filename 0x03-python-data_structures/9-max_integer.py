#!/usr/bin/python3
def max_integer(my_list=[]):
    a = 0
    if my_list == []:
        return None
    else:
        a = my_list[0]
        for i in my_list:
            if a < i:
                a = i
        return a
