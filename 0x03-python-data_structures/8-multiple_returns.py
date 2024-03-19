#!/usr/bin/python3
def multiple_returns(sentence):
    a = (0, None)
    if sentence == '':
        return a
    else:
        a = (len(sentence), sentence[0])
