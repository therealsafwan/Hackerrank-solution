#Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

#Mat size must be X. ( is an odd natural number, and  is  times .)
#The design should have 'WELCOME' written in the center.
#The design pattern should only use |, . and - characters.

def print_door_mat(n, m):
    # Top half
    for i in range(1, n, 2):
        print((".|." * i).center(m, '-'))

    # Middle line
    print("WELCOME".center(m, '-'))

    # Bottom half
    for i in range(n - 2, 0, -2):
        print((".|." * i).center(m, '-'))


if __name__ == '__main__':
    n, m = map(int, input().split())
    print_door_mat(n, m)
