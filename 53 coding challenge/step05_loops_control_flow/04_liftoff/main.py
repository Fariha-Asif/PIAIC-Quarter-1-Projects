def main():
    """
    A program to countdown from 10 to 1 and then print 'Liftoff!'.
    """
    for i in range(10, 0, -1):  # Start from 10, go down to 1 (inclusive)
        print(i, end=" ")  # Print each number on the same line with a space
    print("Liftoff!")  # Print 'Liftoff!' after the countdown

if __name__ == "__main__":
    main()
