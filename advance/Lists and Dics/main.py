# List

fruit_list = ["apple", "mango", "strawberry", "watermelon", "peach"]

# print the length of the list

print(len(fruit_list))

# removed mangoes
fruit_list.remove("mango")

# print updated list
print(fruit_list)

# add mango at the end of the list
fruit_list.append("mango")

# print updated list
print(fruit_list)



# Indexing Game:

def access(user_list: list, index: int) -> None:
    print(user_list[index])

access(fruit_list, 2)

# modify function:

def modify(index, new_value):
    fruit_list[index] = new_value

modify(0, "Mango")

# slice function:

def slice(start_index: int, end_index: int):
    print(fruit_list[start_index:end_index])

slice(1, 3)

# Through Oop:

class ListTaskBuilder:
    def __init__(self, user_list: list[str]):
        self.user_list = user_list

    def access(self, index: int) -> None:
        try:
            print(self.user_list[index])
        except IndexError:
            print(f"Index {index} is out of range.")

    def modify(self, index: int, new_value: str) -> None:
        try:
            self.user_list[index] = new_value
        except IndexError:
            print(f"Index {index} is out of range.")

    def slice(self, start_index: int, end_index: int) -> None:
        print(self.user_list[start_index:end_index])


# Example usage
student_names: list[str] = ["Fariha", "Faraz", "Faham", "Falak"]

task_list = ListTaskBuilder(student_names)

# Access the element at index 1
task_list.access(1)

# Modify the element at index 3
task_list.modify(3, "Farisha")

# Access the modified element at index 3
task_list.access(3)

# Slice the list from index 1 to index 3 (exclusive)
task_list.slice(1, 3)

