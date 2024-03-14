#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    ac = len(argv)
    if ac == 1:
        print("0 arguments.")
    elif ac == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(ac - 1))
    if ac >= 2:
        for i in range(1, ac):
            print("{}: {}".format(i, argv[i]))

