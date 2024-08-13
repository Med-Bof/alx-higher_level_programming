#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    """Print all names defined in hidden_4 module that do not start with '__'."""

    module_attributes = dir(hidden_4)  # Get a list of all attributes in the hidden_4 module
    num_attributes = len(module_attributes)  # Get the total number of attributes

    for index in range(num_attributes):
        if not module_attributes[index].startswith("__"):  # Check if the name doesn't start with '__'
            print(module_attributes[index])  # Print the name
