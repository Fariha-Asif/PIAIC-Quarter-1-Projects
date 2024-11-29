# Lift_off:

# 1st way:

def count_down1():
    for i in range(10, -1, -1):
        print(i, end=" ")

count_down1()

print("Liftoff")


# 2nd way:

list_number:int = [10,9,8,7,6,5,4,3,2,1]

def count_down2():
    for i in list_number:
        print(i, end=" ")
    print("Liftoff")

count_down2()