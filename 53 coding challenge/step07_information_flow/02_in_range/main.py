def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True

    # No need for an else block as return exits the function.
    return False


# Example usage:
print(in_range(5, 1, 10))  # True
print(in_range(11, 1, 10)) # False
print(in_range(1, 1, 10))  # True
print(in_range(10, 1, 10)) # True
