import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    """
    Generates and prints 10 random numbers in the range 1 to 100.
    """
    for _ in range(N_NUMBERS):  # Loop N_NUMBERS times
        value = random.randint(MIN_VALUE, MAX_VALUE)  # Generate a random number
        print(value, end=' ')  # Print each number with a space
    print()  # Move to a new line after printing all numbers

if __name__ == '__main__':
    main()
