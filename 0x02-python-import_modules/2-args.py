#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    Count = len(sys.argv) - 1
    if Count == 0:
        print("0 arguments.")
    elif Count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(Count))
    for i in range(Count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
