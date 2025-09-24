my_arr = (11,21,13,14,55)
print(my_arr)
print(my_arr[3:])
print(len(my_arr))
print(max(my_arr))
print(list(my_arr))
my_list=list(my_arr)
print(my_list[2:6])
print(type(my_arr))
print(type(my_list))
def reverse_string_using_stack(input_string):
    # Step 1: Initialize an empty stack
    stack = []
    
    # Step 2: Push all characters of the string onto the stack
    for char in input_string:
        stack.append(char)
    
    # Step 3: Pop characters from the stack and form the reversed string
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string