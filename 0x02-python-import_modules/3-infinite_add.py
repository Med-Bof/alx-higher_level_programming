#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """Calculate and print the sum of command-line arguments."""
    
    num_args = len(sys.argv)  # Number of command-line arguments including the script name
    total_sum = 0  # Initialize the sum to 0

    for index in range(1, num_args):  # Start from 1 to skip the script name
        total_sum += int(sys.argv[index])  # Convert argument to integer and add to sum
    
    print(total_sum)  # Print the total sum

