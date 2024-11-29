# double_it:

def double_it():
    #type casting with input:

    user_input = int(input("Write any number "))

    # loop:

    while user_input <= 100:
        user_input *= 2
        print(user_input, end=" ")

double_it()