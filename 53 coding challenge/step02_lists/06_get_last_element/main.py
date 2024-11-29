def get_last_element(lst):
    """
    Prints the last element of the given list.

    Parameters:
    lst (list): The input list, guaranteed to be non-empty.

    """
    # Access the last element using the negative index
    last_element = lst[-1]
    print(last_element)

# Example usage:
my_list = [1, 2, 3, 4, 5]
get_last_element(my_list)  # Output: 5
