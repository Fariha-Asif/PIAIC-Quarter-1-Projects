# ## Problem Statement

# Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4 

# 4.0 squared is 16.0

def main():
    num:str = input("Type a number to see its square: ")
    num:float = float(num)

    product:float = num**2

    print(str(num) + " squared is " + str(product)) 



if __name__ == '__main__':
    main()