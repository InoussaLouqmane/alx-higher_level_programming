#!/usr/bin/python3
def no_c(my_string):
    news = ''
    for i in my_string:
        if i != 'C' and i !=  'c':
            news += i
    return news
