#Consider a list (list = []). You can perform the following commands:
#insert i e: Insert integer  at position .
#print: Print the list.
#remove e: Delete the first occurrence of integer .
#append e: Insert integer  at the end of the list.
#sort: Sort the list.
#pop: Pop the last element from the list.
#reverse: Reverse the list.
#Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
if __name__ == '__main__':
    N = int(input("enter the elements"))
    my_list = []

    for _ in range(N):
        command_input = input().strip().split()
        command = command_input[0]
        args = command_input[1:]

        if command == 'insert':
            my_list.insert(int(args[0]), int(args[1]))
        elif command == 'print':
            print(my_list)
        elif command == 'remove':
            my_list.remove(int(args[0]))
        elif command == 'append':
            my_list.append(int(args[0]))
        elif command == 'sort':
            my_list.sort()
        elif command == 'pop':
            my_list.pop()
        elif command == 'reverse':
            my_list.reverse()
