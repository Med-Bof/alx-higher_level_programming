#!/usr/bin/python3

def multiple_returns(sentence):
    lenght = len(sentence)
    if len(sentence) < 1:
        first_Char = None
    else:
        first_Char = sentence[0]

    return lenght, first_Char
