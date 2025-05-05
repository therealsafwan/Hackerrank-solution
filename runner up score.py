if __name__ == '__main__':
    n = int(input("enter the value:"))
    arr = list(map(int, input().split()))

    unique_scores = list(set(arr))       # Remove duplicates
    unique_scores.sort(reverse=True)     # Sort in descending order
    print(unique_scores[1])
