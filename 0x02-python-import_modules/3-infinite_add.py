#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """Calculate and print the sum of command-line arguments."""
    
    num_args = len(sys.argv)
    total_sum = 0

    for index in range(1, num_args):
        total_sum += int(sys.argv[index])
    
    print(total_sum)

