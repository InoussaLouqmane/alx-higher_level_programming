#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    ac = len(argv)
    total = 0

    if ac == 1:
        print("{}".format(total))
    else:
        for i in argv[1:]:
            total += int(i)
        print("{}".format(total))
