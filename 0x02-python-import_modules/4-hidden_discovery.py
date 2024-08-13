#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    File = dir(hidden_4)
    Length = len(File)
    for i in range(0, Length):
        if File[i][0:2] != "__":
            print(File[i])
