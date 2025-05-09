#Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .
if __name__ == '__main__':
    n = int(input())  # Read the number of elements in the tuple
    integer_list = map(int, raw_input().split())  # Read space-separated integers and convert them to integers (Python 2)
    t = tuple(integer_list)  # Convert the list to a tuple
    print hash(t)  # Compute and print the hash of the tuple (Python 2)
