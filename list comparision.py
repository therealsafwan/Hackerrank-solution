if __name__ == '__main__':
    x = int(input("enter the value"))
    y = int(input("enter the value"))
    z = int(input("enter the value"))
    n = int(input("enter the value"))

    result = [[i, j, k]
              for i in range(x + 1)
              for j in range(y + 1)
              for k in range(z + 1)
              if (i + j + k) != n]

    print(result)
