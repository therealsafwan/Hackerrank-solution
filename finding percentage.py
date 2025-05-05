if __name__ == '__main__':
    n = int(input("enter the value"))
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # Compute average
    average = sum(student_marks[query_name]) / len(student_marks[query_name])

    # Print with 2 decimal places
    print(f"{average:.2f}")
