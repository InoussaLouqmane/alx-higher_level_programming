#!/usr/bin/python3
def uppercase(str):
    for i in str:
        ascii_code = ord(i)
        if ascii_code > 96:
            i = chr(ascii_code - 32)
        print(f"{i}", end="")
    print()
