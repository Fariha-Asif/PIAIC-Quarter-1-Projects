# Random Number
# import numpy as np
import random

MIN_NUMBER: int = 1
MAX_NUMBER: int = 101
N_RANDOM_NUMBER: int = 10

# Function:

# for loop:
number_list = []
for i in range(N_RANDOM_NUMBER):
    rand_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    number_list.append(rand_number)


print(*number_list)


# number_list1 = np.random.radint(MIN_NUMBER, MAX_NUMBER, N_RANDOM_NUMBER)
# print(*number_list)