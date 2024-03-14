#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    liste = dir(hidden_4)
    for i in liste:
        if i[0] != '_':
            print(i)
