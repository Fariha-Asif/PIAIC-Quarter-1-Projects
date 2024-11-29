def main():
    """
    A program that doubles a user-provided number until it is 100 or greater,
    printing each doubled value along the way.
    """
    # Get the initial number from the user
    curr_value = int(input("Enter a number: "))
    
    # Repeat the doubling process until curr_value is 100 or greater
    while curr_value < 100:
        curr_value = curr_value * 2  # Double the current value
        print(curr_value, end=" ")  # Print the doubled value on the same line

if __name__ == "__main__":
    main()
